# LESSONS — what we already know (fresh start 2026-08-13)

Clean slate. The prior ledger was useful but had tangled into corrections-on-corrections,
which was itself causing repeated mistakes. It's archived under `archive/2026-08-13/`. This file
is rebuilt from the raw numbers, not inherited.

**Read before producing anything.** Fill the three sections below from your own analysis of
`dashboard/data.js`. One line per entry — narrative belongs in `PROTOKOLL.md`; fixed rules and
verified hashtags live in `brand/registry.json` (the gate reads that).

---

## ★ What wins — rebuild this from data.js (only patterns you can attach a real number to)
_Filled 2026-08-13 from a full re-read of `dashboard/data.js` after `./run.sh`. TikTok token
was connected same day — re-pulled, 40 posts now real; TikTok section updated below._

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

**TikTok — restored 2026-08-13, 40 posts, avg 588 views/post (highest average of any platform).**
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

**★ CONFIRMED 2026-08-21 — product-pain framing beats showcase framing on TikTok, 3.5×.**
The cleanest controlled comparison in the dataset: two nature/animal TikTok posts five days
apart, same channel, same subject class, differing in caption frame.
· Aug 12 wildlife-as-subject — "No safari. No plane tickets. No wildlife crew." → **230**
· Aug 17 product-pain — "Stop regenerating just to fix the lighting." → **805**
805 is 3.1× the August average (262). Predicted "clear 500" before posting; it cleared.
**Product-pain is now the default TikTok frame, not an experiment.** Name the pain the creator
actually pays (wasted credits, re-generating, flat light) — never sell the footage's subject.
Caveat: n=1 per frame, non-identical footage — consistent with, not proof of.

**August 2026 — what the "animal reel flopped" post-mortem actually showed (added 2026-08-14).**
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
  Also note the same post went out twice on both 2026-08-12 and 08-13 — check for duplicate posting.

## ★ Pre-flight checklist — the gate enforces the fixed rules (`./check.sh` → `brand/registry.json`)
_Add only judgment-level reminders here as you learn them; the deterministic checks already run in code._

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
- **YouTube has now shipped Private three times** (2026-07-14, 07-25, 08-12 — all `null` views
  in `data.js`). The gate warns every run and cannot verify the toggle. Confirm Public in the
  Studio UI before treating a YouTube post as published.

## ★ Verified hashtags — source of truth is `brand/registry.json`
_Verify any new tag on-platform, add it there, then note it here if useful._

---
*Fresh start 2026-08-13. Rebuilt from data, not inherited. Keep it lean — a tangled ledger is what stops the system learning.*
