# Marketing System Protokoll

Running log of changes, fixes, and decisions. Newest first.

---

## 2026-08-20 — Repo groundwork + two real bugs found
- `git init` + first commit (75 files). Wrote `README.md` for an outside reader. Hardened
  `.gitignore` — it would otherwise have committed the live TikTok OAuth refresh token and
  `dashboard/.deploy.env` (contains an SFTP password).
- Added `tests/test_preflight.py` (34 tests). Writing them immediately exposed a **dead
  guardrail**: `#aiproductphotography`'s commerce-fit check scanned the hashtag line, and the tag
  contains "product", so it always passed itself. Fixed.
- Diagnosed the Aug 20 data loss: TikTok + YouTube were wiped to 0 rows. Cause was a broken
  playlist entry (~position 36-40) making any page spanning it 404, plus an expired TikTok token —
  and the all-sources-empty guard didn't fire because Meta succeeded. `refresh.py` now preserves
  per-source history, pages at 35, keeps partial results, and backfills from `videos.csv`.
  YouTube recovered 35 of 47 videos. **TikTok still needs `scripts/tiktok_auth.py` re-run.**
- Created `data/performance-log.md` (referenced everywhere, never actually existed). First entry
  grades the Facebook reach experiment: 3 and 1 views → sub-30 → **stop rewriting FB captions,
  audit the account.**
- Open: the otter package went out on IG/FB but **not** TikTok or YouTube; FB duplicated again
  (3rd time). Whether the posted reel used a corrected re-render is unverified.

## 2026-08-13 — Fresh start (memory wiped, machine kept)
- Archived the accumulated lessons / log / packages / grades to `archive/2026-08-13/`. Kept all plumbing, the dashboard, the API connections, `brand/registry.json` (the code-enforced gate rules), CLAUDE.md, and the package template.
- Reason: the system was built by incremental learn-and-tweak, and the memory had accumulated corrections-on-corrections that were themselves causing the repeated mistakes. Early runs performed well from a clean base — resetting to one.
- Next: re-analyse `dashboard/data.js` from scratch and rebuild `LESSONS.md` → *What wins* from the real numbers. See `first-run.md`.
