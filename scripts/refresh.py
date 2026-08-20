#!/usr/bin/env python3
"""One command: pull the live numbers and rewrite the dashboard data.

  python scripts/refresh.py     (or ./run.sh)

Sources actually used by this script:
- YouTube views per video          (YouTube Data API)
- TikTok views                     (TikTok Display API if authorized via
                                    scripts/tiktok_auth.py; else manual from data/videos.csv)
- Instagram + Facebook             (Meta API where available; the videos.csv
                                    columns are the source of truth and override the API)
- App Store downloads: all-time + last ~2 months  (App Store Connect Sales reports)

Output: writes dashboard/data.js (window.DASH). The dashboard reads that file on
open — it does NOT edit index.html. This is the ONE canonical refresh script;
older forks (dashboard/refresh.py, scripts/roriginal-efresh.py) were removed in
the 2026-08-03 rebuild.
"""
import os, sys, csv, json, time, datetime, urllib.parse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH  = os.path.join(ROOT, "data", "videos.csv")
DATA_JS_PATH = os.path.join(ROOT, "dashboard", "data.js")
# Date you began posting the same video to all platforms on the same day.
# On/after this date: same date = one cross-platform row (posts auto-merge by date).
# Before it: each post stays its own single-platform row. Override in .env if needed.
SYNC_START_DEFAULT = "2026-06-13"
ID_FIELD = {"youtube":"youtube_id", "instagram":"instagram_id", "facebook":"facebook_id"}
CSV_COLS = ["name","campaign","date","youtube_id","instagram_id","facebook_id","tiktok","instagram","facebook"]

def load_env(path=os.path.join(ROOT, ".env")):
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def fetch_youtube(ids):
    key = os.environ.get("YT_API_KEY"); ids = [i for i in ids if i]
    if not key or not ids: return {}
    out = {}
    for i in range(0, len(ids), 50):
        url = "https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode(
            {"part":"statistics","id":",".join(ids[i:i+50]),"key":key})
        with urllib.request.urlopen(url) as r: data = json.load(r)
        for it in data.get("items",[]):
            out[it["id"]] = int(it["statistics"].get("viewCount",0))
    return out

def youtube_uploads():
    """Discover videos from the configured playlist (default) — or, if no playlist
    is set, all channel uploads. Returns [{id, title, date}]. Empty on failure.
    Note: with an API key the playlist must be public or unlisted (not private)."""
    key = os.environ.get("YT_API_KEY")
    if not key: return []
    playlist = os.environ.get("YOUTUBE_PLAYLIST", "PL-LTlFdhHph8WLeZG0ARi_P4Px6pg1nat").strip()
    out = []                     # hoisted: the except-handler returns partial results
    try:
        if not playlist:                                    # fall back to channel uploads
            handle = os.environ.get("YOUTUBE_CHANNEL", "@wolframbrandhoff941").lstrip("@")
            if not handle: return []
            u = "https://www.googleapis.com/youtube/v3/channels?" + urllib.parse.urlencode(
                {"part":"contentDetails","forHandle":handle,"key":key})
            with urllib.request.urlopen(u) as r: data = json.load(r)
            items = data.get("items",[])
            if not items: print("  · channel not found for handle @"+handle); return []
            playlist = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
        token = None
        # NOTE: this playlist has a poisoned entry around position ~36-40 (a deleted or
        # otherwise broken item). ANY page that spans it returns a bogus 404. We therefore
        # keep whatever we collected before the failure instead of discarding it — losing
        # the tail is survivable, losing all 47 videos is not. main() backfills the rest
        # from the youtube_id column in data/videos.csv.
        while True:
            # maxResults=35, NOT the API maximum of 50. A broken entry sits at roughly
            # position 36-40, and ANY page spanning it returns a bogus 404 "playlist
            # cannot be found" (verified 2026-08-20: 35 works, 40 fails). 35 is the
            # largest page that still succeeds, so it salvages the most before the
            # pagination dies. That 404 previously emptied the entire YouTube history.
            params = {"part":"contentDetails,snippet","playlistId":playlist,"maxResults":35,"key":key}
            if token: params["pageToken"] = token
            pu = "https://www.googleapis.com/youtube/v3/playlistItems?" + urllib.parse.urlencode(params)
            with urllib.request.urlopen(pu) as r: pd = json.load(r)
            for it in pd.get("items",[]):
                out.append({"id": it["contentDetails"]["videoId"],
                            "title": it["snippet"]["title"],
                            "date": (it["contentDetails"].get("videoPublishedAt")
                                     or it["snippet"].get("publishedAt",""))[:10]})
            token = pd.get("nextPageToken")
            if not token: break
        return out
    except Exception as e:
        if out:
            print(f"  · YouTube pagination stopped early ({e}) — kept {len(out)} discovered so far")
            return out
        print(f"  · YouTube discovery skipped ({e})"); return []

