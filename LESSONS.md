# LESSONS — what we already know (fresh start 13.08.2026)

Clean slate. The prior ledger was useful but had tangled into corrections-on-corrections,
which was itself causing repeated mistakes. It's archived under `archive/2026-08-13/`. This file
is rebuilt from the raw numbers, not inherited.

**Read before producing anything.** Fill the three sections below from your own analysis of
`dashboard/data.js`. One line per entry — narrative belongs in `PROTOKOLL.md`; fixed rules and
verified hashtags live in `brand/registry.json` (the gate reads that).

---

## ★ What wins — rebuild this from data.js (only patterns you can attach a real number to)

**★★★ 21.09.2026 — THE FACEBOOK DUPLICATE-POST BUG REGRESSED, AFTER 16 CLEAN DAYS. Root cause is
still unknown, and that's the actual gap now.** Duplicate posting had stopped 03.09 (see below).
The 19.09 Vespa post went out **twice the same day** (265 + 282 views) — the 5th documented
occurrence (Jul 10, Jul 27, Aug 18/19, then a clean stretch, now this) — and landed on **Sunday**,
a day after the package's scheduled Saturday 09:00. **This repo does not auto-post** (CLAUDE.md,
"posting stays manual, no dlvr.it / auto-distribution"), so the mechanism is either the user's own
posting flow double-submitting, or a Meta-side artifact (Business Suite / cross-post double-firing)
— and after 5 occurrences across two months, **the question that actually needs answering is HOW
the post reaches Facebook**, not "it happened again." Log the answer here the next time this comes
up, because four prior log entries diagnosed the *effect* (downranking risk, second-copy losing
every time) without ever pinning the *mechanism*.
- **Consequence for reading this weekend's Facebook number:** 265/282 can't be graded as a third
  data point on the plain-declarative-caption formula (555, 343) — the post also shipped a day
  late, so both content execution AND timing deviated from plan. Inconclusive, not a miss.
_Filled 13.08.2026 from a full re-read of `dashboard/data.js` after `./run.sh`. TikTok token
was connected same day — re-pulled, 40 posts now real; TikTok section updated below._

**★★★ 07.09.2026 — FACEBOOK IS NOT SUPPRESSED. 537 VIEWS ON THE MAIN ACCOUNT, AGAINST AN AUGUST
MEDIAN OF 4.5.** A user-written post on 05.09 (*The Crossing*) returned **537** — **119× the August
median**, best since 27.07, above July's median of 164.5. **Account confirmed by the user as the
MAIN one**, which closes both alternative explanations: not a new-account cold-start boost, and not
a throttled account (a throttled account cannot do 537). **The "Facebook looks suppressed" reading
is retired.** The August collapse was recoverable, and the most likely mechanism is the
duplicate-posting penalty decaying — every August FB post was half of a duplicate pair, and
duplicate posting stopped 03.09.
· **Same asset, all four platforms, same week — content held constant by construction:
  FB 537 · TikTok 243 · Instagram 3 · YouTube 2.**
· **Four confounded candidates, none promoted to a rule at n=1:** the caption shape (long,
  plain-declarative, an explicit *mechanism* sentence — "the angle changes shot to shot, and the
  light turns over at the border" — and a friction-removal close, "Free on the App Store, no
  account"); duplicates having stopped; content type (narrative single-scene vs August's
  feature-lists and variety reels); early-Saturday timing.
· **It did not reach the KPI.** 05.09 produced **1 product page view and 2 downloads**.
· **★ The planning failure is the durable lesson.** Facebook had been parked as "structurally
  collapsed — needs diagnosis, not content," so the 03.09 package was deliberately Instagram-only.
  The win came from the user posting anyway. **Never park a channel on an unfinished diagnosis —
  keep posting to it while you diagnose, or the diagnosis never gets tested.**

