#!/usr/bin/env python3
"""
preflight.py — the ship gate for a content package.

A package does not ship unless it can SHOW ITS WORK. For every platform it must
either name the proven pattern it's copying WITH the real view count (Grounding:),
or explicitly flag the choice as an Experiment: with a stop signal. On top of that
it enforces the deterministic rules that are always true (banned/forbidden tags,
generator names in visible copy, engagement bait, tag counts, claim landmines).

Usage:
    python3 scripts/preflight.py packages/2026-08-12-foo.md
    python3 scripts/preflight.py            # checks the newest file in packages/

Exit code 0 = clean (ship it).  Exit code 1 = at least one hard failure (do not ship).
Rules live in brand/registry.json — edit that, not this script, when a rule changes.
"""

import json, re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG_PATH = os.path.join(ROOT, "brand", "registry.json")

PLATFORMS = ["tiktok", "instagram", "youtube", "facebook"]
PLATFORM_ALIASES = {
    "tiktok": "tiktok", "instagram": "instagram", "instagram reels": "instagram",
    "reels": "instagram", "youtube": "youtube", "youtube shorts": "youtube",
    "shorts": "youtube", "facebook": "facebook",
}

C = {"red": "\033[31m", "grn": "\033[32m", "yel": "\033[33m", "dim": "\033[2m",
     "bold": "\033[1m", "off": "\033[0m"}
def col(s, c): return f"{C[c]}{s}{C['off']}" if sys.stdout.isatty() else s

def load_registry():
    with open(REG_PATH, encoding="utf-8") as f:
        return json.load(f)

def pick_package(argv):
    if len(argv) > 1:
        return argv[1]
    pkgs = sorted(glob.glob(os.path.join(ROOT, "packages", "*.md")), key=os.path.getmtime)
    if not pkgs:
        print("No package given and packages/ is empty."); sys.exit(2)
    return pkgs[-1]

def heading_platform(line):
    """If a markdown heading names a platform, return the canonical platform key."""
    if not line.lstrip().startswith("#"):
        return None
    text = line.lstrip("#").strip().lower()
    for alias, canon in PLATFORM_ALIASES.items():
        if re.search(r"\b" + re.escape(alias) + r"\b", text):
            return canon
    return None

def parse(path):
    """Attribute each line to the platform whose heading most recently opened.
    A non-platform heading or a '---' rule closes the current attribution."""
    sections = {p: [] for p in PLATFORMS}
    current = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            st = line.lstrip()
            if st == "---":
                current = None; continue
            if re.match(r"#{1,6}(\s|$)", st):      # real ATX heading: # + space (NOT a #hashtag line)
                current = heading_platform(line)   # None if it's a non-platform heading
                continue
            if current:
                sections[current].append(line)
    return sections

def tags_in(lines):
    """Return the post's actual hashtags — only from a *pure hashtag line*.
    Tags quoted inside prose or backticks (e.g. a note about a tag that was dropped)
    are references, not the post's tags, and are ignored."""
    out = []
    for ln in lines:
        s = re.sub(r"`[^`]*`", " ", ln)                 # drop inline-code spans
        s = re.sub(r"\*+", "", s).strip()               # drop markdown emphasis
        s = re.sub(r"^(hashtags?|tags)\s*:\s*", "", s, flags=re.I)  # drop a leading label
        if s and re.fullmatch(r"#\w+(?:\s+#\w+)*", s):  # the whole line is only hashtags
            out += re.findall(r"#\w+", s)
    return out

def is_pure_hashtag_line(ln):
    """True if the whole line is nothing but hashtags."""
    s = re.sub(r"`[^`]*`", " ", ln)
    s = re.sub(r"\*+", "", s).strip()
    s = re.sub(r"^(hashtags?|tags)\s*:\s*", "", s, flags=re.I)
    return bool(s and re.fullmatch(r"#\w+(?:\s+#\w+)*", s))

def prose_text(lines):
    """Caption prose only — `caption_text` minus the pure-hashtag lines.

    Used for context-fit checks. A tag must never be able to justify its own
    presence: `#aiproductphotography` literally contains the fit keyword
    "product", so scanning the hashtag line made that rule unfirable.
    """
    return "\n".join(ln for ln in caption_text(lines).split("\n")
                     if not is_pure_hashtag_line(ln))

def caption_text(lines):
    """Visible copy only — drop backend/keyword lines and pure metadata lines."""
    keep = []
    for ln in lines:
        low = ln.lower()
        if any(k in low for k in ("backend tag", "app store keyword", "keyword field", "backend:")):
            continue
        keep.append(ln)
    return "\n".join(keep)

def has_grounding(lines):
    ground = exp = False
    ground_num = False
    for ln in lines:
        m = re.match(r"\s*\**\s*(grounding|copying|proven)\s*:", ln, re.I)
        if m:
            ground = True
            if re.search(r"\d", ln):
                ground_num = True
        if re.match(r"\s*\**\s*(experiment|testing)\s*:", ln, re.I):
            exp = True
    return ground, ground_num, exp