# ---------- App Store ----------
def _month_strings(today, n=12):
    y, m, out = today.year, today.month, []
    for _ in range(n):
        m -= 1
        if m == 0: m = 12; y -= 1
        out.append(f"{y:04d}-{m:02d}")
    return out

def _daterange(start, end):
    d = start
    while d <= end:
        yield d; d += datetime.timedelta(days=1)

CACHE_PATH = os.path.join(ROOT, "data", ".daily_downloads_cache.json")

def appstore_totals():
    """Return (all_time, last_60) first-time downloads by summing DAILY reports.
    Monthly reports are unreliable on newer accounts, so we sum daily and cache
    finalized days — first run is slow, later runs only fetch the newest days."""
    need = ["ASC_KEY_ID","ASC_ISSUER_ID","ASC_VENDOR_NUMBER","ASC_PRIVATE_KEY_PATH"]
    if any(not os.environ.get(n) for n in need): return None, None, []
    try: import jwt, gzip, io, time, requests
    except ImportError: return None, None, []

    now = int(time.time())
    token = jwt.encode({"iss":os.environ["ASC_ISSUER_ID"],"iat":now,"exp":now+60*19,
                        "aud":"appstoreconnect-v1"},
                       open(os.environ["ASC_PRIVATE_KEY_PATH"]).read(),
                       algorithm="ES256", headers={"kid":os.environ["ASC_KEY_ID"]})
    vendor = os.environ["ASC_VENDOR_NUMBER"]

    try: cache = json.load(open(CACHE_PATH))
    except Exception: cache = {}

    def fetch_day(ds):
        r = requests.get("https://api.appstoreconnect.apple.com/v1/salesReports",
            headers={"Authorization":f"Bearer {token}","Accept":"application/a-gzip"},
            params={"filter[frequency]":"DAILY","filter[reportDate]":ds,
                    "filter[reportType]":"SALES","filter[reportSubType]":"SUMMARY",
                    "filter[vendorNumber]":vendor,"filter[version]":"1_1"})
        if r.status_code != 200: return 0
        tsv = gzip.GzipFile(fileobj=io.BytesIO(r.content)).read().decode("utf-8")
        # total downloads = first-time ("1*") + redownloads ("3*"), matching
        # App Store Connect's "Total Downloads". Updates/other types are excluded.
        return sum(int(row.get("Units",0) or 0)
                   for row in csv.DictReader(io.StringIO(tsv), delimiter="\t")
                   if (row.get("Product Type Identifier","") or "").strip()[:1] in ("1","3"))

    today = datetime.date.today()
    yest  = today - datetime.timedelta(days=1)
    start = yest - datetime.timedelta(days=364)         # last 12 months of daily data
    # Apple keeps revising DAILY Sales reports for well over a week (a day fetched
    # during the reporting lag can read 0, then gain downloads days later). Only trust
    # the cache once a day is comfortably finalized; always re-fetch the recent window
    # so late-arriving downloads aren't lost. (Was 3 days — that froze recent days at 0.)
    final_before = today - datetime.timedelta(days=16)
    vals, fetched, changed = {}, 0, False
    d = start
    while d <= yest:
        ds = d.isoformat()
        if ds in cache and d < final_before:
            vals[ds] = cache[ds]
        else:
            vals[ds] = fetch_day(ds); cache[ds] = vals[ds]; changed = True; fetched += 1
            if fetched % 20 == 0: sys.stdout.write("."); sys.stdout.flush()
        d += datetime.timedelta(days=1)
    if changed:
        try: json.dump(cache, open(CACHE_PATH, "w"))
        except Exception: pass
    if fetched: print()

    all_time = sum(vals.values())
    # daily series spans the full active period (first day with a download → now)
    nonzero = [ds for ds, v in vals.items() if v > 0]
    start_ds = min(nonzero) if nonzero else (yest - datetime.timedelta(days=59)).isoformat()
    daily = [{"d": ds, "n": v} for ds, v in sorted(vals.items()) if ds >= start_ds]
    cutoff = (yest - datetime.timedelta(days=59)).isoformat()
    last60 = sum(v for ds, v in vals.items() if ds >= cutoff)
    return all_time, last60, daily

