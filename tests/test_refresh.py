"""
Tests for the data pipeline (`scripts/refresh.py`).

Every test here corresponds to a failure that actually happened in production, not
to a hypothetical. This module had three real incidents in a single week — a silent
history wipe, a truncated YouTube feed that still looked healthy, and a token type
the code didn't understand — and all three were found by running it and watching it
break, which is the expensive way. These pin them.

Run:  python3 -m pytest tests/ -q
"""

import importlib.util
import json
import os

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_spec = importlib.util.spec_from_file_location(
    "refresh", os.path.join(ROOT, "scripts", "refresh.py")
)
refresh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(refresh)


# ==========================================================================
# The staleness guard — 2026-08-20: a partial failure wiped 87 posts
# ==========================================================================

def test_empty_source_keeps_previous_rows():
    data = {"youtube": [], "instagram": [], "facebook": [], "tiktok": []}
    prev = {"youtube": [{"name": "a", "views": 1}]}
    stale = refresh.apply_staleness_guard(data, prev)
    assert data["youtube"] == prev["youtube"]
    assert stale == ["youtube (1 rows kept)"]


def test_populated_source_is_never_overwritten_by_history():
    fresh = [{"name": "new", "views": 9}]
    data = {"youtube": list(fresh), "instagram": [], "facebook": [], "tiktok": []}
    prev = {"youtube": [{"name": "old", "views": 1}]}
    refresh.apply_staleness_guard(data, prev)
    assert data["youtube"] == fresh


def test_partial_failure_flags_only_the_failed_sources():
    """THE regression: Meta succeeded while YouTube and TikTok returned nothing.

    The original guard only refused to write when *every* source was empty, so this
    exact shape destroyed 47 YouTube and 40 TikTok posts while looking like success.
    """
    data = {"youtube": [], "instagram": [{"n": 1}], "facebook": [{"n": 2}], "tiktok": []}
    prev = {"youtube": [{"n": i} for i in range(47)],
            "tiktok": [{"n": i} for i in range(40)],
            "instagram": [{"n": 0}], "facebook": [{"n": 0}]}
    stale = refresh.apply_staleness_guard(data, prev)
    assert len(data["youtube"]) == 47
    assert len(data["tiktok"]) == 40
    assert sorted(s.split(" (")[0] for s in stale) == ["tiktok", "youtube"]
    assert data["instagram"] == [{"n": 1}]      # live data untouched


def test_no_history_means_nothing_to_flag():
    data = {"youtube": [], "instagram": [], "facebook": [], "tiktok": []}
    assert refresh.apply_staleness_guard(data, {}) == []


def test_all_sources_healthy_produces_no_stale_flag():
    data = {k: [{"n": 1}] for k in refresh.SOURCE_KEYS}
    assert refresh.apply_staleness_guard(data, {k: [{"n": 0}] for k in refresh.SOURCE_KEYS}) == []


# ==========================================================================
# Meta token handling — user token vs PAGE token
# ==========================================================================

def test_meta_pages_uses_me_accounts_for_a_user_token(monkeypatch):
    monkeypatch.setattr(refresh, "_mget", lambda url: {
        "data": [{"id": "1", "name": "Cinematic Prompts", "access_token": "pg"}]})
    pages = refresh._meta_pages("user-token")
    assert [p["name"] for p in pages] == ["Cinematic Prompts"]


def test_meta_pages_falls_back_to_page_token(monkeypatch):
    """A Page token's /me IS the Page, so /me/accounts 400s with '(#100) ... (accounts)'.

    CREDENTIALS.md recommends Page tokens because they never expire — following that
    advice used to break the pipeline outright.
    """
    def fake(url):
        if "/me/accounts" in url:
            raise Exception("HTTP Error 400: Bad Request")
        return {"id": "42", "name": "Cinematic Prompts"}
    monkeypatch.setattr(refresh, "_mget", fake)
    pages = refresh._meta_pages("page-token")
    assert len(pages) == 1
    assert pages[0]["id"] == "42"
    assert pages[0]["access_token"] == "page-token"


def test_meta_pages_reraises_when_the_token_is_simply_dead(monkeypatch):
    """A genuinely invalid token must still surface as an error, not an empty list."""
    def fake(url):
        raise Exception("HTTP Error 400: Bad Request")
    monkeypatch.setattr(refresh, "_mget", fake)
    with pytest.raises(Exception):
        refresh._meta_pages("expired-token")


