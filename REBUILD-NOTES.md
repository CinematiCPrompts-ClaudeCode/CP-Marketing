# Rebuild notes — 2026-08-03

An external review of why the agent was "bumbling, making errors, and not learning."
**Verdict: the brain is good; the plumbing was broken.** No ground-up rewrite — targeted
fixes to data integrity, the memory model, and file sprawl. Details also logged in `PROTOKOLL.md`.

## What was wrong, and what changed

### 1. It was analyzing fabricated data (why you had to check everything)
`scripts/refresh.py` prepended **9 fake backdated Facebook posts** to the real data on every
run — invented view counts, one literally named "Noir alley, one prompt." Every FB average and
recommendation was partly fiction.
→ **Fixed:** fabrication block removed from `refresh.py`; the 9 fake rows also scrubbed from the
current `dashboard/data.js`. FB is now real-data-only.

### 2. It wasn't learning (the memory model was split three ways)
- `CLAUDE.md` said long-term memory was `data/performance-log.csv` — but that file was **stale
  (ended June)** and held lighting names the brand docs call invalid. The real journal is the `.md`.
- `PROTOKOLL.md` — where the actual lessons live — was **written to but never read**: it appeared
  in no "read before you write" instruction.
- The agent kept narrating "saved to memory: `feedback-workflow-reality.md`" etc. — **those files
  never existed**, so every such lesson evaporated.
→ **Fixed:** created **`LESSONS.md`**, one durable-rules ledger (seeded from `PROTOKOLL.md`), as the
  single append target. `CLAUDE.md` now reads `LESSONS.md → PROTOKOLL.md → data.js → packages/` in
  order and defines exactly three memory locations (nothing else counts). Old CSV frozen as
  `data/performance-log.legacy-thru-2026-06.csv`.

### 3. It kept overclaiming the product (the most-repeated correction)
"No wasted credits," "one prompt" for a multi-scene video, "more presets," "one perfect shot," Sora,
"harsh noon," lowercase "golden hour" — each caught only after it shipped.
→ **Fixed:** created **`brand/claims.md`**, an allowed/banned claims allowlist, wired as a hard
  pre-publish gate in the marketing skill.

### 4. File sprawl (made everything ambiguous)
Three refresh scripts (one garbled `roriginal-efresh.py`), duplicate `index.html`, duplicate
`content-package.md`, all with docstrings that lied about what they did.
→ **Fixed:** `scripts/refresh.py` is the one canonical script (docstring corrected); stale forks and
  stray root duplicates deleted; Stop hook now points at all three memory files.

## Two things left for you (judgment calls, not auto-changed)

1. **Rotate your API keys.** `.env`, both `AuthKey_*.p8`, and the TikTok token were correctly
   git-ignored, but they were included in the zip you uploaded, so they've left your machine.
   Regenerate: App Store Connect keys, the YouTube/Meta keys in `.env`, and re-run
   `scripts/tiktok_auth.py`. (These files were removed from the returned copy.)
2. **Pick one content-package template.** `templates/content-package.md` and the skill's
   `references/content-package-template.md` are two *different* output shapes. Decide which you want,
   make the other match or delete it, and make sure `CLAUDE.md` + the skill point at the same one.

## To fully apply
Re-run `./run.sh` (or `python scripts/refresh.py`) once, so the dashboard regenerates cleanly from
the fixed script.