# ---------------------------------------------------------------------------
# Meta (Instagram + Facebook) — dormant until META_ACCESS_TOKEN is set in .env.
# Reads your own posts' view counts. First real run will need metric calibration
# (Meta's insight metric names vary by content type / API version).
# ---------------------------------------------------------------------------
META_GRAPH = "https://graph.facebook.com/v22.0"

def _mget(url):
    with urllib.request.urlopen(url) as r: return json.load(r)

def _meta_views(post_id, token, metrics):
    """Try a list of insight metrics; return the first numeric value found."""
    for metric in metrics:
        try:
            d = _mget(META_GRAPH + f"/{post_id}/insights?" + urllib.parse.urlencode(
                {"metric": metric, "period": "lifetime", "access_token": token}))
            vals = d.get("data", [])
            if vals:
                item = vals[0]
                v = item.get("value")
                if v is None:
                    v = item.get("values", [{}])[0].get("value")
                if isinstance(v, (int, float)): return int(v)
        except Exception:
            continue
    return None

def meta_refresh_token(token):
    """Exchange a token for a fresh long-lived one when app creds are present."""
    app_id, secret = os.environ.get("META_APP_ID"), os.environ.get("META_APP_SECRET")
    if not (app_id and secret): return token
    try:
        d = _mget(META_GRAPH + "/oauth/access_token?" + urllib.parse.urlencode(
            {"grant_type":"fb_exchange_token","client_id":app_id,
             "client_secret":secret,"fb_exchange_token":token}))
        return d.get("access_token", token)
    except Exception:
        return token

def meta_fetch():
    """Discover the Page + linked IG account from the token and pull per-post
    views. Returns (ig_views{id:views}, fb_views{id:views}, discovered[list]).
    ({},{},[]) when no token, so the whole feature is opt-in."""
    token = os.environ.get("META_ACCESS_TOKEN")
    if not token:
        print("  · Meta off (no META_ACCESS_TOKEN in .env)"); return {}, {}, []
    ig_token = token  # preserve original token — refreshed token loses IG insights access
    token = meta_refresh_token(token)
    ig_views, fb_views, discovered = {}, {}, []
    try:
        pages = _mget(META_GRAPH + "/me/accounts?" + urllib.parse.urlencode(
            {"fields":"id,name,access_token,instagram_business_account","access_token":token})).get("data", [])
        if not pages:
            print("  · token valid but no Pages returned — check it has pages_show_list "
                  "+ pages_read_engagement and that a Page is linked to your account")
            return {}, {}, []
        print(f"  · {len(pages)} Page(s) found: " + ", ".join(p.get("name","?") for p in pages))
        for pg in pages:
            ptoken = pg.get("access_token", token)
            # Facebook: use video_reels endpoint + direct `views` field for Reels
            # (the posts/insights endpoint undercounts Reel plays ~6x).
            # Also fetch the posts feed to catch older non-Reel video posts.
            # Reels data takes priority; posts fill in anything not covered.
            reels_by_date = {}
            try:
                cursor = None
                while True:
                    params = {"fields":"id,description,title,created_time,views","limit":100,"access_token":ptoken}
                    if cursor: params["after"] = cursor
                    page_data = _mget(META_GRAPH + f"/{pg['id']}/video_reels?" + urllib.parse.urlencode(params))
                    for reel in page_data.get("data", []):
                        caption = (reel.get("description") or reel.get("title") or "")[:40]
                        date = reel.get("created_time","")[:10]
                        v = reel.get("views")
                        fb_views[reel["id"]] = v
                        reels_by_date[date] = (reel["id"], caption, v)
                        discovered.append(("FB", reel["id"], caption, date, v))
                    cursor = page_data.get("paging", {}).get("cursors", {}).get("after")
                    if not page_data.get("paging", {}).get("next"): break
            except Exception as e:
                print(f"  · FB reels skipped ({e})")
            try:
                fb = _mget(META_GRAPH + f"/{pg['id']}/posts?" + urllib.parse.urlencode(
                    {"fields":"id,message,created_time","limit":100,"access_token":ptoken}))
                for post in fb.get("data", []):
                    date = post.get("created_time","")[:10]
                    if date in reels_by_date:
                        continue  # already have accurate reel data for this date
                    v = _meta_views(post["id"], ptoken, ["post_video_views","post_impressions_unique","post_impressions"])
                    fb_views[post["id"]] = v
                    discovered.append(("FB", post["id"], (post.get("message") or "")[:40], date, v))
            except Exception as e:
                print(f"  · FB posts skipped ({e})")
            ig = pg.get("instagram_business_account", {})
            if ig.get("id"):
                try:
                    med = _mget(META_GRAPH + f"/{ig['id']}/media?" + urllib.parse.urlencode(
                        {"fields":"id,caption,timestamp,media_type","limit":100,"access_token":ig_token}))
                    for m in med.get("data", []):
                        v = _meta_views(m["id"], ig_token, ["views"])
                        ig_views[m["id"]] = v
                        discovered.append(("IG", m["id"], (m.get("caption") or "")[:40], m.get("timestamp","")[:10], v))
                except Exception as e:
                    print(f"  · IG media skipped ({e})")
        return ig_views, fb_views, discovered
    except urllib.error.HTTPError as e:
        try: body = e.read().decode()[:300]
        except Exception: body = ""
        print(f"  · Meta API error {e.code}: {body}")
        return {}, {}, []
    except Exception as e:
        print(f"  · Meta fetch error ({e})")
        return {}, {}, []

