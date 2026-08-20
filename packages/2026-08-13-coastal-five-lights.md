# Content Package — "Same coast, five real lights" (style + lighting demo)

Built from a fresh `dashboard/data.js` read on 2026-08-13. Every platform's pattern below
is a real number from that pull — see `LESSONS.md → What wins` for the full breakdown.

**Asset:** a sea otter in West Coast (Canadian) coastal scenes, re-rendered across the 5 real
daylight lighting conditions — dawn, sunny, Golden Hour, blue hour, night. Same style
(Nature Documentary), same subject and framing, lighting is the only variable. This is the
same subject as the archived Jun 21 "West Coast Wildlife" package (FB 1096, IG 717→1000) —
reused here specifically to demo the v1.8 lighting picker on the proven money-shot, not as a
repeat of that package's angle.

---

## Demo
- **What's in the clip:** a sea otter, West Coast coastal setting, same composition, regenerated once per lighting condition
- **Style shown:** Nature Documentary
- **Daylight lighting shown:** dawn → sunny → Golden Hour → blue hour → night (same scene, all 5)
- **Hook angle:** style + lighting choice (proves you pick the light, not the generator) — with the wasted-credits pain as the cold open

## First 2 seconds (scroll-stopper)
- **On-screen text:** "5 lighting looks. 1 scene." (≤6 words, big)
- **Visual beat:** open on the **Sunny** frame — sharpest contrast and fastest read of the five stills (crisp blue sky vs. the warm haze on dawn/golden hour), so frame one stops the scroll instantly. Cut to Golden Hour second — it's the exact look behind FB's all-time-best post (2496 views, "golden light...") — then blue hour, dawn, night in quick succession.
- **Stills reviewed 2026-08-13:** `Marketing-Examples/Reels-August/Sea-Otter-5Daylight/` (sunny, golden-hour, dawn, blue-hour, night — all 5 present, all usable, no reshoot needed).

---

## ⛔ RENDERED CUT — BLOCKED, do not post (reviewed 2026-08-14)
`Marketing-Examples/Reels-August/Daylight-Reel.mp4` (14.4s, 1080×1920, 30fps). Length and
format are right; four defects must be fixed in a re-render first. The `./check.sh` gate reads
this markdown and **cannot see the video**, so these were caught by frame inspection, not the gate.

1. **End card reads "NO WASTED CREDITS"** — the single most-banned claim in `brand/claims.md`
   ("the app reduces waste, never eliminates it"). Change to **"FEWER WASTED CREDITS"**. Blocking.
2. **Segment 04 is labelled "MIDDAY · 12:30"** — not a real lighting name. The five are dawn,
   sunny, Golden Hour, blue hour, night. Change to **"SUNNY"**. Blocking.
3. **Lighting order runs backwards at the end.** On-screen timestamps go night → 05:10 blue
   hour → 07:55 Golden Hour → 12:30 midday → **06:25 dawn**, so it lands on dawn *after* midday
   while the title card promises "a full day — from midnight to noon." Reorder to
   night → dawn → Golden Hour → sunny → blue hour, or re-cut per the opening note below.
4. **Title card says "Watch one prompt travel a full day."** Each lighting condition is its own
   prompt — `brand/claims.md` specifically flags "one prompt" framing and prescribes the
   "one app"/variety framing instead. Change to **"One scene. Five prompts. Every light."**
   or **"One scene. Every light — one app."**

