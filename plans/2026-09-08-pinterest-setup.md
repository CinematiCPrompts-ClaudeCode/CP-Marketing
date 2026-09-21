# Pinterest — setup and 30-day test (08.09.2026)

Business account confirmed (`contact@wolfram-brandhoff.com`), which is the gate for analytics.

**Why this channel and not a sixth one:** Pinterest is a **search surface that links out**. Intent
lives in the query, like the App Store; the App Store link sits on the pin rather than in a bio; and
it reports **outbound clicks**, so for the first time a social channel is measurable on something
that tracks downloads (page views, +0.76) rather than views (+0.19). A pin also keeps surfacing for
months against ~48 hours for a Reel, and `Marketing-Examples/` is already full of unused stills.

---

## 1. The naming mistake to avoid — we just made it on the App Store

The existing board is **"Cinematic Prompts - Prompts for AI image and video"**. That is named for
**what we are**, not for **what people search** — which is precisely the error that produced a
subtitle targeting a 1/5-popularity phrase. Nobody searches Pinterest for "prompts for AI video".
They search for **the look**: `film noir lighting`, `golden hour portrait`, `product photography
setup`, `moody street photography`.

**Board names, board descriptions and pin descriptions are all indexed by Pinterest search.** Put
the searchable phrase in all three. The app is the *credit*, not the headline.

### Boards to create

Keep the existing board as the brand/home board. Add these, each named as a search phrase:

| Board | Source material already on disk |
|---|---|
| `Cinematic Lighting Reference` | the 12 style stills, Prenzlauer Berg / Napoli / Tokyo Noir |
| `Golden Hour Photography` | the golden-light nature set (FB's 2497 and 1096 came from here) |
| `Film Noir & Neo-Noir Stills` | Tokyo Noir, Black & White, 70s Gritty |
| `AI Product Photography` | `Products/` (15), `Lemon-Soda/` (6), `Microlina/` |
| `Fashion Editorial Reference` | `Fashion/`, the red-dress set |
| `Interior & Furniture Styling` | `Segmüller/`, `Furniture/` |
| `Camera Angles & Composition` | the 6 camera-angle stills |

### Pin description shape

```
<searchable phrase describing the LOOK> — <one line on how it was set up>.
Prompt written in Cinematic Prompts. Free on the App Store, no account.
```

**Pinterest is not the other four platforms.** Hashtags are ineffective there; **keywords in the
description are what get indexed**. Do not port the hashtag habit across — write the phrase people
would type, in plain words.

**The claims rules still apply** — pin descriptions are visible copy. No "no wasted credits", no
generator names in visible copy, "Golden Hour" capitalised, the five real lighting names only.

---

## 2. ★ Campaign links — do this before pinning anything

App Store Connect generates **campaign-tagged links** (a `ct=` token on the product URL). Traffic
arriving through one is reported **by campaign in App Analytics** — the same feed `refresh.py`
already reads.

This is the direct answer to the 29.08 caveat, *"attribution is inferred — no install can be traced
to a post"*, which sits under every conclusion this system has drawn about social, **including the
+0.19 correlation itself.**

**Generate one link per channel, not just Pinterest:**

| Channel | `ct=` token |
|---|---|
| Pinterest | `pinterest` |
| Facebook | `facebook` |
| TikTok | `tiktok` |
| YouTube | `youtube` |
| Instagram | `instagram` |

Use App Store Connect's own generator rather than hand-building the URL — the `pt` provider token is
account-specific. Put each link in that channel's bio/description and on every pin.

**Nine weeks of argument about whether social reaches the KPI becomes a number the week after this
is done.**

---

## 3. The test

**Effort ceiling: existing stills only, no bespoke creative.** This channel earns its place at
near-zero cost or not at all — and it must not delay the Facebook replication, which is the live
experiment.

- **20–30 pins over two weeks**, batched, drawn from the folders above
- Every pin links to the App Store via the `ct=pinterest` link
- **Measure outbound clicks. Ignore impressions and saves entirely.**

### Signal — pre-registered

Current baseline: **~2.7 App Store page views/day (~81/month)**.

| 30-day outbound clicks | Verdict |
|---|---|
| **Clears 30** | Keep and scale — that is a ~37% lift to the top of a funnel we cannot otherwise move, and it would justify wiring the API. |
| 10–30 | Inconclusive; run one more month before deciding. |
| **Under 10** | Close it. A search surface that does not produce clicks in 30 days will not produce them in 90. |

With `ct=pinterest` in place we also get the second half for free: **how many of those clicks became
downloads** — which no other channel has ever been able to answer.

---

## 4. API — later, not now

Pinterest API v5 (developers.pinterest.com, OAuth 2.0) exposes impressions, saves, pin clicks and
outbound clicks. Two gates: a **Business account** (✅ done) and **app review for production
access** — new developer apps start limited.

**Do not wire it until the channel clears its signal.** This repo's rule is API where one exists,
paste-in where it does not; a channel should prove itself before it earns pipeline work. Paste the
outbound-click number into the weekly review for the first month.