# ---------------------------------------------------------------------------
# TikTok (Display API) — dormant until TikTok creds + a token are set up.
# Run scripts/tiktok_auth.py once to authorize; it saves a refresh token.
# ---------------------------------------------------------------------------
TIKTOK_TOKEN_CACHE = os.path.join(ROOT, "data", ".tiktok_token.json")

def tiktok_access_token():
    """Cached access_token while still valid; refresh-token grant as fallback.
    TikTok has been rejecting the refresh_token grant with invalid_client even
    right after a fresh, successful auth (confirmed Aug 10 — same client_key/
    secret that just worked for authorization_code fails for refresh_token,
    consistently, with or without a delay). Using the cached access_token
    directly for its real ~24h validity window sidesteps that; the refresh
    grant is still attempted as a fallback in case TikTok fixes it server-side.
    """
    key, secret = os.environ.get("TIKTOK_CLIENT_KEY"), os.environ.get("TIKTOK_CLIENT_SECRET")
    if not (key and secret): return None
    cached = {}
    try: cached = json.load(open(TIKTOK_TOKEN_CACHE))
    except Exception: pass

    obtained_at, expires_in, cached_access = cached.get("obtained_at"), cached.get("expires_in"), cached.get("access_token")
    if cached_access and obtained_at and expires_in and time.time() < obtained_at + expires_in - 300:
        return cached_access  # still valid (5-min safety margin)

    refresh = cached.get("refresh_token") or os.environ.get("TIKTOK_REFRESH_TOKEN")
    if not refresh: return None
    try:
        body = urllib.parse.urlencode({"client_key":key, "client_secret":secret,
            "grant_type":"refresh_token", "refresh_token":refresh}).encode()
        req = urllib.request.Request("https://open.tiktokapis.com/v2/oauth/token/",
            data=body, headers={"Content-Type":"application/x-www-form-urlencoded"})
        d = json.load(urllib.request.urlopen(req))
        if d.get("refresh_token"):
            try:
                d["obtained_at"] = int(time.time())
                json.dump(d, open(TIKTOK_TOKEN_CACHE, "w"))
            except Exception: pass
        return d.get("access_token")
    except urllib.error.HTTPError as e:
        try: body = e.read().decode()[:200]
        except Exception: body = ""
        print(f"  · TikTok token refresh failed {e.code}: {body}"); return None
    except Exception as e:
        print(f"  · TikTok token error ({e})"); return None