def test_meta_pages_empty_account_list_falls_through_to_page(monkeypatch):
    def fake(url):
        return {"data": []} if "/me/accounts" in url else {"id": "7", "name": "P"}
    monkeypatch.setattr(refresh, "_mget", fake)
    assert refresh._meta_pages("t")[0]["id"] == "7"


# ==========================================================================
# YouTube tail recovery — the truncated feed that still looked healthy
# ==========================================================================

def _stub_uploads(monkeypatch, items):
    """Stub the two endpoints _uploads_tail calls, in order."""
    def fake_urlopen(url):
        if "/channels?" in url:
            payload = {"items": [{"contentDetails": {"relatedPlaylists": {"uploads": "UU1"}}}]}
        else:
            payload = {"items": [
                {"contentDetails": {"videoId": i["id"], "videoPublishedAt": i["date"] + "T00:00:00Z"},
                 "snippet": {"title": i["title"], "publishedAt": i["date"] + "T00:00:00Z"}}
                for i in items]}

        class R:
            def __enter__(self_): return self_
            def __exit__(self_, *a): return False
            def read(self_): return json.dumps(payload).encode()
        return R()

    monkeypatch.setattr(refresh.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(refresh.json, "load", lambda r: json.loads(r.read()))


def test_uploads_tail_recovers_only_newer_videos(monkeypatch):
    found = [{"id": "old", "title": "Old", "date": "2026-07-03"}]
    _stub_uploads(monkeypatch, [
        {"id": "new1", "title": "Newer", "date": "2026-08-20"},
        {"id": "stale", "title": "Older", "date": "2026-06-01"},
    ])
    extra = refresh._uploads_tail("key", found)
    assert [v["id"] for v in extra] == ["new1"]


def test_uploads_tail_skips_ids_already_discovered(monkeypatch):
    found = [{"id": "dup", "title": "D", "date": "2026-07-03"}]
    _stub_uploads(monkeypatch, [{"id": "dup", "title": "D", "date": "2026-08-01"}])
    assert refresh._uploads_tail("key", found) == []


def test_uploads_tail_is_a_noop_without_a_cutoff():
    """No curated results means no cutoff, so recovery can't reason about a tail."""
    assert refresh._uploads_tail("key", []) == []


def test_uploads_tail_never_raises(monkeypatch):
    """Recovery is best-effort: it must not take the whole refresh down with it."""
    def boom(url):
        raise Exception("network down")
    monkeypatch.setattr(refresh.urllib.request, "urlopen", boom)
    assert refresh._uploads_tail("key", [{"id": "a", "date": "2026-01-01"}]) == []


# ==========================================================================
# Reading back the previous dashboard
# ==========================================================================

def test_load_previous_dash_parses_the_written_format(tmp_path, monkeypatch):
    p = tmp_path / "data.js"
    p.write_text("/* header */\nwindow.DASH = " + json.dumps({"youtube": [{"v": 1}]}) + ";\n",
                 encoding="utf-8")
    monkeypatch.setattr(refresh, "DATA_JS_PATH", str(p))
    assert refresh._load_previous_dash()["youtube"] == [{"v": 1}]


def test_load_previous_dash_returns_empty_on_garbage(tmp_path, monkeypatch):
    """Must degrade to {} — never raise — or a corrupt file blocks every future run."""
    p = tmp_path / "data.js"
    p.write_text("window.DASH = {not json;", encoding="utf-8")
    monkeypatch.setattr(refresh, "DATA_JS_PATH", str(p))
    assert refresh._load_previous_dash() == {}


def test_load_previous_dash_returns_empty_when_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_JS_PATH", str(tmp_path / "nope.js"))
    assert refresh._load_previous_dash() == {}


# ==========================================================================
# Network timeouts — 2026-08-22: a stalled socket hung the whole refresh
# ==========================================================================

def test_a_default_socket_timeout_is_set():
    """urllib blocks forever by default, so one stalled call froze the entire run.

    Reported as a KeyboardInterrupt traceback mid-SSL-read: the script had no
    timeout anywhere, so a flaky connection meant Ctrl+C and a lost pull.
    """
    import socket as _socket
    assert _socket.getdefaulttimeout() is not None, "no default socket timeout set"
    assert 0 < _socket.getdefaulttimeout() <= 120


def test_timeout_is_overridable():
    assert refresh.NET_TIMEOUT == float(os.environ.get("REFRESH_TIMEOUT", "45"))
