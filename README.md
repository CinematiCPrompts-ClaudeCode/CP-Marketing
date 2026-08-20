# Cinematic Prompts — Marketing Agent

An LLM agent that runs the marketing for a real, shipped iOS app
([Cinematic Prompts](https://apps.apple.com/app/id6757644087)) — it pulls live performance data
from four platforms, decides what to post next, writes the platform-specific copy, and is
mechanically blocked from shipping content that breaks the rules it has already learned.

It is not a demo. It runs against production APIs and real numbers, and the content it produces
gets posted.

---

## Why this project is interesting

Most agent projects fail quietly: the model sounds confident, produces plausible output, and
nobody notices it was wrong. This repo is mostly a set of answers to that problem.

**1. Rules live in code, not in the prompt.**
Telling the model "don't overclaim" in `CLAUDE.md` did not work — the same mistakes shipped
repeatedly. So the rules moved into a deterministic gate:

```bash
./check.sh packages/2026-08-13-coastal-five-lights.md   # exit 0 = ship, exit 1 = blocked
```

`scripts/preflight.py` reads the finished content package and blocks it on banned claims,
hashtags unverified for that platform, generator names in visible copy, engagement bait, wrong
tag counts, and more. The rules themselves are data (`brand/registry.json`), not code, so
changing a rule doesn't mean editing the checker.

**2. Every claim must cite a real number.**
The gate's most important rule: each platform block must open with either

```
Grounding: pain-first lighting hook, 820 ("Stop regenerating just to fix your lighting")
Experiment: <lever being tested>. Signal: <clears X → keep / sub-Y → drop>
```

No receipt, no ship. Either you're copying a pattern that demonstrably worked *with the view
count to prove it*, or you're explicitly flagging a guess and pre-committing to a stop rule.
This is the anti-hallucination mechanism: the agent cannot assert that something works without
pointing at data on disk.

**3. Memory is explicit and bounded.**
Three files, and only three: `LESSONS.md` (durable rules), `PROTOKOLL.md` (dated log),
`data/performance-log.md` (weekly grades + predictions). The agent is forbidden from inventing
new "memory" files — an earlier version narrated saving lessons to files that never existed, so
every lesson evaporated.

**4. The system is designed to be wrong in public.**
`data/performance-log.md` requires quoting the previous week's prediction *verbatim* before
grading it HIT / MISS / PARTIAL. Experiments carry stop rules that must be honoured even when
the result is disappointing.

---

## Architecture

```
CLAUDE.md                  agent instructions / operating rules
.claude/skills/            three skills (content, weekly review, storyboard) + bundled refs
.claude/settings.local.json  Stop hook → forces the end-of-session memory write

scripts/refresh.py         one canonical data pull: YouTube, Meta, App Store, TikTok
scripts/preflight.py       the ship gate (deterministic, exit-code)
brand/registry.json        the gate's rules as data
brand/claims.md            allowed vs. banned product claims

dashboard/data.js          the live numbers the agent reads
tests/test_preflight.py    34 tests pinning every gate rule to a failing example
```

**Data sources** — YouTube Data API v3, Meta Graph API, App Store Connect (JWT-signed, ES256),
TikTok Display API (OAuth refresh-token flow). Where an API can't return trustworthy numbers
(Instagram/Facebook organic play counts), a manual CSV column is the declared source of truth
and overrides the API. `data-sources.md` records the provenance of every metric.

## Running it

```bash
./run.sh                                  # refresh all data → dashboard/data.js
./check.sh packages/<file>.md             # gate a content package
python3 -m pytest tests/ -q               # run the test suite
```

Credentials go in `.env` (see `.env.example` and `CREDENTIALS.md`). Nothing secret is committed.

---

## Things that went wrong, and what changed

These are the interesting parts, kept deliberately.

**The agent was analysing fabricated data.** `refresh.py` prepended nine fake backdated Facebook
posts on every run — invented view counts, one literally titled "Noir alley, one prompt." Every
Facebook average and recommendation was partly fiction. Removed, and the integrity note in
`data-sources.md` now forbids reintroducing placeholder rows.

**A transient API error silently destroyed history.** A 404 on YouTube plus an expired TikTok
token wrote empty arrays over 47 and 40 posts of history, while Meta succeeded — so the existing
"refuse to overwrite" guard never fired, because it only triggered when *every* source failed.
`refresh.py` now preserves the last known good rows per source and marks them stale rather than
letting a blip erase the record.

**The root cause was worse than it looked.** The 404 wasn't the playlist being missing — the
playlist contains a broken entry around position 36-40, and any page spanning it returns a bogus
"playlist cannot be found." Pagination at the API's documented maximum of 50 always hit it, and
the handler discarded the items already collected. Now it pages at 35, keeps partial results, and
backfills from the CSV record.

**A test found a guardrail that could never fire.** `#aiproductphotography` is only allowed on
product/commerce content, checked by scanning the caption for keywords like "product". But the
scan included the hashtag line — and the tag itself contains the substring "product", so it
always justified its own presence. Written as a test, failed immediately, fixed by excluding
hashtag lines from the context check. The rule had been dead since it was written.

**The gate cannot see pixels.** A finished reel shipped for review with the single most-banned
claim ("NO WASTED CREDITS") and an invented lighting name ("MIDDAY") burned into the video
frames. Both would have been blocked instantly as text; both sailed through a gate that only
reads markdown. Caught by extracting frames and reading them as copy — now a documented
pre-approval step in `LESSONS.md`.

---

## Honest limitations

- **The conversion chain is unmeasured.** The stated KPI is `views → App Store taps → installs`,
  but App Store Connect's Analytics Reports API isn't wired up yet, so taps and conversion rate
  are currently invisible. Download totals are real; attribution to a specific post is not.
- **Sample sizes are small.** Most per-platform monthly figures are n=3-13. The project's own
  honesty rules require saying "consistent with" rather than "proves", and naming n.
- **Facebook is broken and not yet diagnosed.** Average views/post fell 512 → 319 → 157 → ~6
  across four months. No caption change explains that; it needs an account-level investigation.
- **TikTok ingestion requires periodic manual re-auth** when the refresh token expires.
- Posting is deliberately manual. The agent writes and gates content; a human publishes it.