def tiktok_fetch():
    """Pull your own TikTok videos with view counts. [] if not set up."""
    if not os.environ.get("TIKTOK_CLIENT_KEY"):
        return []                       # not configured → silent, fall back to manual
    token = tiktok_access_token()
    if not token:
        print("  · TikTok configured but no token — run scripts/tiktok_auth.py once"); return []
    out, cursor, page = [], None, 0
    fields = "id,title,video_description,view_count,create_time"
    try:
        while page < 10:
            body = {"max_count": 20}
            if cursor: body["cursor"] = cursor
            req = urllib.request.Request(
                "https://open.tiktokapis.com/v2/video/list/?fields=" + urllib.parse.quote(fields),
                data=json.dumps(body).encode(),
                headers={"Authorization":"Bearer "+token, "Content-Type":"application/json"})
            d = json.load(urllib.request.urlopen(req)).get("data", {})
            for v in d.get("videos", []):
                name = (v.get("title") or v.get("video_description") or "")[:40]
                ts = v.get("create_time")
                date = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date().isoformat() if ts else ""
                out.append({"name": name, "date": date, "views": v.get("view_count")})
            if d.get("has_more") and d.get("cursor"): cursor = d["cursor"]; page += 1
            else: break
        print(f"  · {len(out)} TikTok videos")
        return out
    except urllib.error.HTTPError as e:
        try: body = e.read().decode()[:200]
        except Exception: body = ""
        print(f"  · TikTok API error {e.code}: {body}"); return []
    except Exception as e:
        print(f"  · TikTok fetch error ({e})"); return []

def _load_previous_dash():
    """Parse the existing dashboard/data.js into a dict, or {} if absent/unreadable."""
    if not os.path.exists(DATA_JS_PATH):
        return {}
    try:
        import re as _re
        raw = open(DATA_JS_PATH, encoding="utf-8").read()
        m = _re.search(r"window\.DASH\s*=\s*(\{.*\});", raw, _re.S)
        return json.loads(m.group(1)) if m else {}
    except Exception:
        return {}

