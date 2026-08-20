"""
Tests for the ship gate (`scripts/preflight.py`).

Why this suite exists: the gate is the one component that mechanically blocks bad
content from shipping. Every rule in it was added because a real mistake reached a
real platform — so a regression here silently re-opens a hole that already cost views
once. These tests pin each rule to a failing example.

Run:  python3 -m pytest tests/ -q
"""

import importlib.util
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# scripts/ is not a package, so load preflight.py by path.
_spec = importlib.util.spec_from_file_location(
    "preflight", os.path.join(ROOT, "scripts", "preflight.py")
)
preflight = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(preflight)


@pytest.fixture(scope="module")
def reg():
    return preflight.load_registry()


def run_check(platform, lines, reg):
    """Run check_platform and return (errors, warns, notes)."""
    errors, warns, notes = [], [], []
    preflight.check_platform(platform, lines, reg, errors, warns, notes)
    return errors, warns, notes


GROUNDED = "Grounding: test pattern, 999"


# --------------------------------------------------------------------------
# parse() — attributing lines to the right platform
# --------------------------------------------------------------------------

def write(tmp_path, text):
    p = tmp_path / "pkg.md"
    p.write_text(text, encoding="utf-8")
    return str(p)


def test_parse_attributes_lines_to_platform_heading(tmp_path):
    path = write(tmp_path, "## TikTok (lead) — caption\nhello tiktok\n")
    assert preflight.parse(path)["tiktok"] == ["hello tiktok"]


def test_parse_horizontal_rule_closes_section(tmp_path):
    path = write(tmp_path, "## TikTok\nmine\n---\northaned\n")
    assert preflight.parse(path)["tiktok"] == ["mine"]


def test_parse_non_platform_heading_closes_section(tmp_path):
    path = write(tmp_path, "## TikTok\nmine\n## CTA used this round\nnot tiktok\n")
    assert preflight.parse(path)["tiktok"] == ["mine"]


def test_parse_hashtag_line_is_not_a_heading(tmp_path):
    """A '#aivideo' line must not be mistaken for a markdown heading."""
    path = write(tmp_path, "## TikTok\n#aivideo #aicinema\n")
    assert preflight.parse(path)["tiktok"] == ["#aivideo #aicinema"]


def test_parse_reels_alias_maps_to_instagram(tmp_path):
    path = write(tmp_path, "## Instagram Reels — caption\ncopy\n")
    assert preflight.parse(path)["instagram"] == ["copy"]


# --------------------------------------------------------------------------
# tags_in() — only a *pure* hashtag line counts as the post's tags
# --------------------------------------------------------------------------

def test_tags_from_pure_hashtag_line():
    assert preflight.tags_in(["#aivideo #aicinema"]) == ["#aivideo", "#aicinema"]


def test_tags_ignores_hashtags_mentioned_in_prose():
    lines = ["We dropped #fyp because it does nothing."]
    assert preflight.tags_in(lines) == []


def test_tags_ignores_backticked_tag_references():
    lines = ["Removed `#nanobanana` on this platform."]
    assert preflight.tags_in(lines) == []


def test_tags_strips_markdown_emphasis():
    assert preflight.tags_in(["**#aivideo #aicinema**"]) == ["#aivideo", "#aicinema"]


def test_tags_strips_leading_label():
    assert preflight.tags_in(["Hashtags: #aivideo #aicinema"]) == ["#aivideo", "#aicinema"]


# --------------------------------------------------------------------------
# caption_text() — backend lines are not visible copy
# --------------------------------------------------------------------------

def test_caption_text_drops_backend_tag_lines():
    lines = ["visible copy", "**Backend tags:** kling, runway"]
    assert "kling" not in preflight.caption_text(lines).lower()


# --------------------------------------------------------------------------
# has_grounding() — show your work, with a real number
# --------------------------------------------------------------------------

def test_grounding_with_number_is_accepted():
    ground, ground_num, exp = preflight.has_grounding(["Grounding: transformation, 1987"])
    assert ground and ground_num and not exp


def test_grounding_without_number_is_flagged():
    ground, ground_num, exp = preflight.has_grounding(["Grounding: transformation"])
    assert ground and not ground_num


def test_experiment_line_is_recognised():
    _, _, exp = preflight.has_grounding(["Experiment: trending audio. Signal: clears 100 → keep."])
    assert exp


def test_missing_grounding_is_an_error(reg):
    errors, _, _ = run_check("tiktok", ["copy", "#aivideo #aicinema #aifilmmaking"], reg)
    assert any("no grounding" in e for e in errors)


