# Apple Search Ads probe — paste-ready setup (08.09.2026)

**Why this exists now:** the subtitle indexed (the app IS returned for "AI prompt generator for
video") but ranks at the bottom, and organic search impressions fell 249/day → 68/day after the
03.09 release. Apple exposes **no organic search terms** — Search Ads is the only route to
keyword-level data. This probe answers two questions nothing else can:

1. **Does the phrase the whole ASO change targets have real search volume?**
2. **What do people actually type** — i.e. which long-tail terms could a 12-downloads/week app
   realistically rank for organically?

**It is not a growth test.** €10 buys a handful of taps. Do not read installs from it.

---

## The one thing that makes this cheap

**Apple Search Ads bills per TAP, not per impression.** Impressions cost nothing. So the daily cap
limits taps, not reach — and the search-term data we actually want accumulates for free. Bid low,
run it longer, read the reports.

---

## Setup

Go to **ads.apple.com** → Apple Search Ads **Advanced** (not Basic — Basic gives no keyword-level
data, which defeats the point). Apple renames things periodically; follow the on-screen labels if
they differ from the names below.

### Placement — pick ONE

**Search Results. Deselect Today Tab, Search Tab and Product Pages.**

Search Results is the only keyword-driven placement, and keyword-level impressions plus the
search-terms report are the entire deliverable here. The others are query-less:
- **Search Tab** shows in the suggested list *before the user types*, so there is no query and no
  search-term data — it would spend the budget on taps that teach us nothing about terms.
- **Today Tab** is front-page awareness, no query, and typically the most expensive.
- **Product Pages** ("You Might Also Like" at the bottom of competing apps' pages) is genuinely
  high intent and worth a **second, separate probe later** — but it matches on category and similar
  apps, not keywords, so it answers a different question. Splitting €10 across both leaves neither
  conclusive.

### Bid strategy — **Manage Bids** (manual), not Maximize Conversions

Apple applies the bid strategy to the **whole campaign**, and Maximize Conversions **requires
Search Match** — which would force it on in the `Thesis` ad group and destroy the clean exact-match
test. The two-ad-group design does not survive it.

It is also the wrong objective: the auto-bidder optimises for installs, and €10 produces 1–5 of
them — nothing for it to learn from. And it removes the one diagnostic that matters, the ability
to raise a single keyword's bid to check whether zero impressions means *no volume* or *bid too
low to enter the auction*. Those are opposite conclusions and they look identical from the outside.

Set max CPT per ad group: **€0.70** on `Thesis`, **€0.45** on `Discovery`.

### Campaign
| Field | Value |
|---|---|
| Name | `CP — Keyword Discovery` |
| Countries | **US, GB, DE** |
| Daily cap | **€2** |
| Total intended spend | **~€10** (stop it manually after ~5 days) |

Three storefronts, chosen deliberately: **US** for volume, **DE** because it has our best
conversion by a distance (17% all-time impression→page-view), **GB** because it collapsed hardest
after the release (−87%) and is worth a look.

### Ad group 1 — `Thesis` (Search Match **OFF**)

This tests the terms we chose. Exact match, all four:

| Keyword | What a result tells us |
|---|---|
| `ai prompt generator for video` | The phrase the whole 1.8.4 subtitle was built around |
| `cinematic prompt generator` | Closest to what the app literally is |
| `ai video prompt app` | Long-tail, should be cheap |
| `prompt generator for kling` | Generator-specific; lowest competition of the four |

**Max CPT bid: €0.70.** If a keyword gets zero impressions after two days, raise that one to €1.20
before concluding it has no volume — a bid too low to enter the auction looks identical to a term
nobody searches, and those are opposite conclusions.

### Ad group 2 — `Discovery` (Search Match **ON**, no keywords)

Apple matches the app to queries it thinks are relevant, and the **search-terms report** shows you
what those were. This is the half that produces new information rather than confirming ours.

**Max CPT bid: €0.45.**

### Negative keywords (both ad groups)

Keeps the budget off traffic that will never convert:

```
video editor, photo editor, wallpaper, chatgpt, free movies, video player, screen recorder
```

---

## Before you start — 30 seconds, do not skip

**Write down today's organic numbers**, because paid impressions land in the same App Store search
bucket and the revert trigger depends on separating them:

- Organic search impressions: **53–54/day** (05.09 = 54, 06.09 = 53)
- Organic page views: **~1–2/day**

Search Ads reports its own impressions and taps in its own dashboard, so subtract those.
**The ~120/day revert trigger on 20.09 is measured on ORGANIC impressions only.**

---

## What to read when it finishes

Read it as a keyword test. In order of value:

1. **Search-terms report from `Discovery`** — the actual queries. Anything here that we don't
   already target is a candidate for the next release's keyword field.
2. **Impressions per keyword in `Thesis`** — volume, not taps. This is the answer to question 1.
3. **Tap-through rate per keyword** — if a term gets impressions but under ~2% TTR, the problem is
   the tile (icon, name, subtitle, first screenshot), not the bid.
4. **Installs — ignore.** 3–16 taps is noise against a 12/week baseline.

### Signals, pre-registered so they can't be rationalised later

| Result | Reading |
|---|---|
| `ai prompt generator for video` gets **<50 impressions** across the run, even at €1.20 | The phrase has little real volume. The subtitle is aimed at a term nobody searches — this becomes the strongest argument for the 20.09 revert. |
| It gets impressions but **TTR under 2%** | The phrase is real; our search-result tile loses. That is the cover screenshot and icon, not the metadata. |
| It gets impressions and **TTR above 4%** | The phrase and the tile both work — we are simply out-ranked, and the fix is time plus long-tail keywords, not a revert. |
| `Discovery` surfaces terms we don't target | Straight into the next release's keyword field. `kling` and `seedance` are already suspected gaps — `gemini` and `runway` are in the field, those two are not. |

---

## Notes

- **Keywords and subtitle need a new app version to change.** Anything learned here rides the next
  release. Promotional text is the only listing field editable in place.
- **The ad creative is your live listing** — Search Ads serves the current icon, name, subtitle and
  screenshots. So the TTR reading above is a read on the *current* store assets, not the new cover,
  which does not go up until 21.09.
- **This does not break anything we are still measuring.** The organic CTR window was already
  suspended on 08.09 because of the re-index; there is no clean organic measurement left to
  contaminate.

---

# ✅ AS CREATED — 08.09.2026

The plan above records the reasoning; this is what actually went live. **It diverges from the draft
because Apple's own keyword-popularity tool answered, for free, most of what the probe was going to
buy.**

**The free finding that reshaped it:** popularity scores read straight off the Add Keywords screen —

| Aligned volume + intent | | Volume, wrong intent | | Dead |
|---|---|---|---|---|
| `gemini` **5/5** · `veo` **4/5** · `kling` `seedance` `runway` **3/5** | | `angle` 3/5 · `fashion` 3/5 | | `prompt generator` · `generator` · `prompt` · `image` · `filmmaker` · `marketing` · `ads` — all **1/5** |

**`ai prompt generator for video` is 1/5.** The phrase the whole 1.8.4 subtitle was built around has
minimal search volume, established before spending anything.

**Live campaign:**
| | |
|---|---|
| Placement | Search Results |
| Countries | DE, GB, US |
| Bid strategy | Manage Bids, €0.67 default max CPT |
| Daily budget | €2 · runs 09.09 19:00 → 13.09 21:00 (~€8) |
| Ad group | `Thesis` — Search Match **OFF** |
| Keywords (all **Exact**) | `ai prompt generator for video` (control) · `kling` · `seedance` · `veo` · `gemini` |
| Negative keywords | **none — unnecessary.** Exact match serves only on the precise query; negatives only do work under Broad or Search Match. |
| `Discovery` ad group | **dropped this round.** Its question — "what do people actually type" — was answered free by the popularity tool and Apple's recommendation panel. It would also have starved `Thesis`, since both share the €2 daily cap. |

**Apple's recommendation panel is itself a positioning signal:** it suggested `capcut`, `picsart`,
`inshot` (video editors) and `grok`, `meta ai`, `dola ai` (chatbots). **Apple does not currently
classify us as a prompt tool** — it sees an editor or a chatbot. Worth remembering when the next
release's category and keyword choices come up.

## Reading the first 24 hours (check 10.09)

The three outcomes are diagnostic and they mean different things:

| What you see | Reading |
|---|---|
| Generator keywords get impressions, **control gets zero** | The expected result and the strongest possible case for the next release: the volume is in generator names and the 1.8.4 phrase is empty. Rewrite the keyword field. |
| **Every keyword gets zero**, including `gemini` at 5/5 | Not a volume problem — either the bid is under the auction floor (raise to €1.20–1.50 and re-check) or **Apple is not treating the app as relevant to generator names at all**, which is a much bigger finding and a category/positioning problem, not a keyword one. |
| Impressions but **TTR under ~2%** | The terms are right and the search-result tile loses. That is the icon and first screenshot — the cover shipping 21.09 is the fix, and it should be re-tested after. |

Installs remain irrelevant at this budget. Do not read them.