def main():
    load_env()
    rows = list(csv.DictReader(open(CSV_PATH)))   # videos.csv used only for manual TikTok fallback

    print("Discovering YouTube (playlist) …")
    uploads = youtube_uploads()
    # Backfill any video recorded in videos.csv that playlist discovery didn't reach
    # (the playlist paginates badly — see youtube_uploads). CSV is the durable record.
    seen = {u["id"] for u in uploads}
    missing = []
    for r in rows:
        vid = (r.get("youtube_id") or "").strip()
        if vid and vid not in seen:
            seen.add(vid)
            missing.append({"id": vid, "title": (r.get("name") or "").strip(), "date": (r.get("date") or "").strip()})
    if missing:
        print(f"  · backfilled {len(missing)} video(s) from videos.csv that discovery missed")
        uploads = uploads + missing
    yt_views = fetch_youtube([u["id"] for u in uploads]) if uploads else {}
    youtube = [{"name": u["title"], "date": u["date"], "views": yt_views.get(u["id"])} for u in uploads]
    print(f"  · {len(youtube)} videos, {sum(v for v in yt_views.values()):,} views")

    print("Fetching Meta (Instagram + Facebook) …")
    ig_views, fb_views, discovered = meta_fetch()
    # IG: CSV column is the source of truth (API cannot return real Reel play counts).
    # Use the manual instagram column when present; fall back to the API value otherwise.
    ig_manual = {}
    for r in rows:
        iv = (r.get("instagram") or "").strip()
        date = (r.get("date") or "").strip()
        if iv and date:
            try: ig_manual[date] = int(iv)
            except ValueError: pass
    instagram = []
    for (plat, pid, cap, date, views) in discovered:
        if plat != "IG": continue
        instagram.append({"name": cap, "date": date, "views": ig_manual.get(date, views)})
    if ig_manual:
        n = sum(1 for i in instagram if i["date"] in ig_manual)
        print(f"  · {n} IG view(s) from videos.csv")

    # Manual FB override: CSV rows with facebook_id + facebook column (or date + facebook).
    # post_video_views is now tried first but may still lag; CSV is the source of truth.
    fb_manual_by_id, fb_manual_by_date = {}, {}
    for r in rows:
        fv = (r.get("facebook") or "").strip()
        if not fv: continue
        try: val = int(fv)
        except ValueError: continue
        fbid = (r.get("facebook_id") or "").strip()
        date = (r.get("date") or "").strip()
        if fbid: fb_manual_by_id[fbid] = val
        elif date: fb_manual_by_date[date] = val
    fb_overrides = 0
    facebook = []
    for (plat, pid, cap, date, views) in discovered:
        if plat != "FB": continue
        v = fb_manual_by_id.get(pid, fb_manual_by_date.get(date, views))
        if v != views: fb_overrides += 1
        facebook.append({"name": cap, "date": date, "views": v})
    if fb_overrides:
        print(f"  · {fb_overrides} FB view(s) overridden from videos.csv")

    # Facebook is now REAL data only (API values + any videos.csv overrides above).
    # NOTE (rebuild 2026-08-03): a block of 9 FAKE backdated FB posts used to be
    # prepended here, silently inflating every Facebook average. It has been
    # removed. Do not reintroduce fabricated posts — if FB history is thin, show
    # it thin. Analysis must run on real numbers only.

    if discovered:
        print(f"  · {len(instagram)} IG + {len(facebook)} FB posts")

    print("Fetching App Store (summing daily reports) …")
    all_time, last60, daily = appstore_totals()
    if all_time is None:
        print("  · skipped (no Apple creds)")
    else:
        print(f"  · {all_time} downloads all-time · {last60} in the last ~2 months")

    # TikTok: from the Display API if set up, otherwise manual (videos.csv rows with a tiktok value)
    print("Fetching TikTok …")
    tiktok = tiktok_fetch()
    if not tiktok:
        for r in rows:
            tv = (r.get("tiktok") or "").strip()
            if tv:
                try: tiktok.append({"name": r.get("name") or "", "date": r.get("date") or "", "views": int(tv)})
                except ValueError: pass
        print(f"  · {len(tiktok)} manual TikTok posts (from videos.csv)")

    data = {"youtube": youtube, "instagram": instagram, "facebook": facebook, "tiktok": tiktok,
            "downloads": all_time if all_time is not None else 0,
            "downloads60": last60 if last60 is not None else 0,
            "daily": daily,
            "updated": datetime.datetime.now().isoformat(timespec="seconds")}
    prev = _load_previous_dash()

    # A failed API call must never silently destroy history. If a source came back
    # empty but we had rows for it last run, keep the old rows and flag them stale.
    # (Before this guard, a YouTube 404 + expired TikTok token wiped 47 and 40 posts
    #  while Meta succeeded, so the all-sources-empty check below never fired.)
    stale = []
    for _key in ("youtube", "instagram", "facebook", "tiktok"):
        if not data[_key] and prev.get(_key):
            data[_key] = prev[_key]
            stale.append(f"{_key} ({len(prev[_key])} rows kept)")
    if stale:
        data["stale"] = [s.split(" (")[0] for s in stale]
        print("\n  ! STALE — these sources failed this run; previous rows kept:")
        for s in stale:
            print(f"      · {s}")
        print("    Their numbers are LAST KNOWN GOOD, not current. Fix the source before trusting them.")

    fetched_nothing = (not youtube and not instagram and not facebook and not tiktok
                       and not daily and (all_time in (None, 0)))
    if fetched_nothing and os.path.exists(DATA_JS_PATH):
        _had = any(prev.get(k) for k in ("youtube","instagram","facebook","tiktok","daily")) or prev.get("downloads")
        if _had:
            print("\n\u2717 Refusing to overwrite data.js \u2014 pulled 0 from every source (keys missing?).")
            print("  Your existing dashboard was left untouched. Restore .env + .p8, then re-run.\n")
            sys.exit(1)
    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write("/* Saved data — written by refresh.py. The dashboard reads this on open. */\n")
        f.write("window.DASH = " + json.dumps(data, indent=2) + ";\n")
    print(f"\n✓ saved to {os.path.relpath(DATA_JS_PATH, ROOT)} — open dashboard/index.html (no need to re-run)\n")

if __name__ == "__main__":
    main()