def check_platform(p, lines, reg, errors, warns, notes):
    if not lines:
        return  # platform not present in this package — nothing to check
    tags = tags_in(lines)
    low_tags = [t.lower() for t in tags]
    cap = caption_text(lines)
    low_cap = cap.lower()
    low_prose = prose_text(lines).lower()   # excludes hashtag lines — see prose_text()

    # --- grounding: show your work, or it doesn't ship ---
    ground, ground_num, exp = has_grounding(lines)
    if not ground and not exp:
        errors.append(f"[{p}] no grounding — add a 'Grounding: <pattern>, <real number>' line "
                      f"(name the proven post you're copying) or 'Experiment: <what/stop-signal>'.")
    elif ground and not ground_num:
        errors.append(f"[{p}] grounding names no number — cite the real view count of the post "
                      f"you're copying (e.g. 'Grounding: triple-negation open, 858').")
    else:
        notes.append(f"[{p}] grounded ({'experiment' if exp and not ground else 'copying a proven pattern'}).")

    # --- hashtags ---
    if p in reg["hashtag_count"] and tags:
        lo, hi = reg["hashtag_count"][p]
        if not (lo <= len(tags) <= hi):
            errors.append(f"[{p}] {len(tags)} hashtags — should be {lo}–{hi} for {p}.")
    banned = {k.lower(): v for k, v in reg["banned_everywhere"].items()}
    forbid = {k.lower(): v for k, v in reg.get("forbidden_per_platform", {}).get(p, {}).items()}
    verified = set(t.lower() for t in reg["verified_hashtags"].get(p, []))
    ctx = {k.lower(): v for k, v in reg.get("context_sensitive", {}).items()}

    for t in tags:
        tl = t.lower()
        if tl in banned:
            errors.append(f"[{p}] {t} is banned everywhere — {banned[tl]}.")
        elif tl in forbid:
            errors.append(f"[{p}] {t} is forbidden on {p} — {forbid[tl]}.")
        elif tl in verified:
            if tl in ctx:
                fits = any(k in low_prose for k in ctx[tl]["fit_keywords"])
                if not fits:
                    errors.append(f"[{p}] {t} — {ctx[tl]['reason']}. This post's copy shows no "
                                  f"product/fashion/commerce angle; justify the fit or drop it.")
        else:
            errors.append(f"[{p}] {t} is unverified on {p} — verify it on-platform and add it to "
                          f"brand/registry.json, or remove it. (real ≠ relevant ≠ verified-here.)")

    # --- visible copy landmines ---
    for g in reg["generator_names"]:
        if re.search(r"\b" + re.escape(g) + r"\b", low_cap):
            errors.append(f"[{p}] generator name \"{g}\" in visible copy — move it to a "
                          f"'Backend tags:' line / App Store keywords only.")
    for bait in reg["engagement_bait"]:
        if bait in low_cap:
            errors.append(f"[{p}] engagement bait \"{bait}\" — CTA should point at the install.")
    for phrase, why in reg["banned_phrases"].items():
        if phrase in low_cap:
            errors.append(f"[{p}] claim landmine \"{phrase}\" — {why}.")

    # --- youtube visibility reminder ---
    if p == "youtube":
        if re.search(r"\bprivate\b", low_cap):
            errors.append(f"[{p}] copy mentions 'Private' — YouTube has shipped Private twice; set Public.")
        else:
            warns.append(f"[{p}] can't see the real visibility toggle — confirm the upload is Public.")

def main():
    reg = load_registry()
    path = pick_package(sys.argv)
    sections = parse(path)

    print(col(f"\nPreflight — {os.path.relpath(path, ROOT)}", "bold"))
    present = [p for p in PLATFORMS if sections[p]]
    print(col(f"platforms found: {', '.join(present) if present else '(none — check headings)'}\n", "dim"))

    errors, warns, notes = [], [], []
    for p in PLATFORMS:
        check_platform(p, sections[p], reg, errors, warns, notes)

    for n in notes:
        print(col("  ✓ ", "grn") + n)
    for w in warns:
        print(col("  ⚠ ", "yel") + w)
    for e in errors:
        print(col("  ✗ ", "red") + e)

    print()
    if errors:
        print(col(f"BLOCKED — {len(errors)} issue(s) to fix before this ships.", "red"))
        if warns:
            print(col(f"(+{len(warns)} reminder(s) above.)", "yel"))
        sys.exit(1)
    else:
        msg = "CLEAR — every platform shows its work. OK to ship."
        print(col(msg, "grn"))
        if warns:
            print(col(f"(Still confirm {len(warns)} reminder(s) above.)", "yel"))
        sys.exit(0)

if __name__ == "__main__":
    main()