def test_grounding_without_number_is_an_error(reg):
    lines = ["Grounding: transformation", "copy", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("names no number" in e for e in errors)


# --------------------------------------------------------------------------
# hashtag rules
# --------------------------------------------------------------------------

def test_clean_tiktok_block_passes(reg):
    lines = [GROUNDED, "Pick the light before you generate.", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert errors == []


def test_banned_tag_everywhere_is_rejected(reg):
    lines = [GROUNDED, "copy", "#aivideo #aicinema #fyp"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("#fyp" in e and "banned everywhere" in e for e in errors)


def test_tag_forbidden_on_youtube_is_rejected(reg):
    """#cinematicprompts returns zero on YouTube — brand terms belong in backend metadata."""
    lines = [GROUNDED, "copy", "#shorts #aivideo #cinematicprompts"]
    errors, _, _ = run_check("youtube", lines, reg)
    assert any("#cinematicprompts" in e and "forbidden on youtube" in e for e in errors)


def test_unverified_tag_is_rejected(reg):
    lines = [GROUNDED, "copy", "#aivideo #aicinema #totallymadeup"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("#totallymadeup" in e and "unverified" in e for e in errors)


def test_instagram_requires_exactly_five_tags(reg):
    lines = [GROUNDED, "copy", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("instagram", lines, reg)
    assert any("should be 5–5" in e for e in errors)


def test_commerce_tag_rejected_on_non_commerce_copy(reg):
    """#aiproductphotography is real but only fits product/fashion/commerce content."""
    lines = [GROUNDED, "Golden Hour light on the water.",
             "#aivideo #aicinema #aiproductphotography"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("#aiproductphotography" in e for e in errors)


def test_commerce_tag_allowed_on_product_copy(reg):
    lines = [GROUNDED, "Studio product shots without the studio.",
             "#aivideo #aicinema #aiproductphotography"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert errors == []


# --------------------------------------------------------------------------
# visible-copy landmines
# --------------------------------------------------------------------------

def test_generator_name_in_visible_copy_is_rejected(reg):
    lines = [GROUNDED, "Built with Kling in one pass.", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("kling" in e.lower() for e in errors)


def test_generator_name_in_backend_line_is_allowed(reg):
    lines = [GROUNDED, "Pick the light.", "**Backend tags:** kling, runway, seedance",
             "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert errors == []


def test_engagement_bait_is_rejected(reg):
    lines = [GROUNDED, "Follow for more prompts.", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("engagement bait" in e for e in errors)


@pytest.mark.parametrize("phrase", ["no wasted credits", "lands first try", "harsh noon"])
def test_claim_landmines_are_rejected(reg, phrase):
    """The most-corrected mistakes in this project's history — each must stay blocked."""
    lines = [GROUNDED, f"This one has {phrase} in it.", "#aivideo #aicinema #aifilmmaking"]
    errors, _, _ = run_check("tiktok", lines, reg)
    assert any("claim landmine" in e for e in errors)


def test_youtube_private_mention_is_rejected(reg):
    lines = [GROUNDED, "Upload is still Private.", "#shorts #aivideo #nanobananapro"]
    errors, _, _ = run_check("youtube", lines, reg)
    assert any("Private" in e for e in errors)


def test_youtube_without_private_gets_visibility_warning(reg):
    """The gate cannot see the real toggle, so it must always remind."""
    lines = [GROUNDED, "Pick the light.", "#shorts #aivideo #nanobananapro"]
    errors, warns, _ = run_check("youtube", lines, reg)
    assert errors == []
    assert any("visibility" in w for w in warns)


def test_absent_platform_is_skipped(reg):
    """A package that omits a platform must not be penalised for it."""
    errors, warns, notes = run_check("facebook", [], reg)
    assert (errors, warns, notes) == ([], [], [])


# --------------------------------------------------------------------------
# integration — the shipped example package must stay green
# --------------------------------------------------------------------------

def test_example_package_passes_the_gate():
    path = os.path.join(ROOT, "packages", "_EXAMPLE-grounded-package.md")
    reg = preflight.load_registry()
    sections = preflight.parse(path)
    errors = []
    for p in preflight.PLATFORMS:
        preflight.check_platform(p, sections[p], reg, errors, [], [])
    assert errors == [], f"example package regressed: {errors}"


def test_registry_tags_are_internally_consistent():
    """Every per-platform verified tag must not also be banned everywhere."""
    reg = preflight.load_registry()
    banned = {k.lower() for k in reg["banned_everywhere"]}
    for platform, tags in reg["verified_hashtags"].items():
        overlap = {t.lower() for t in tags} & banned
        assert not overlap, f"{platform} lists banned tag(s): {overlap}"
