# August–September Plan — Downloads, Views→Clicks, ASO

Written 2026-08-13 from `dashboard/data.js` (post-`./run.sh`), the live App Store listing
(fetched directly), and `LESSONS.md`. Three stated goals, one plan each, ranked by leverage.

**Baseline, so we can tell if this worked:** downloads/day went **2.07 (Jun 14–Jul 13) →
3.50 (Jul 14–Aug 12), +69%** — a real recent uptick (computed from `daily`, not eyeballed).
327 lifetime downloads, 167 in the last ~2 months. The plan below has to beat 3.5/day, not
just sound good.

---

## Goal 1 — More downloads

**#1 lever — DONE 2026-08-13.** TikTok token reconnected same day this plan was written; 40
posts re-pulled, avg 588 views/post — the highest average of any platform, confirming
`brand/positioning.md`'s "strongest, lead channel" claim. See `LESSONS.md → What wins` for
the refreshed pattern read (transformation hook 1987, narrative "The X" titles cluster
780-1868, pain-first hooks 784-859). Keep posting here at the same cadence as IG/FB — it was
never actually weaker, it was just dark.

**#2 lever: ship the sea-otter 5-lighting package** (already built, gate-CLEAR —
`packages/2026-08-13-coastal-five-lights.md`). It stacks IG's best-ever pattern (coastal
nature, 717 views) and FB's #3 all-time pattern (nature-doc, 1096 views) onto the actual
v1.8 lighting-picker feature. This is the most-grounded piece available this round — post it
this week rather than waiting on the plan below.

**#3 lever: hold cadence.** The +69% uptick lines up with July's posting volume increasing —
don't let cadence slip while attention goes to the ASO work below. 3–4 posts/week across the
three active platforms (TikTok once restored), grounded per `LESSONS.md → What wins`.

## Goal 2 — More views AND more clicks-that-become-downloads

Views alone aren't wired to conversion yet — `data-sources.md` flags "App Store impressions
/ page views / conversion" as `⏳ optional upgrade`, meaning **we currently cannot measure
whether a view actually became an App Store tap.** That's a measurement gap, not just a
content gap, and it should be closed before spending more effort guessing at which hooks
convert.

1. **Turn on the App Store Connect Analytics Reports API** (the async, richer endpoint —
   already scoped in `data-sources.md` as the upgrade path). This gets us real product-page
   views and conversion rate, so "views→clicks→downloads" in `CLAUDE.md`'s own KPI chain
   stops being unmeasured.
2. Until that's live, the only lever we can pull blind is the CTA itself: every caption this
   round states "Free on the App Store" explicitly (removes the #1 objection) rather than
   implying it — already true of the sea-otter package, keep it standard going forward.
3. The product-page fixes in Goal 3 (subtitle, description, screenshots) are also
   Goal-2 work — a stronger page converts the clicks that already arrive, independent of ASO
   ranking.

## Goal 3 — ASO: rank for "AI prompt generator for video"

**Verified against the live listing (v1.8.3, fetched 2026-08-13), not guessed:**
- **Title:** "Cinematic Prompts" — no "generator," no "video."
- **Subtitle:** "Create cinematic AI prompts" — has "AI" and "prompts," but no
  "generator" or "video," and wastes characters repeating "cinematic" (already in the title —
  Apple indexes title + subtitle + keywords together, so repeating a word already covered is
  wasted budget).
- **Category:** Productivity only shown; secondary category not visible from the public page —
  **verify in App Store Connect whether "Photo & Video" is set as secondary; add it if not.**
  This is a straightforward relevance lever for a video-related search term.

This is exactly why the app doesn't surface for "AI prompt generator for video" — neither
"generator" nor "video" exists anywhere in the two fields Apple weights most.

### Recommended v1.8.4 subtitle (30-char cap)
**"AI Prompt Generator for Video"** — 29 characters. Covers the literal failing search
phrase, doesn't repeat "cinematic" (title already owns that word), and is accurate — it
generates prompts *for* video/image generators, which matches `brand/positioning.md` exactly
and doesn't cross any line in `brand/claims.md`.

### Recommended keywords field (100-char cap, no spaces after commas, no repeats of title/subtitle words)
```
image,filmmaker,director,lighting,camera,angle,style,scene,gemini,runway,kling,veo,nanobanana
```
93/100 characters. Generator names are explicitly sanctioned here per
`brand/registry.json` ("Allowed only in a line marked 'Backend tags:' or an App Store keyword
section") — this is that section. Doesn't repeat any word already in the title or subtitle,
which is where most keyword-field budget gets wasted.

### Recommended v1.8.4 description opening (description isn't search-indexed by Apple, but it's
the first thing a visitor who *did* find the app reads — this is Goal-2 conversion work)
> Cinematic Prompts is an AI prompt generator for video and image generators like Gemini,
> Runway, and Kling. Stop guessing — pick your style, daylight lighting, and camera angle,
> and get a filmmaker-grade prompt that lands more often.
>
> 12 cinematic styles, including Tokyo Noir, Napoli, and Nature Documentary.
> 5 real daylight conditions: Dawn, Sunny, Golden Hour, Blue Hour, Night.
> 6 camera angles: Bird's Eye, Centered Eye-Level, Slight High, Dramatic Low, Close-Up, Front 3/4.
> Marketing Prompts for Cinematic Ads, Product Photography, and Fashion Photography.
>
> 100% on-device. No account. Nothing leaves your phone. Free on the App Store.

Checked against `brand/claims.md`: "lands more often" is the approved phrasing (not "lands
first try" / "guaranteed"); no Sora mention; no "storyboard"; generator names appear only as
examples of compatibility, not a closed list.

### Product Page Optimization — the "Cinematic Apps Promo" test
You've already created the test shell in App Store Connect. One thing to know going in:
**Apple's Product Page Optimization only tests icon, screenshots, and app preview video — not
title/subtitle/keywords/description.** Those text fields ship immediately on the next version
update instead (that's the v1.8.4 work above); PPO is purely a visual test.

Recommended 3 variants for the test:
- **Control:** current live screenshots.
- **Variant B — "golden light" lead screenshot:** the sea-otter Golden Hour still as the
  first screenshot. This is a direct re-use of the single best-performing piece of content in
  the whole dataset (FB, 2496 views, "golden light...") as the first thing an App Store
  visitor sees.
- **Variant C — "3-way choice" lead screenshot:** a single screenshot showing the
  style + lighting + camera-angle picker UI in one frame, proving the core differentiator
  (competitors give you one dial, this app gives you three) before a visitor reads a word of
  copy.

**Caveat to set expectations correctly:** at ~3.5 downloads/day, App Store Connect's PPO needs
a meaningfully larger sample to call a winner — Apple's own guidance is ~90 days minimum, and
at current volume that's genuinely a low-traffic test. Worth running since it's free and
passive, but don't expect a fast readout; the ASO fix (subtitle/keywords, which affects
whether people arrive at all) will likely move the needle sooner than the PPO test will.

---

## What to check next round
- TikTok: did `scripts/tiktok_auth.py` get run — is `data.js["tiktok"]` non-empty next pull?
- Downloads/day: still ≥3.5, or did the +69% uptick stall?
- App Store search: does "AI prompt generator for video" surface the app after the v1.8.4
  subtitle/keyword update ships?
- PPO test: still running, any early (non-significant but directional) signal in App Store
  Connect's own test dashboard?
