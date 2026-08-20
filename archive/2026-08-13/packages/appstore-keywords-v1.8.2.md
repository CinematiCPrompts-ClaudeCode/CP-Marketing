# App Store keyword field — v1.8.2 update

**Trigger:** user reports random App Store searches for "Ai Prompt generator" and "AI Cinematic prompt Generator" aren't finding the app. Per the parked plan (`appstore-aso-v1.8.1.md`, Jul 20), 1.8.2 is the checkpoint to revisit it — this IS that revisit, scoped to what's actually being asked (the keyword field, not name/subtitle/description).

## The honest read first
Apple indexes search ONLY from **App Name → Subtitle → Keyword field**, in that weight order; the description isn't indexed at all. The live Name (`Cinematic Prompts`) + Subtitle (`Cinematic AI prompt generator`) already contain every token in both missed phrases — **ai, cinematic, prompt, generator**. So the app is technically *eligible* for those searches already; it's just ranking too low to surface. **The keyword field can't fix that by itself** — repeating name/subtitle words there is wasted space (Apple's own guidance), and eligibility isn't the bottleneck.

**Decision: ship the keyword-field tightening below now** (it's this week's ask, zero risk, and it's not doing nothing — it adds real new-token coverage). **But the actual fix for "not found for AI Prompt Generator" is still the app-name lever from the parked plan** (`Cinematic Prompts AI Generator`, 30/30 chars) — that's the one move that would meaningfully move ranking for that exact phrase, and 1.8.2 is a legitimate version bump to carry it on. That's a bigger, branding-level call — flagging it, not doing it unasked, since this round only asked for keywords.

## New keyword field (99/100 chars)
```
veo,kling,runway,seedance,nano banana,gemini,camera angle,lighting,product photo,fashion,photoshoot
```

**Corrected Aug 4** — the first draft kept `storyboard`. User caught it: the app has nothing to do with storyboards (I'd wrongly associated it with the Contact Sheet / Turnaround Sheet tools, which aren't storyboarding). Dropped it and used the freed space for `photoshoot` — a real, generic, high-relevance term for the Marketing Prompts (product/fashion) audience that isn't tied to any one generator.

**Changes from the current field** (`veo,kling,runway,seedance,filmmaker,camera angle,daylight,product photo,ad,fashion,storyboard,film`):
- **Dropped `filmmaker`, `film`, and `storyboard`** — generic/inapplicable; `camera angle` already signals filmmaking context, and the app has no storyboard feature.
- **Dropped `ad`** — too generic alone to earn its 3 characters; `product photo` and `fashion` already cover the commercial lane.
- **Added `nano banana` + `gemini`** — real, currently-supported generator terms (Gemini's Nano Banana 2 model) that weren't in the field at all. Verified via web search (Aug 3): the "Nano Banana" trend has 1B+ impressions since Jan 2026 — this is a genuinely high-traffic, high-relevance term, not a guess.
- **Added `photoshoot`** — generic, real search term, reinforces that prompts serve any kind of shoot rather than being locked to named tools.
- **Swapped `daylight` → `lighting`** — same length, broader/more commonly searched term for the same real v1.8 feature.
- **Kept:** `veo`, `kling`, `runway`, `seedance` (people search generators by name — these are examples of what the app works with, not the exhaustive list), `camera angle` (v1.8 feature), `product photo`, `fashion` (Marketing Prompts commercial lane).

**Also corrected Aug 4:** the What's New draft below, and the Diversity reel captions, said prompts are "tuned for Gemini, Runway, Kling, and Seedance" — that reads as a closed list. The real claim (already correct in `brand/claims.md`) is **prompts work with any AI image or video generator**; those four are named examples, not the full set. Fixed in both places.

## What's New copy (pairs with the keyword update)
Bundle this into the 1.8.2 submission so the keyword change isn't a silent, isolated tweak:
> New Marketing Prompts environments (product photography): Seamless White Sweep, Neutral Studio, Lifestyle Scene, Nature Setting, Futuristic, and Luxury Interior. Refinements throughout.

*(Verified against source Aug 3 — see `brand/claims.md`. This was flagged UNVERIFIED as of Aug 1; now confirmed in `mrwolfcineprompts-daca2fe5-main/src/lib/promptGenerator.ts`, so it's safe to put in the listing.)*

## Re-check
Search both phrases again ~1–2 weeks after 1.8.2 settles, in a store where the app is actually available (not the US). If still absent, that's the signal to run the app-name change as its own tracked experiment.
