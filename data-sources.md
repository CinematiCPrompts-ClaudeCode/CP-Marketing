# Data Sources — where every number comes from

Rule of thumb: **official API if one exists, paste-in if it doesn't, scraping only
as a last resort.** This file tells the agent (and you) the real source of each
metric so nothing is invented.

| Metric | Source | How | Status |
|---|---|---|---|
| **App Store downloads** | App Store Connect API | `scripts/fetch_appstore.py` (Sales report) | ✅ API |
| App Store impressions / page views / conversion | App Store Connect API | Analytics Reports API (richer, async) | ⏳ optional upgrade |
| **YouTube views / likes / comments** | YouTube Data API v3 | `scripts/fetch_youtube.py` | ✅ API |
| **TikTok views** | TikTok Display API (if authorized) | `scripts/tiktok_auth.py` once, then `refresh.py`; falls back to the `tiktok` column in `data/videos.csv` | ⚠️ API-or-manual |
| Instagram views | `instagram` column in `data/videos.csv` is source of truth; Meta API as fallback | read off Reel insights → `videos.csv` | ✍️ manual (CSV wins) |
| Facebook views | `facebook` column in `data/videos.csv` is source of truth; Meta API as fallback | read off post insights → `videos.csv` | ✍️ manual (CSV wins) |
| Engagement / saves / shares | manual, weekly | per-platform analytics → `data/performance-log.md` | ✍️ manual |
| Follower growth | manual, weekly | per-platform analytics → `data/performance-log.md` | ✍️ manual |
| ROAS / CPI / CAC / CPM / CPC / LTV | (none yet) | starts when you run paid ads | 🔒 not active |

> **Integrity note (2026-08-03 rebuild):** `refresh.py` no longer fabricates any
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
