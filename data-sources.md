# Data Sources — where every number comes from

Rule of thumb: **official API if one exists, paste-in if it doesn't, scraping only
as a last resort.** This file tells the agent (and you) the real source of each
metric so nothing is invented.

| Metric | Source | How | Status |
|---|---|---|---|
| **App Store downloads** | App Store Connect API | `scripts/fetch_appstore.py` (Sales report) | ✅ API |
| App Store impressions / page views / taps | App Store Connect API | Analytics Reports API — `scripts/enable_analytics.py`, read by `refresh.py` | ✅ **READING 04.09.2026** |
| **YouTube views / likes / comments** | YouTube Data API v3 | `scripts/fetch_youtube.py` | ✅ API |
| **TikTok views** | TikTok Display API (if authorized) | `scripts/tiktok_auth.py` once, then `refresh.py`; falls back to the `tiktok` column in `data/videos.csv` | ⚠️ API-or-manual |
| Instagram views | `instagram` column in `data/videos.csv` is source of truth; Meta API as fallback | read off Reel insights → `videos.csv` | ✍️ manual (CSV wins) |
| Facebook views | `facebook` column in `data/videos.csv` is source of truth; Meta API as fallback | read off post insights → `videos.csv` | ✍️ manual (CSV wins) |
| **Pinterest** impressions / saves / **outbound clicks** | Pinterest API v5 (business account + approved app) | not wired — **paste-in first**, see below | ⏳ evaluating |
| Engagement / saves / shares | manual, weekly | per-platform analytics → `data/performance-log.md` | ✍️ manual |
| Follower growth | manual, weekly | per-platform analytics → `data/performance-log.md` | ✍️ manual |
| ROAS / CPI / CAC / CPM / CPC / LTV | (none yet) | starts when you run paid ads | 🔒 not active |

> **Integrity note (03.08.2026 rebuild):** `refresh.py` no longer fabricates any
> data. A block of fake backdated Facebook posts used to be injected on every run,
> inflating FB averages — it has been removed. If a platform's history is thin, the
> dashboard shows it thin. Never reintroduce placeholder numbers.

## API status
- **App Store + YouTube** — fully wired, official, free.
- **TikTok** — Display API works once you run `scripts/tiktok_auth.py` (saves a refresh token); otherwise paste the number into `data/videos.csv`.
- **Instagram / Facebook** — the Meta Graph API can't reliably return Reel/organic play counts, so the `videos.csv` columns are the **source of truth** and override any API value. Paste them in weekly.
- Weekly qualitative grades + predictions go in `data/performance-log.md` (via the `marketing-weekly-review` skill), **not** the frozen legacy CSV.

## The two that are wired now
- **App Store downloads** — your hero metric. App Store Connect API, official, free.
- **YouTube views** — official, free, 10,000 quota units/day (plenty).

See `CREDENTIALS.md` for exactly where to get the keys.

## Analytics Reports — enabled 02.09.2026

There is **no toggle in the App Store Connect web UI**; the feed is request-driven. Created once
via `python3 scripts/enable_analytics.py --create --snapshot` and now running:

| Request | accessType | ID |
|---|---|---|
| Ongoing daily feed | `ONGOING` | `d2fcc92e-c855-4827-bce2-140dcf5ea674` |
| Historical backfill (~1y) | `ONE_TIME_SNAPSHOT` | `56dfb2b7-94bd-4ae3-944a-4e8266471c24` |

App: `Cinematic Prompts` / `com.mrwolfcineprompts.app` / id `6757644087`.

Read path: `/v1/analyticsReportRequests/{id}/reports` → `/instances` → `/segments` (gzipped CSV).
The two report categories that matter: **APP_STORE_ENGAGEMENT** (impressions, product page views)
and **APP_STORE_COMMERCE** (downloads, conversion rate).

**Column trap that cost two days (04.09.2026).** The `App Store Discovery and Engagement Standard`
report has an **`Event`** column (`Impression` / `Page view` / `Tap`) *and* a separate
**`Engagement Type`** column (`Get` / `Open` / `Share` / `Update`, blank on impression rows). The
metric is `Event`. Matching `Engagement Type` silently drops every impression and turns every
product-page tap into a page view. Also: `Standard` and `Detailed` are the same events at different
dimensional depth, the ONGOING and ONE_TIME_SNAPSHOT requests overlap in dates, and
`Web Preview Engagement` is a browser surface with no impression denominator — read **one** report
name and merge per date with **max**, never sum. One snapshot instance carries the full history
(230 days in a single segment), so the daily instance count is not the history length.

**Gotchas already hit:** `accessType` is the only writable attribute — sending `name` returns
409 `ENTITY_ERROR.ATTRIBUTE.UNKNOWN`. And Apple stops an ONGOING request that goes unread for
too long (`stoppedDueToInactivity`), so the read has to actually run, not just be configured.
Re-running `enable_analytics.py` with no flags reports current state without creating anything.

## Pinterest — added 08.09.2026

**Why it is being tried when four channels already exist:** Pinterest is the only one that is
**search-driven AND links out**. Both properties address problems the other four cannot:
- **Search-driven** means intent lives in the query, like the App Store itself. Our documented
  failure mode is high-volume, low-intent impressions (August: impressions 116→249/day while CTR
  fell 4.9%→2.42%). A feed cannot fix that; a search surface can.
- **Links out** means a pin can point straight at the App Store listing. TikTok and Instagram bury
  the link in a bio; Pinterest puts it on the pin.
- **Outbound clicks are reported**, so for the first time a social channel can be measured on
  something that actually tracks downloads (+0.76 for page views) rather than views (+0.19).
- **Long half-life.** A pin keeps surfacing for months; a Reel is dead in 48 hours. The stills in
  `Marketing-Examples/` are already made and currently unused.

### Is there an API? Yes — Pinterest API v5, with two real gates

- **developers.pinterest.com**, OAuth 2.0, REST. Analytics endpoints cover pin, board and account
  level: **impressions, saves, pin clicks, outbound clicks** — outbound clicks being the one we care
  about.
- **Gate 1: the account must be a Business account.** Personal accounts get no analytics. Converting
  is free and reversible.
- **Gate 2: the app needs review for production access.** New developer apps start with limited/
  trial access; full analytics scopes require submitting the app for approval. Timelines vary and
  Pinterest changes the process periodically — check the current state in the portal rather than
  trusting this note.

**Do not wire it yet.** This repo's own rule is official API where one exists, paste-in where it does
not, and the channel has to prove itself before it earns pipeline work. Paste the numbers into the
weekly review for the first month; wire `refresh.py` and add a fifth `data.js` array only if it
clears its signal.

## ★ The bigger find: App Store Campaign Links solve attribution for EVERY channel

Looking up Pinterest link handling surfaced something that has been missing since the campaign
began. **App Store Connect can generate campaign-tagged links** (a `ct=` provider/campaign token
appended to the product URL). Traffic arriving through a tagged link is then reported **by campaign
in App Analytics** — the same feed `refresh.py` already reads.

This is the direct answer to the 29.08 finding's own caveat: *"attribution is inferred — no install
can be traced to a post."* With a tagged link per channel, it no longer has to be inferred.

**It is not Pinterest-specific.** Tag one link per channel — `ct=pinterest`, `ct=facebook`,
`ct=tiktok`, `ct=youtube`, `ct=instagram` — put each in that channel's bio/description, and the
question that has been open for nine weeks becomes directly measurable. **Do this before the next
round of content, not after.**
