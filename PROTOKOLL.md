# Marketing System Protokoll

Running log of changes, fixes, and decisions. Newest first.

---

## 2026-08-22 — Refresh hung on a stalled socket; timeout added

- **`./run.sh` hung, it didn't fail.** The traceback was a `KeyboardInterrupt` mid-SSL-read:
  `refresh.py` set **no timeout on any request**, so urllib blocked forever on a stalled TLS
  read. Ctrl+C was the only way out, and that loses the whole pull.
- **Fixed:** `socket.setdefaulttimeout(45)` covers every `urlopen` in the file (override via
  `REFRESH_TIMEOUT` in `.env`). A timeout now raises like any other error, so the per-source
  staleness guard keeps last-known-good rows instead of wiping them. Two tests pin it — **52
  passing**.
- **The API itself was fine** — a direct call answered in 0.4s. The re-run completed (exit 0)
  but took **13m20s at 1% CPU**: almost entirely network wait, not a hang. The App Store part
  only re-fetches ~16 days (416 cached), so the bulk is **Meta's per-post insight calls** —
  49 IG + 44 FB posts, several metrics each, all sequential. If that slowness recurs, the fix
  is caching post insights the way App Store daily reports already are; older posts' counts
  barely move, so re-querying all 93 every run is mostly waste. Not done yet — it was a slow
  network, not a code regression.
- **Numbers after the pull:** YouTube **49** (up from 45 — the playlist reached further this
  run), Instagram 49, Facebook 44, TikTok **42**, downloads **359** (355 → 359). Nothing stale.
- Note on this log: the pre-2026-08-13 history lives in `archive/2026-08-13/PROTOKOLL.md`
  (continuous June → 2026-08-10, 29 dated entries). The live file restarted on 08-13 **by
  design** — the old ledger had accumulated corrections-on-corrections that were themselves
  causing repeat mistakes. It is not missing; it is archived.

## 2026-08-21 — All four sources live; framing win confirmed; next package built

**The week's result: the framing change worked.** The sea-otter package hit **805 on TikTok**
(Aug 17) — 3.1× the August average of 262. Both predictions HIT (TikTok "clear 500", Instagram
"flat 10-25" → 11). The controlled comparison is clean: two nature posts five days apart, same
channel, differing only in caption frame — wildlife-as-subject 230 vs product-pain **805**.
Promoted from experiment to a default rule in LESSONS.

**But the KPI didn't move, and that's the finding that matters.** The 805-view week produced
**19 downloads — the lowest of the last four weeks** (25 / 21 / 29 / 19). Views tripled, installs
fell. Getting views on TikTok is now solved; converting them is not. Next package therefore
tests the CTA, not the hook.

**All four sources live for the first time.** A long credential fight, most of it self-inflicted:
- Meta died twice — first a password change (code 190/460), then an expired short-lived token
  (190/463). Added `scripts/meta_token.py` + a CREDENTIALS section; **use the PAGE token**, it
  doesn't expire. `refresh.py` only understood user tokens, so following that advice broke it
  (`/me/accounts` doesn't exist on a Page) — now handles both.
- **TikTok was broken by my own commit.** Moving credentials out of the source into `.env`
  silently switched apps: `.env` held `sbawa5c7mkdgoxox43` (the Lovable upload app), not the
  working `sbaw38iz0q3h0sm8ga`. Six rounds of console reconfiguration chased the wrong app. The
  user's "this worked before the deploy" was right; I twice concluded otherwise. Restored.
- YouTube recovered 35→45 videos via the uploads-playlist fallback.

**Bugs found and fixed:** a dead guardrail (`#aiproductphotography`'s commerce check scanned the
hashtag line, and the tag contains "product", so it always passed itself); the partial-failure
data wipe; the YouTube playlist truncation hiding the *recent* tail; `refresh.py` discarding
publish timestamps, which made all posting-time advice unevidenced.

**Repo work:** `git init` → https://github.com/MisterWolf1965/Marketing-Agent (private).
50 tests (34 preflight + 16 refresh). `.gitignore` hardened — it would have committed a live
TikTok OAuth token and an SFTP password. `data/performance-log.md` created and running: 2 HIT
predictions, 2 KILL verdicts. Brand assets + design system stored in `brand/assets/`.

**Shipped:** `packages/2026-08-21-diverse-set-change.md` (gate CLEAR) — 28s variety reel, film +
commerce. Facebook deliberately unwritten; its stop rule fired at 7 and 2. Cover + credits-led
end card designed to the real CI, inside social safe zones.

**Open for next session:**
1. **Was the otter reel re-rendered?** The banned "NO WASTED CREDITS" end card and invented
   "MIDDAY" label were flagged pre-post and never confirmed fixed. If not, a banned claim is live.
2. **Facebook audit** — Meta Business Suite reach settings / Page restrictions. Not a copy problem.
   Also: the same post has now double-fired three times (Jul 10, Jul 27, Aug 18/19).
3. **YouTube visibility discipline** — Private shipped 3×; Aug 12 = 1 view, Aug 20 = 5 views.
   A 20-40× effect, far bigger than posting hour.
4. The ~15s Instagram cut of the 28s reel (IG's band is 7-15s; it sits at 11 views).
5. Grade the CTA experiment: downloads clear 30 → keep privacy in the CTA; under 22 → move the
   test to the App Store page.

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