**Also strongly recommended (not a claims blocker, but it's the biggest view lever we have):**
the cut opens on **night**, the darkest frame — measured mean luma ~16–24/255 for the first
~3.5s, with the bright payoff not arriving until ~6.5s. `CLAUDE.md`'s opening-frame rule and
this package's own spec both call for opening on the brightest, fastest-reading frame. Lead
with **Sunny** (or Golden Hour), then let the day-cycle play. Re-order rather than re-shoot —
the footage itself is good.

---

## TikTok (lead) — caption
Grounding: pain-first lighting hook, 820 ("Stop regenerating just to fix your lighting") — TikTok's own token was reconnected 2026-08-13 and this near-identical hook is already a proven TikTok post, not a cross-platform guess.

Stop regenerating just to fix the lighting.
Pick the light before you generate — dawn, sunny, Golden Hour, blue hour, night. Same scene, five looks, one app.
Free on the App Store — link in bio.

#aivideo #aifilmmaking #aicinema #cinematicprompts
**⏰ Post: Mon 2026-08-17, 19:00 CEST** (5-day gap after the Aug 12 post)

_Revised 2026-08-14: dropped "one sea otter, one West Coast scene" from the lead. August's TikTok post-mortem shows wildlife-as-subject framing underperforms here (safari 230, hunter 279) while product-pain/promise framing wins (821–859). The otter is the vehicle, not the pitch — keep the copy on the mechanism._

## Instagram Reels — caption
Grounding: coastal nature, 717 ("Ocean and coastal AI footage is the hardest...") — same subject matter that's already IG's single best post, now with the lighting payoff up front.

Ocean light is the hardest thing to get right in AI.
Pick the light before you generate. Five looks, one scene. ✦
Free on the App Store — link in bio.

#aivideo #aifilmmaking #aicinema #cinematicprompts #nanobanana
**⏰ Post: Tue 2026-08-18, 19:00 CEST**

_Revised 2026-08-14: tightened to the ultra-short 2-line shape that produced IG's best runs (717 / 301 / 272). Posted a day after TikTok so the two aren't competing for the same first-day push._

## YouTube Shorts — title + description
Grounding: searchable feature title, 599 ("New Cinematic Style: Nature - Coming soon!") — nature content is already YouTube's #4 post; naming the five real lighting condition names keeps this one both correct and searchable.

**Title:** 5 Real Daylight Looks, Same AI Scene — Dawn to Night (Cinematic Prompts App)
**Description:** Pick the lighting before you generate — dawn, sunny, Golden Hour, blue hour, or night. Same coastal scene, five real looks, no regenerating to fix it. Free on the App Store — link below. Set the upload to Public before publishing.

#shorts #aivideo #nanobananapro
**Backend tags:** cinematic prompts app, AI lighting control, golden hour AI video, blue hour AI video, dawn lighting AI video, night AI video, daylight lighting picker, AI video generator app, cinematic AI prompts, nature documentary AI video
**⏰ Post: Thu 2026-08-20, 12:00 CEST**

_🚨 **Set visibility to Public.** Three uploads — 2026-07-14, 07-25 and 08-12 — all sit in `data.js` with `null` views because the visibility toggle was never flipped, the animal reel included. This is the cheapest view loss in the whole system: the upload succeeded and earned zero. Verify the toggle in Studio after publishing, not before._

## Facebook — caption
Experiment: post ONE clean nature-doc post (no duplicate) and treat it as a reach diagnostic, not a content test. Signal: clears 150 → the Aug collapse was content/duplication and nature-doc still works here; stays sub-30 → the problem is account/reach-level, stop rewriting captions and audit Meta Business Suite instead.

_Why this is an Experiment and not a Grounding: the obvious grounding would be "plain declarative nature-doc, 1096" — but Facebook has fallen 512.2 (May) → 318.6 → 157.2 → **6.8** (Aug) average views per post, four straight months, monotonic. Citing a June number as if it were still achievable would be dishonest. Nothing about a caption explains 512 → 6.8._

Same ocean scene, five real lighting conditions — dawn, sunny, Golden Hour, blue hour, and night. Pick the lighting before you generate instead of regenerating to fix it. Free on the App Store.

#aivideo #aifilmmaking #aicinema
**⏰ Post: Wed 2026-08-19, 14:00 CEST — POST ONCE.** The Aug 12/13 animal post went out twice (2 views each); the Jul 27 and Jul 10 posts also appear twice. Confirm there's no scheduler double-fire before publishing.

---

## CTA used this round
Medium rung — "Free on the App Store — link in bio" on every platform. This is a
feature-proof piece riding two already-proven patterns (IG coastal, FB nature-doc), not a cold
audience test, so a direct-but-unaggressive CTA fits; no hard "download now" push needed.

## Scheduling rationale (revised 2026-08-14) — and the one thing I got wrong
**Spacing is not the lever.** I started this review expecting post frequency to explain the
August drop, and the bucket averages looked supportive (TikTok 4–7-day gaps median 679 vs
1–3-day median ~300). The post-by-post list disproves it: a 2-day gap produced 830 views, a
6-day gap produced 297, and Aug 7 had the longest recent gap (7 days) and still landed 266.
**Do not reschedule to fix what is a framing problem.** Recording this in `LESSONS.md` so the
same wrong hypothesis isn't re-derived next round.

What the staggered dates above are actually for — one platform per day, Mon→Thu:
- **Not** algorithmic protection (different platforms don't compete with each other).
- It's operational: one post a day means each upload gets its visibility toggle, its caption,
  and its duplicate-check verified individually. Both mechanical failures in the last cycle
  (YouTube left Private, Facebook posted twice) are the kind that happen when four uploads are
  pushed out in one sitting.
- A 5-day gap after the Aug 12 TikTok post keeps the same-platform cadence in the range the
  good months ran at, without claiming that's what drives the numbers.

**On "increase views slowly":** the growth lever this round is framing, not volume — keep to
roughly one strong post per platform per week and put the effort into the hook. The two
mechanical fixes (Public toggle, no duplicate FB post) recover lost views at zero cost and
should land before any cadence change is considered.