**★★ 07.09.2026 — INSTAGRAM'S PROBLEM IS DEFINITIVELY NOT CONTENT. Stop writing IG experiments.**
Same film, same week: **Facebook 537, Instagram 3 — a 179× gap on identical footage.** No caption,
hook, hashtag or format decision produces that. Third independent signal in the same direction
(13.07, three failed interventions; 29.08, grounding on IG's own best post returned 7; now this).
**The next Instagram test is account-level — reach settings, posting method, Page-vs-profile — or
there is no next Instagram test.** Spend that effort on Facebook.

**★★ 07.09.2026 — THE MULTI-SUBJECT GALLERY IS FACEBOOK'S WORST FORMAT, AND IT FAILED WHILE THE
ACCOUNT WAS HEALTHY.** This matters because it is the format most often proposed for showing range.
From May–July, *before* the collapse, so the account is not the excuse:

| Gallery / feature-list posts | Views | | One subject, many settings | Views |
|---|---|---|---|---|
| 08.07 "One idea, **12 cinematic styles — swipe to…**" | **0** | | 27.05 "AI did it anyway" (golden light, ruins) | **2497** |
| 22.07 "Campaign shots without the campaign budget" | 13 | | 21.06 "AI Nature Documentary — West Coast Ocean" | **1096** |
| 20.06 "Without a Cinematic Prompt vs With One" | 32 | | 30.05 "They built an empire…" | 699 |
| 06.06 "Stop wasting credits! Generate cinematic…" | 41 | | **01.07 "One Day of the Dead street, re-lit across…"** | **339** |

**The rule: ONE SUBJECT ACROSS MANY SETTINGS beats MANY SUBJECTS ACROSS ONE APP.** The 01.07 post
is the proof case — it shows range without becoming a catalogue — and the 05.09 winner (537) is the
same shape. A tour of twelve different products reads as a catalogue; **the same product in twelve
setups reads as a capability.** Hardest on Facebook, and consistent with TikTok's bands
(single-subject 784–859 vs variety 255–303).

**★★★ 08.09.2026 — APP STORE CAMPAIGN LINKS END THE ATTRIBUTION PROBLEM. Do this before the next
round of content.** Found while checking whether Pinterest pins could link to the listing. **App
Store Connect generates campaign-tagged links** (a `ct=` token on the product URL), and traffic
arriving through one is reported **by campaign in App Analytics** — the same feed `refresh.py`
already reads.

This is the direct answer to the 29.08 finding's own stated caveat: *"attribution is inferred — no
install can be traced to a post."* It has been the acknowledged hole in every conclusion this system
has drawn about social ever since, including the +0.19 correlation itself.
**Tag one link per channel** — `ct=pinterest`, `ct=facebook`, `ct=tiktok`, `ct=youtube`,
`ct=instagram` — put each in that channel's bio or description, and "does social reach the KPI"
stops being an inference from weekly totals and becomes a number. **Nine weeks of argument could
have been a measurement.**

**★★ 08.09.2026 — PINTEREST IS THE ONLY SOCIAL CHANNEL THAT MATCHES WHAT THE FUNNEL ACTUALLY NEEDS.**
Not because it is a fifth audience, but because it has two properties none of the other four do:
· **It is a search surface, not a feed.** Intent is in the query, like the App Store. Our documented
  failure mode is high-volume, low-intent impressions — a feed cannot fix that.
· **Pins link out.** The App Store link sits on the pin, not buried in a bio.
· **It reports OUTBOUND CLICKS** — so for the first time a social channel is measurable on something
  that tracks downloads (page views, +0.76) rather than views (+0.19). **Measure Pinterest on
  outbound clicks and ignore impressions and saves entirely.**
· **A pin has a half-life of months**, against ~48 hours for a Reel, and the stills in
  `Marketing-Examples/` are already made.
**Caveat that keeps it honest:** it is a fifth channel while Instagram is unresolved and Facebook's
537 is unreplicated. It only earns its place at near-zero creative cost — existing stills, no
bespoke work — and it must not delay the Facebook replication, which is the live experiment.

**★★★ 14.09.2026 — THE €10 AD SETTLED THREE THINGS. THE TILE IS THE WHOLE PROBLEM.**
Five days, DE/GB/US, Search Results, exact + broad, €10 spent:

| Keyword | Impressions | Taps | TTR | Installs | CR |
|---|---|---|---|---|---|
| `veo` | 471 | 5 | 1.06% | 1 | 20% |
| `kling` | 386 | 8 | 2.07% | 1 | 12.5% |
| `gemini` | 65 | 1 | 1.54% | 0 | 0% |
| `seedance` | 48 | 1 | 2.08% | 1 | 100% |
| **`[ai prompt generator for video]`** | **1** | 1 | — | 1 | 100% |
| **TOTAL** | **971** | **16** | **1.65%** | **4** | **25%** |

**1 — The subtitle targets a phrase that does not exist.** The exact-match control drew **ONE
impression in five days across three storefronts** at €0.67. Pre-registered signal #1 was "under 50
→ the phrase has no real volume". One. **The 1.8.4 subtitle is aimed at nothing**, and the next
metadata release should stop defending it. Apple's 1/5 popularity score called this before a cent
was spent.

**2 — Generator names are where the volume is: 970 of 971 impressions.** `veo` and `kling` alone
carried 857. Confirms the popularity data and settles the keyword-field question.

**3 — ★★★ THE TILE CONVERTS AT 1.65% AND THAT IS THE ENTIRE PROBLEM.** Tap→install is **25%**,
which is strong — once someone reaches the page they install. But impression→tap is 1.65%.
**The arithmetic, on the same 971 impressions and the same 25% CR:**
| TTR | Installs | CPI |
|---|---|---|
| 1.65% (actual) | 4 | €2.50 |
| 3% | 7 | €1.37 |
| **4%** | **10** | **€1.03** |
| 5% | 12 | €0.82 |
**The user expected 10 installs for €10. At a normal 4% tap-through that is exactly what €10 buys.**
The gap is not the bid, the keywords, the budget or the targeting — **it is the search-result tile**:
icon, name, subtitle, first screenshot.

**★ And the same tile serves ORGANIC search.** Paid and organic draw the identical creative, so the
1.65–2% ceiling applies to every organic impression too. That is the same shape the funnel has shown
all year — weak impression→page-view, strong page-view→install — now confirmed on traffic we
controlled. **Moving to organic does not escape this; it just stops paying to observe it.**
**The cover screenshot has been built since 06.09 and is still not uploaded (5 of 10 slots).** It is
the cheapest available move against the one number that gates everything else.

**★★★ 08.09.2026 — THE SUBTITLE INDEXED. IT JUST CANNOT RANK. Indexing and ranking are different
tests and we only ever planned the first one.** Searching the App Store for **"AI prompt generator
for video"** now returns the app — **it did not before**, because the old subtitle carried neither
*generator* nor *video*. The plan called this "a clean pass/fail on the whole ASO change": it is a
**PASS**. But the app sits **at the bottom of the results**, and a bottom-ranked result earns
almost no impressions, which is most of the 249→68/day collapse.

**The mistake underneath: we picked the phrase for RELEVANCE and never asked whether we could WIN
it.** App Store rank for a term is driven heavily by download velocity *on that term*. At **~12
downloads a week** the app cannot outrank established apps on a head phrase, no matter how well the
subtitle matches it. **Relevance gets you indexed; volume gets you ranked.** For an app this size
the keyword field has to target **long-tail phrases where 12/week is enough to rank** — generator
names (`kling`, `veo`, `seedance` — allowed in keyword fields, and someone searching "kling prompt"
is exactly our user), not head terms like *ai video generator*. Note `gemini` and `runway` are
already in the field; `kling` and `seedance` are not.

**★ And the revert decision has a hole in it: we never knew what the OLD subtitle ranked for
either.** Apple's App Analytics exposes *no* organic search terms — only Search Ads does, and only
for paid. So "revert to Create cinematic AI prompts" is a blind swap between two unmeasured
keyword sets; all we know is that the old one coincided with 249 impressions/day. **Watch rank, not
just impression count**, and remember 1.8.4 also moved categories, so a subtitle revert would not
undo the whole change. **If anything is reverted, revert one field at a time.**
**Keywords and subtitle need a new version to change; promotional text does not.** Any keyword fix
therefore rides the next release — plan it, do not expect it this week.

**★★★ 08.09.2026 — 1.8.4 CANNOT BE JUDGED YET, AND IMPRESSIONS HAVE COLLAPSED 73% SINCE RELEASE.
The download slowdown has TWO causes and only one of them is the release.**

**Search impressions, time-locked to the 03.09 release:** 02.09 → 162 · **03.09 → 176 (release)** ·
04.09 → 114 · 05.09 → 54 · 06.09 → 53. Pre-release baseline **249/day**, now **68/day**.
**Verified real, not partial data** (each ONGOING instance carries a rolling 3-day window and the
values never move after publication).

**It is a re-index, not a targeting improvement and not a penalty.** The evidence rules out the
optimistic reading: the drop is **uniform across every territory** (US −65%, GB −87%, IN −65%,
DE −63%, CN −97%, CA −93%) and **entirely in search** (248/day → 67/day; browse was ~1/day and is
unchanged). A quality-of-targeting improvement would have dropped the low-CTR territories and held
DE/IN. A uniform search-only collapse right after a subtitle + keyword + category change is what
losing your old rankings looks like while the new ones are still being earned.

**The three-phase story behind the download decline — it started BEFORE 1.8.4:**
| | imp/day | CTR | page views/day | install rate | downloads |
|---|---|---|---|---|---|
| July | 116 | **4.9%** | 5.7 | **61%** | 108 |
| August | **249** | **2.42%** | 6.6 | **45%** | 92 |
| Post-release (3d) | **68** | 3.9% (n=8, noise) | **2.7** | — | ~12/wk |
Weekly downloads: 25 → 20 → **14** → **12**. **August bought volume and lost quality** — more
impressions from weaker queries, so CTR *and* the install rate fell together. Then the release
removed the volume as well. **Page views are now down 55% against the pre-release baseline, and
page views are the thing that tracks downloads at +0.76.**

**Consequences for the measurement plan:**
· **Do not read the CTR test on 20.09.** A CTR measured mid-re-index is not the subtitle's
  steady-state effect. **Restart the 14-day clock when impressions plateau** (3 consecutive days
  within ±25% of each other), and grade from there.
· **Revert trigger:** if impressions are still under **~120/day** by 20.09, the metadata change has
  cost more volume than any CTR gain can repay, and reverting the subtitle goes on the table.
  68/day × 3.9% = 2.7 page views/day against 249 × 2.42% = 6.0. **A better tile on a listing nobody
  is shown is worth less than a worse tile on one that is.**
· **A metadata change is not free.** Nothing in the 1.8.4 plan priced in a re-index dip. Budget one
  on every future listing change, and never change subtitle, keywords and categories in the same
  release again — this one cannot be attributed to any single field.

**★★★ 04.09.2026 — THE APP STORE FUNNEL IS FINALLY READABLE, AND THE BOTTLENECK IS THE SEARCH
RESULT, NOT THE PRODUCT PAGE.** First real numbers, 16.01.2026 → 02.09.2026 (230 days):

| Step | Number | Rate |
|---|---|---|
| Impressions (16,422 search + 1,559 browse) | 17,981 | — |
| Product page views | 836 | **4.65% of impressions** |
| Downloads | 384 | **45.9% of page views** |

**95% of the loss happens before anyone reaches the product page.** The page converts between 40%
and 67% in *every single month* — it is not the problem and does not need work. What needs work is
the tile in the search results: **app name, subtitle, icon, first screenshots, app preview**, because
that is the only thing 17,981 people actually saw.
· **Size of the prize:** at August's volume (7,326 impressions/month), **each +1 percentage point of
  CTR ≈ +73 page views ≈ +33 downloads a month.** Nine weeks of caption work moved downloads by
  nothing measurable.
· **The app preview video now has a price tag.** It autoplays muted in *search results* — at the
  impression step, the exact step losing 95%. It has sat on the open-items list as "0 of 3, not
  blocking" since 08-30. It is the highest-leverage unshipped asset in this system.
· **★ Daily page views correlate with daily downloads at +0.76** (n=230), against **+0.19** for
  social views. **Page views/day is the metric to steer on** — it moves earlier than downloads and
  carries 2–3× the sample size.
· **Impressions are not the problem and are growing on their own:** 116/day (Jul) → 236/day (Aug).
  Reach is arriving and the tile is wasting it — downloads per 1,000 impressions fell 30.2 → 12.6
  across that same doubling.
· **Check the territory mix before reading any CTR change.** AU 0.3%, CA 0.9%, JP 0.9%, IT 0.8%
  against IN 4.9% and DE 17.0%. August's aggregate CTR fall (4.9% → 2.8%) is partly just more
  impressions landing where nobody taps. Grade CTR on a fixed top-5 territory set, and split by
  Source Type: **browse impressions convert at 1.86%, search at 4.64%**, so 1.8.4's category move
  (Grafik und Design + Foto und Video) can move aggregate CTR on its own.

**YouTube** — top 5: The Ride 1054, Now Pick Your Camera Angle — New in 1.8 1033, The System
Failure 877, New Cinematic Style: Nature - Coming soon! 599, Cinematic Prompts App - Prompt
Generator 489. Pattern: two things beat the generic "app description" titles (worst: Cinematic
Video and Image Prompt Generator App, 17) — (1) narrative shorts with a punchy one/two-word title
("The Ride," "The System Failure"), and (2) direct feature-announcement titles naming a specific
new capability ("Now Pick Your Camera Angle," "New Cinematic Style: Nature — Coming soon"). Vague
descriptive titles lose regardless of production quality.

**Facebook** — top 5: "AI did it anyway" (golden light / ancient ruins nature-doc) 2496,
Nature style "Coming soon" announcement 1554, AI Nature Documentary — West Coast Ocean 1096,
"They built an empire. I rebuilt it in a…" 662, Revenge (narrative short) 611. Pattern: nature-doc
+ golden-hour content is the single strongest FB lever — the top 3 posts are all nature/golden-light
themed, more than double anything else on the platform. Long, plain-declarative captions
outperform crafted TikTok-style hooks here (confirms the template's "plain statement, not a
crafted hook" instruction).

**Instagram** — top 5: "Ocean and coastal AI footage is the hard[est]…" 717, "This is what AI
video looks like without…" 301, "Stop rewriting prompts to fix the lighting" 272, "Stop
struggling with boring AI video pro…" 148, "Need a 70s gritty cinematic style? Choos…" 131.
Pattern: the top 3 are ALL pain-first, direct-statement hooks (wasted effort / before-vs-after /
lighting frustration) — none are narrative-title reposts. Compare same-footage reposts under
narrative titles ("The Ride" repost 30, "Revenge" repost 30, "Car Chase" repost 29): direct
pain-hook captions beat narrative-title captions on IG by ~10-24x on the same or similar source
footage. IG rewards stating the problem in the first line, not naming a story.

**TikTok — restored 13.08.2026, 40 posts, avg 588 views/post (highest average of any platform).**
Top 5: "Amateur to Hollywood in 1 click" (transformation) 1987, The Crime (narrative) 1868,
The Conspiracy (narrative) 1030, The Car Chase (narrative) 930, "No studio. No photographer.
No shoot." (triple-negation pain) 859. This confirms the `brand/registry.json` proven_winners
that were sitting unverified while the array was empty (1986/1867/858 — real, off by rounding).
Pattern: TikTok is the one platform where narrative "The X" story titles cluster at the top
(Crime, Conspiracy, Car Chase, Escape, Ride — all 780-1868) — the *same* footage reposted under
those titles gets ~29-30 views on Instagram. TikTok rewards the story title IG punishes.
Pain-first hooks also work here ("Stop regenerating just to fix your lighting" 820, "Stop
letting AI pick your camera angle" 784) — pain-first is the one hook shape proven on all three
of TikTok/Instagram/Facebook simultaneously, narrative titles are TikTok/YouTube-only.

**★★ YouTube publish hour — I GAVE A BAD TIME. The hour buckets hid the opposite signal
(corrected 15.09.2026, user caught it).** The 08-21 entry reported medians by *four-hour bucket* and
concluded "15–19 → 192 (n=12), default slot ~16:30 CEST". **Broken out by actual hour, across all 44
videos that have both a timestamp and a view count:**

| CEST | n | median | | CEST | n | median |
|---|---|---|---|---|---|---|
| 09:00 | 3 | 63 | | 18:00 | 6 | 211 |
| 10:00 | 2 | 354 | | 19:00 | 9 | 28 |
| 11:00 | 2 | 72 | | 20:00 | 6 | 90 |
| 13:00 | 3 | 23 | | **21:00** | 2 | **644** |
| 14:00 | 2 | 136 | | 22:00 | 1 | 132 |
| 15:00 | 5 | 173 | | | | |
| **16:00** | 3 | **11** | | | | |

**16:00 is the WORST hour in the entire dataset — median 11.** The "15–19" bucket averaged 18:00
(n=6, median 211) together with 16:00 (n=3, median 11) and produced a recommendation that points at
the worse of the two. **A bucket average can recommend the exact hour the data argues against.**

**What the data actually supports: nothing.** n runs 1–9 per hour, content confounds every cell, and
the two "best" hours (21:00 median 644, 10:00 median 354) are n=2 each. **Stop giving a posting hour
as if it were evidence-based.** If an hour must be named, say it is a guess and say why.

**And the industry advice does not transfer.** "Best time to post a Short" articles are
population-level, drawn from channels big enough that the first-hour push drives distribution. On a
channel this size, a Short is discovered through the Shorts feed and search over days, not in the
first hour. **The user's 11:00 Short clearing 100 is consistent with their own 11:00 median of 72 —
a normal-to-good result, not evidence that 11:00 is special.** The thing that needs explaining is
not the 100; it is the 13.09 upload that got 11.

**★ The real YouTube killer is visibility at publish, not the hour.** Aug 12 = 1 view (confirmed
set Private), Aug 20 = 5 views, against a recent baseline of 25–218. A video that isn't Public
during its launch window never gets the initial push, and flipping it Public later does not
recover it. This is a 20–40× effect; posting hour is at best a 2–5× one. **Confirm Public in
Studio immediately after upload — before anything else.**

**Operating mode from 29.08.2026 — maintenance, not withdrawal.** Presence stays on all four
platforms; what stops is four bespoke copy sets a week. **One asset, four posts, ~1 hour:**
TikTok gets fresh grounded copy (it is the only channel with real view volume, 255–805); the
other three reuse it mechanically. Evidence that reuse costs nothing: Instagram's 08-27 post was
grounded on its own best-ever post (35) and returned **7** — better writing did not transfer.
Post one platform per day so each upload's visibility toggle and duplicate-check get checked
individually; both recurring operational failures (YouTube Private 3×, Facebook double-fire 4×)
happen when four go out in one sitting. Full plan: `plans/2026-08-29-maintenance-cadence.md`.

**★★★ 02.09.2026 — THE FACEBOOK ACCOUNT LOOKS SUPPRESSED, NOT UNDERPERFORMING. Check account
health before writing another caption.** User posted the same content from a second, accidental
account under their own name. Same platform, same person, same footage:

| | Median views |
|---|---|
| Main FB account, August (n=9) | **4** |
| Second account, same content | **~229** (29, 34, 218, 224, 234, 245, 278, 307) |
| Main FB account, **July** (n=12) | 164.5 |

**~57× apart on the same platform, and the new account lands right where the main account sat in
July.** Content is held constant by construction, so content cannot be the explanation. The main
account fell off a cliff between July (median 164.5) and August (median 4.0) — a **41× collapse**
that no caption change can produce.

**The most likely mechanism is ours.** `data.js` shows **7 duplicate uploads of the same asset
since July 1** on Facebook, and in every single pair the second upload underperforms the first
(240→89, 327→256, 19→5, 330→257, 7→4, 12→4, 3→1). Repeated duplicate posting is a documented
Meta downranking trigger, and the "Facebook double-fire" was logged four times as an *operational*
bug — it was never treated as a *distribution* risk. The 08-29 "one asset, four posts" maintenance
mode makes mechanical cross-posting of identical content the default, which is the other known
trigger. **Both need to stop until account health is confirmed.**

**✅ TEST 1 RESULT (03.09.2026): NO FORMAL PENALTY. Account Quality is clean on BOTH accounts.**
Meta *Aktuelle Kontoprobleme*, 05.08–03.09.2026, Wolfram Brandhoff + MisterWolf both selected:
**"Keine Konto- oder Assetprobleme."** So the strong version of this finding — a formal
restriction or non-recommendable flag — is **ruled out**, and appealing an enforcement action is
not the fix. Downgraded from "looks suppressed" to "unexplained collapse with no penalty behind
it."

**What the clean result does NOT rule out, and why the header above still stands:**
- **Account Quality only reports FORMAL enforcement.** Soft algorithmic downranking — the kind
  duplicate posting actually causes — is never surfaced to the user. A clean page is consistent
  with reduced reach.
- **The window misses the event.** It covers 05.08–03.09; the collapse is July (164.5) → August
  (4.0). A violation in late July that has since cleared would not appear. **Check the "Geklärt"
  tab and widen the date range past 05.08 before treating this as settled.**

**★ The confounder that now matters more than suppression: PAGE vs PERSONAL PROFILE.** Facebook
gives personal-profile reels substantially more organic reach than Page reels. If the second
account is a profile and the main one is a Page, that difference alone can produce a large gap
with no penalty anywhere. **Establish which type each account is before running any further
comparison** — it is a one-minute check that could explain the whole thing.

**Test 2, still outstanding — new accounts get a cold-start boost**, so a fresh account beating an
old one is expected for ~2–3 weeks. Post the same asset to both on the same day and compare. If
the second account is still winning past its first three weeks, *and* both are the same account
type, then it is reach suppression rather than novelty.

**Regardless of the outcome: stop the duplicate uploads.** Seven since July 1, second copy losing
every time. That is free to fix, it is a known soft-ranking factor, and nothing above depends on
it being the cause.

**⚠️ This partially confounds the 08-29 "views don't predict downloads" finding below.** If the
8.5× view swing was account health rather than content quality, then that analysis never tested
content — it tested a dying account against a stable App Store baseline. The finding still stands
as *"caption work did not move downloads"*, but the reason may be that the content was never
being distributed, not that content doesn't matter. Do not retire caption work on its authority
until the account question is settled.

**★★ 29.08.2026 — SOCIAL VIEWS DO NOT PREDICT DOWNLOADS. Read this before optimising a caption.**
Nine weeks tested: views swung **8.5×** (282 → 2,385), downloads swung **1.7×** (18 → 30),
**correlation +0.19**. The best-viewed week (2,385) produced the **fewest** downloads of the nine
(18). Downloads sit in an 18–30/week band regardless of content performance — the shape of
baseline App Store discovery, not social referral.
**Consequence:** hook/framing/timing work has no measurable effect on the KPI. Before spending a
round on captions, ask whether the lever is the App Store listing instead. As of 29.08.2026 the
listing still does not contain "generator" or "video" in title or subtitle, so it cannot surface
for "AI prompt generator for video" — that fix was written 08-13 and is still unshipped.
**Caveat:** n=9 weeks, and attribution is inferred — App Store Connect's Analytics Reports API
(impressions, product page views, conversion) is not wired up, so no install can be traced to a
post. Wiring it is the highest-value measurement work available.

**★ REVISED 23.08.2026 — content TYPE sets the band; framing only moves you within it.**
_Supersedes the 21.08.2026 claim that product-pain framing alone was worth 3.5×. That was
promoted to a rule on n=1 and the very next post contradicted it. Kept visible as a worked
example of over-generalising from one clean pair._
· Aug 17 product-pain + **single-subject** (coastal otter) → **805**
· Aug 22 product-pain + **variety reel** (7 looks) → **255**
Same frame, same platform, five days apart, **3.2× apart** — so framing cannot be the driver.
Predicted "clear 600, kill under 350"; it came in at 255 and the kill rule fired.

**The bands, as they now stand on TikTok:**
| Content type | Views |
|---|---|
| Single-subject demo + pain hook | 784–859 (784, 805, 821, 859) |
| Variety / showcase reels | 255–303 (255, 266, 303) — one outlier at 768 |
| Narrative "The X" shorts | 780–1868 (older, Feb–Mar) |
| Feature-count captions | 297–485 |

**Practical rule:** choose the *subject* first — a single scene demonstrating one capability
beats a tour of many, on TikTok, by roughly 3×. Pain framing is still worth using, but it does
not rescue variety content. The 805 is better explained by the coastal otter subject (the same
subject behind Instagram's best-ever 717) than by its caption.

**August 2026 — what the "animal reel flopped" post-mortem actually showed (added 14.08.2026).**
Monthly averages: TikTok 634.6 (Jul) → 262.0 (Aug, n=3); Facebook 512.2 (May) → 318.6 → 157.2 →
**6.8** (Aug, n=5); Instagram 13.0 (Jul) → 21.5 (Aug, n=4, i.e. normal-for-IG, not a crash);
YouTube 170.7 → 120.3 (Aug, n=3, within its usual bounce).
- **Framing, not cadence, is what moved TikTok.** I initially suspected post spacing and the
  bucket averages looked supportive (4–7-day gaps median 679 vs 1–3-day median ~300) — but the
  post-by-post July/August list kills it: gap 2 days → 830 views, gap 6 days → 297, and Aug 7
  had the *longest* recent gap (7 days) and still got 266. **Spacing is not the driver; don't
  reschedule to fix a framing problem.**
- **What actually separates TikTok winners from losers is product-pain/promise vs.
  showcase/feature-list framing.** Winners: "Stop regenerating just to fix your lighting" 821,
  "Stop letting AI pick your camera angle" 784, "No studio. No photographer. No shoot." 859,
  "A luxury Vespa ad" 782, "So many looks. One app." 768. Losers: "12 Cinematic Styles 5
  Lighting Styles 6 Camera Angles" 297, "Generate AI Prompts with the Cinematic Prompts App"
  291, "Cinema-grade and marketing-grade AI prompts" 266. Feature lists and generic app
  descriptions lose on TikTok regardless of spacing.
- **Wildlife-as-showcase underperforms on TikTok** (hunter narrative 279, "No safari" 230) even
  though nature *crushes* on Facebook (2496, 1096). The May/June nature posts that DID win on
  TikTok (817, 807) were framed as **new-style announcements** ("New AI prompt style! Nature
  Documentary"), not as wildlife footage. Nature is FB-native; on TikTok it needs a product frame.
- **Triple-negation only works when it negates a cost the viewer actually pays.** "No studio.
  No photographer. No shoot." = 859 (real production costs a creator faces). "No safari. No
  plane tickets. No wildlife crew." = 230 TikTok / 7 IG (negates a holiday nobody was buying —
  no pain relieved). Copying the surface form without the underlying pain does not transfer.
- **Facebook's collapse is structural, not caption quality.** Four consecutive months of
  monotonic decline ending at ~3–7 views/post. No caption rewrite explains 512 → 6.8. Treat FB
  as needing a *diagnosis* (reach/account-level check in Meta Business Suite), not better copy.
  Also note the same post went out twice on both 12.08.2026 and 08-13 — check for duplicate posting.

## ★ App Store release process — dates that determine when experiments actually start

**17.09.2026 — "uploaded to Connect" is not "live." Measurement clocks start on public release.**
The 15.09.2026 gallery replacement (3 CI-built screenshots, old step slides deleted) was uploaded
to App Store Connect that day, attached to the pending **1.8.7** submission — but App Store
screenshots/previews attached to a version don't go live until that version **clears App Review**.
The App Store kept showing the video + the old slides to every real visitor until 1.8.7 actually
released on **17.09.2026**. The pre-registered 2-week tile-fix read (`plans/2026-09-14-tile-fix.md`)
had assumed 2 days of live data that were never served — **the window had to be reset to the actual
release date.** Rule going forward: **when logging "shipped X" for any screenshot/preview/metadata
change, record the App Review release date as the experiment start, not the Connect upload date** —
and don't start a measurement clock from a PROTOKOLL entry's date without checking which one it was.

## ★ Repo & credentials — how this repo actually pushes

**21.09.2026 — This repo lives at `CinematiCPrompts-ClaudeCode/CP-Marketing` and pushes with the
repo's own PAT, not with SSH and not as MisterWolf1965.** Three failure modes were hit in order,
so check them in this order next time:
- **HTTPS with the default credential authenticates as `MisterWolf1965`**, who has no write access
  to the `CinematiCPrompts-ClaudeCode` org → `403`. A **403 means the repo exists** (404 would mean
  it doesn't) — useful for telling "no access" apart from "wrong name."
- **The SSH route looks configured but is not.** `~/.ssh/cp_cc_claudecode` + the `github-cpcc` host
  alias (created 10.09.2026) are a valid, unencrypted, correctly-wired keypair, but the public key
  was never added to the GitHub account, so it fails `Permission denied (publickey)`. Don't spend
  time debugging the local SSH config — the gap is server-side. Public key is in
  `~/.ssh/cp_cc_claudecode.pub` (`SHA256:f6n7mlIie2fI4pOsE1UyXmqok0eX+vRWHyr2aUj7Epo`) if this is
  ever worth finishing.
- **What works: the PAT at git's interactive prompt, run from the user's own terminal.** Never ask
  for a token in chat — it lands in the transcript and has to be rotated. Use
  `git -c credential.helper= push -u cp-marketing main` so the keychain doesn't silently re-supply
  MisterWolf1965's credential, with username `CinematiCPrompts-ClaudeCode`. A fine-grained PAT
  needs *Contents: read/write* **and** org approval, or it 403s identically to the wrong-account case.
- **`origin` still points at `MisterWolf1965/Marketing-Agent`** and is deliberately left alone —
  `cp-marketing` is the live remote. Verify any push server-side with `git ls-remote cp-marketing`,
  not just by trusting the local tracking ref.
- **The keychain's cached credential for the org account is read-only: `ls-remote` succeeds, push is
  refused with 403.** So a successful read proves nothing about write access, and **the agent cannot
  push this repo at all** — commit freely, but the push itself is always a command for the user to
  run in their terminal. Don't report work as pushed without an `ls-remote` SHA match.

## ★ Pre-flight checklist — the gate enforces the fixed rules (`./check.sh` → `brand/registry.json`)
_Add only judgment-level reminders here as you learn them; the deterministic checks already run in code._

- **★ 17.09.2026 — `object-fit:cover` is not safe by default on a tall narrow tile; check by
  rendering, every time.** Second tile-building session in a row where it silently produced a bad
  crop: a 768×1376 photo into a 1284×1560 (phone) or 1140×2752 (iPad) box left a face small and
  high with dead space below crowding the footer, or cut a full figure off at the ankles. The fix
  both times was a manual pixel crop (explicit width/height/top/left on the `<img>`, computed from
  a chosen source y-window, not `object-position` percentages guessed and eyeballed). Rule: after
  placing any photo in a tile whose aspect ratio differs meaningfully from the source, **render it
  and crop-inspect the photo box in isolation** (`ffmpeg -vf crop=...`) before calling the layout
  done — don't trust `object-fit:cover` to have picked a sane crop just because it filled the box.

- **★ DON'T NAME YOURSELF AFTER A COMPETITOR'S FREE BUTTON (decided 07.09.2026).** Proposed:
  put **"Enhance your prompt"** on the App Store cover, because Runway and Seedance both ship an
  *Enhance* option that improves a prompt, and the phrase is already on our splash screen.
  **Rejected for the cover, kept as a keyword.** Three reasons, in order of weight:
  · **Their Enhance is a free button inside the generator the user already pays for.** Adopting
    their word frames us as a paid substitute for something bundled — it invites the single
    comparison we cannot win. Borrow a competitor's vocabulary only when we do that thing *better*,
    never when they give it away.
  · **It describes the commodity half of the product.** Enhance = expand my text. Our edge is
    *choosing* the style, the lighting and the camera angle — art direction by selection. Naming
    the expansion step buries the dials.
  · **It is not a feature.** Verified in the source 07.09.2026: "enhance" appears nowhere in the UI
    or the iOS assets, only as an adjective inside generated prompt text. It lives on the splash
    graphic alone, so on a store page it names nothing the user can tap.
  **Where it belongs: the backend App Store keyword field.** If Runway/Seedance users think in
  "enhance prompt", that is real search demand at zero positioning cost — and keyword lines are the
  one place generator-adjacent terms are allowed. Splash screen can keep it; post-install the
  comparison risk is gone.
- **★ WE CANNOT A/B TEST THE LISTING YET — THE FUNNEL IS TOO SMALL (measured 07.09.2026).**
  Apple's **Product Page Optimization** is the right mechanism for a screenshot-copy question (up
  to 3 treatments against the live page, real traffic split, conversion reported with confidence).
  It is unusable at current volume. At the observed 46% page-view→install rate and August's 6.6
  page views/day split across two arms:
  · detecting a **10-point** swing needs ~400 page views per arm ≈ **4 months**
  · detecting a **5-point** swing ≈ **16 months**
  **So listing-copy decisions get made on reasoning, and revisited when the funnel is ~10× bigger.**
  This is a second, independent argument for fixing the impression→page-view step first: a bigger
  funnel is what makes every future test possible at all.
- **★ DIAGNOSE BEFORE YOU REWRITE — the hook is usually not the problem (07.09.2026).** Generic
  "your hook isn't performing, generate 5 variations" advice assumes the caption is the cause. In
  this account it has been the cause **almost never**. Every large effect measured so far was
  structural:
  | Symptom | Actual cause | Size |
  |---|---|---|
  | Instagram at 3–15 views | account-level, not content (537 vs 3 on identical footage) | **179×** |
  | Facebook at 4/post in August | duplicate posting; recovered to 537 once it stopped | **119×** |
  | YouTube posts at 1–5 views | video was Private during its launch window | **20–40×** |
  | Downloads flat across 9 weeks | the App Store listing, not the captions | caption effect ≈ 0 |
  Best caption work moves a post within its content-type band (roughly 3×). **Structural faults are
  10–180×.** So when a post underperforms, check — in this order — was it public, was it a
  duplicate, is the account healthy, is the content type right — **and only then look at the copy.**
  Rewriting first is how nine weeks got spent on the one variable that could not reach the KPI.
- **★ THE GATE WOULD HAVE BLOCKED OUR BEST FACEBOOK POST — and that is not a bug (07.09.2026).**
  The 537-view caption ended `#aivideo #aifilmmaking #aicinema #cinematicprompts`, and
  `#cinematicprompts` is **explicitly forbidden on Facebook** in `brand/registry.json`
  ("near-zero on Facebook — TikTok/IG only"). It still did 537. **The correct reading is that a
  dead tag does not sink a good post, not that the rule is wrong** — a tag with no audience adds
  nothing and costs nothing, which is exactly what "near-zero" predicts. Hashtags were already
  logged as a minor signal that never drives reach.
  **The general point: `check.sh` tests COMPLIANCE, not PERFORMANCE.** A BLOCKED verdict is not a
  prediction that a post will fail, and a CLEAR verdict is not a prediction that it will work.
  Do not start relaxing rules because a non-compliant post did well.
  **For the Facebook replication:** drop `#cinematicprompts` and use the FB-verified
  `#aiproductphotography` in its place — it fits the product/marketing context rule — giving
  `#aivideo #aifilmmaking #aicinema #aiproductphotography` (4 tags, inside FB's 3–5 range).
  **Record that this is one deliberate deviation from the winning post**, so a failed replication
  has a known changed variable.
- **★ "SOCIAL VIEWS DON'T PREDICT DOWNLOADS" DOES NOT MEAN "SOCIAL PRESENCE IS WORTHLESS"
  (corrected 07.09.2026 — the user was right).** The +0.19 finding tests whether **week-to-week
  swings in views** predict **week-to-week swings in downloads**. It has never tested **presence
  versus zero**: the campaign has never run a week with no posting, so that condition has no data.
  Citing the correlation as grounds to stop posting is a misuse of it — and it was cited that way.
  **A baseline presence is a defensible, untested position; only the claim that *tuning* content
  moves downloads is falsified.** Keep the two apart in any argument about posting volume.
- **★ `while True` PAGINATION WITH NO PAGE CAP IS A QUOTA BOMB (found 08.09.2026).** `./run.sh`
  sat at "Discovering YouTube (playlist) …" for 12 minutes and looked frozen. It was not stalled —
  `lsof` showed the local port climbing by **~6 new HTTPS connections per second**, several thousand
  calls, silently. Both pagination loops (`youtube_uploads` and `_uploads_tail`) exited only on
  `if not token: break`, and a playlist can return a `nextPageToken` that yields the same page
  forever, so that condition never fires.
  · **The damage is the YouTube quota, not the clock.** 10,000 units/day, 1 unit per
    `playlistItems` call, ~6 calls/second → the whole day's quota gone in under half an hour, which
    then surfaces as the already-logged `quotaExceeded` 403 and an empty YouTube history.
  · **A hang and a runaway look identical from the terminal.** Distinguish them before waiting:
    `ps -p <pid> -o etime,time,%cpu` (CPU accruing = working) and `lsof -p <pid> -a -i` twice a
    second apart (**local port changing = new connections = a loop, not a stall**).
  · **Fixed with two independent brakes in both loops:** stop if a page token repeats, and a hard
    40-page cap. Never ship an API pagination loop whose only exit is the server's own token.
- **★ THE TWO APPLE FEEDS BEHAVE DIFFERENTLY AT THE TAIL — only one of them backfills
  (07.09.2026, corrected 08.09.2026).**
  · **Sales / downloads: the last day IS partial.** On 04.09 the final row (03.09) read **0**; it
    now reads **2**. A weekly total read on refresh day is undercounted — which is exactly how a
    fine week gets graded a MISS. **Drop the trailing day.**
  · **Analytics / funnel: the last day is NOT partial — it settles immediately.** Verified by
    reading the raw ONGOING instances, each of which carries a rolling 3-day window: 04.09 read
    114 in three consecutive instances, 05.09 read 54 in two. **Values do not move after
    publication, so a low recent impression count is real and must not be waved away as "partial".**
    I initially assumed the opposite and would have dismissed a genuine 70% collapse as an artifact.
  · The analytics feed runs ~1–2 days behind the sales feed; that is lag, not incompleteness.
- **★ APP STORE SCREENSHOTS ARE MINIATURES — design them at tile size, not at full size
  (user's correction, 06.09.2026).** A store screenshot is first seen at roughly **130–150px wide**
  in search results, an ~9× reduction from 1284px. Type sized to look right in a full-size preview
  turns to grey mush there. Working numbers that survive the tile:
  · Headline **~195px** (≈22px at tile), three short lines, uppercase, weight 900.
  · One support line **~85px**. **Two text levels maximum** — a third line is noise at tile size.
  · Wordmark ~52px; legal/attribution ~32px, which is deliberately unreadable in the tile and
    belongs to the product page.
  **Always review at 132px before shipping**, never only at preview size. And move the subject UP:
  a headline that big needs the lower 40% of the frame, so the crop has to put the face and the
  colour block in the top half or the photo and the type fight each other.
- **★ AI-GENERATED STILLS CARRY A VISIBLE GENERATOR WATERMARK — check every one before it becomes
  an asset (found 06.09.2026).** `Marketing-Examples/.../Stills/fashion.png`, proposed as the App
  Store cover, had Google's four-point **Gemini sparkle** burned into the lower right. On a store
  screenshot that is a third-party generator's mark on our own listing — the same category as the
  banned generator names in visible copy, and Apple dislikes third-party branding in screenshots.
  **It is invisible in a thumbnail and obvious at full size, which is exactly backwards from how we
  review images.** Zoom the corners of any generated still before using it.
  **Removal: crop, don't patch.** `delogo` and a copied texture patch both left a visible
  rectangle on the flat concrete background (the wall carries a luminance gradient, and the blur
  kills the grain). Cropping the bottom 12% removed it cleanly and tightened the portrait.
- **★★★ "NO WASTED CREDITS" SHIPPED AGAIN — SECOND TIME IN 25 DAYS. The prose rule failed, so it
  is now a script (08.09.2026).** `Marketing-Prompts-Reel.mp4` carried **"✦ NO WASTED CREDITS"**
  burned into the end card, beside the App Store badge — verbatim the most-banned claim in
  `brand/claims.md`, and the *same claim in the same place* as the 14.08 otter reel. The 14.08
  countermeasure was a sentence telling a human to read rendered frames as caption copy. **It
  failed on its first real test**, because a rule that depends on remembering is not a gate.
  **Fix: `./scripts/check_video.sh <video>`** — extracts a frame per second, OCRs every one via
  Vision (`scripts/ocr_frames.swift`), matches against the banned list, and exits 1 on a hit. It
  caught this in about forty seconds. **Run it on every rendered cut before the cut is approved,
  the same way `./check.sh` runs on every package.**
  · **Language correction is deliberately OFF** in the OCR. It would silently "fix" garbled AI
    label text (SPARALING → SPARKLING) and hide the exact defect worth finding.
  · The script also dumps **all** recognised on-screen text, because no banned-string list can catch
    the other failure mode: **garbled AI text inside the imagery itself.** This same reel has
    `SPARALING REPRESHNENT / NATURALLY FLAVOARED` on the soda label — on the end card, next to the
    App Store badge, in a reel whose entire pitch is shot-ready product photography. The main
    lockup (MRWOLF / LEMON SODA) renders clean; it is the small sub-line that breaks.
  · **Zoom the small text on any AI-generated product shot before shipping it.** Brand lockups
    usually survive; secondary lines usually do not, and they are legible enough to notice.
- **★ THE APP'S OWN UI CONTAINS A BANNED CLAIM — so any full-screen recording ships one
  (found 06.09.2026).** The `Target Platform` section renders **Gemini Veo 3 / Runway Gen 4.5 /
  Kling Video 3 / Seedance 2** on screen. Generator names in visible copy are blocked by the gate,
  and `check.sh` reads the package `.md` — **it cannot see pixels**, which is the same hole that let
  the Aug 14 otter reel ship "NO WASTED CREDITS" on its end card. The difference, and the reason
  this needs its own rule: nobody *wrote* the violation here. It came free with the screen recording.
  **Any capture that scrolls past Target Platform is non-shippable until that stretch is cut.** In
  the 06.09.2026 recording it was on screen from ~5.5s to ~8.8s of 18.35s. **Scrub every screen
  recording for that section before it becomes an asset**, and prefer recordings that stay above it.
- **★ A ZERO in a derived metric is a MAPPING BUG until proven otherwise (found 04.09.2026).**
  The dashboard read "Impressions 0 · Product page views 686 · 56.0% of page views" and was
  believed for two days. All three numbers were wrong, and the zero was the tell: **page views
  cannot exist without impressions.** Three separate bugs, all inside `appstore_analytics()`:
  · **Wrong column.** Apple's report carries an `Event` column (`Impression` / `Page view` / `Tap`)
    *and* a separate `Engagement Type` column (`Get` / `Open` / `Share` / `Update`, empty on
    impression rows). `_pick_col(fn, "engagement")` matched `Engagement Type` first — so all 17,981
    impressions were dropped, and every `Tap` on the product page was counted as a page view.
  · **Summed across duplicate sources.** `Standard` and `Detailed` are the same events at different
    dimensional depth, the snapshot and ongoing requests overlap in dates, and `Web Preview` is a
    browser surface with no impression denominator — the loop added all of them together. Now: one
    report name only, merged per date with **max, never sum**.
  · **All-time numerator over a windowed denominator.** 384 all-time downloads ÷ 119 days of page
    views = the phantom 56%. Real figure 45.9%. **Never divide two numbers without checking that
    their windows match.**
  Fixed in `scripts/refresh.py` and `dashboard/index.html` on 04.09.2026; the funnel section now
  prints its own date range, so a window mismatch is visible on the page instead of silent.
- **★ App Store metadata must be written TWICE — the primary localisation is Englisch (Kanada),
  not USA (found 02.09.2026).** App Store Connect lists two localised languages: *Englisch
  (Kanada)* marked **Primär**, and *Englisch (USA)*. Apple serves the **primary** localisation to
  every storefront that has no localisation of its own — i.e. most of the world, including the
  UK and Australia. Editing only English (USA) ships the new copy to the US storefront and leaves
  everyone else on the old listing. **Every field — subtitle, keywords, promotional text,
  description, What's New — has to be pasted into both, and the language picker sits at the top
  right of the version page, above the screenshots.** This is invisible on the form: both
  localisations look identical until you open the dropdown, so it will silently repeat on every
  future release unless checked.
  **Do not try to fix this by switching the primary language to Englisch (USA)** — Apple blocks
  it until EN-USA screenshots exist *for all versions*, including already-released ones whose
  screenshots can't be edited without a new submission. Attempted 02.09.2026, rejected. Duplicate
  the metadata instead; it takes minutes and blocks nothing. Revisit the primary switch only
  between releases, never while a build is waiting.
- **★ Setting a YouTube video to Private ERASES its view history from `data.js` (found 02.09.2026).**
  `refresh.py` authenticates with an API key, not OAuth, so a private video comes back as
  `"Private video"` with `views: null` — and nothing carries the previous number forward. There
  are already **9 such rows** (5 private, 4 deleted), 4 of them from August. Consequences:
  · Any per-month YouTube median is computed on the surviving subset, so **privating the good
    posts makes a month look worse than it was, and privating the bad ones makes it look better.**
    The "August median 11" reading is on 7 of 11 August videos and should be treated as biased.
  · Deleting a video loses the number permanently; privating loses it only until republished
    (YouTube keeps the count on its side, so it returns on the next refresh after going public).
  **Before privating anything, write the view count down.** And note the separate, already-logged
  rule: a video that was Private during its launch window never recovers its push. Toggling an
  already-public video private and back keeps the count but loses its search/suggested position.
  **Fix worth making:** `refresh.py` should carry last-known-good views forward for a video that
  goes private (same principle as the source-level staleness guard) instead of writing null.
- **The gate reads the package `.md` — it CANNOT see the rendered video.** The Aug 14 otter reel
  shipped to review with **"NO WASTED CREDITS"** burned into the end card (the single
  most-banned claim in `brand/claims.md`) and an invented lighting name **"MIDDAY"** on a
  segment label — both would have been blocked instantly in text, both sailed through because
  they were pixels. **Before approving any rendered cut, read its on-screen text as if it were
  caption copy** (extract frames if needed) and run the same claims check.
- **A guardrail that has never fired is not a guardrail.** The `#aiproductphotography` context
  rule scanned the whole caption *including the hashtag line* — and the tag itself contains the
  fit keyword "product", so it always justified its own presence. Dead since written, found only
  by writing a test that asserted it should fail. **When adding a context/keyword rule, test the
  negative case**, and never let the thing being judged be part of the text you judge it by.
- **A partial API failure is more dangerous than a total one.** `refresh.py` guarded against
  "every source returned nothing" but not "two of four returned nothing" — so a transient YouTube
  404 plus an expired TikTok token silently overwrote 47 and 40 posts of history while Meta
  succeeded. Guards must be **per-source**, and a failed fetch must preserve, not overwrite.
  Also: the YouTube handler discarded the 30 items it had already collected before failing.
- **YouTube has now shipped Private three times** (14.07.2026, 07-25, 08-12 — all `null` views
  in `data.js`). The gate warns every run and cannot verify the toggle. Confirm Public in the
  Studio UI before treating a YouTube post as published.

## ★ Verified hashtags — source of truth is `brand/registry.json`
_Verify any new tag on-platform, add it there, then note it here if useful._

---
*Fresh start 13.08.2026. Rebuilt from data, not inherited. Keep it lean — a tangled ledger is what stops the system learning.*
