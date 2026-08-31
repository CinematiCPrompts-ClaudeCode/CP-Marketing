# CLAIMS — what you may and may not say about the product

Overclaiming is the single most-corrected mistake in this system's history. **Check this
list before writing any caption, CTA, on-screen text, App Store copy, or hook that states
what the product does.** If a claim isn't clearly supported here, verify against the app
source (`../cinematic-prompts-app`) and `brand/positioning.md` before using it — and add
the result here.

The pattern to catch in yourself: a *specific* new phrasing of an old overclaim. Every
banned item below was individually corrected only after it shipped. The rule is the class,
not just the exact words.

## BANNED — never say these

| Don't say | Why | Say instead |
|---|---|---|
| "no wasted credits" / "zero waste" | The app writes the prompt; the generator can still miss. | "**fewer** wasted credits" / "lands far more often" |
| "lands first try" / "one perfect shot every time" / "guaranteed" | Same reason — no guarantee is truthful. | "lands more often" / "less guessing" |
| "one prompt" made a multi-scene / set-change video | The app generates ONE scene's prompt at a time; multi-scene transitions are hand-assembled by the user. | "So many looks. One app." (variety framing) |
| "we have more presets" / "more camera presets than \<competitor\>" | FALSE — Higgsfield has 50–100+ camera-motion presets, more than ours. | "Other tools give you camera buttons. We give you the director's prompt — and it works everywhere." |
| "one continuous take" / "no cuts" as the selling point | That's a *production* detail, not a product benefit. | Sell the feature (style/light/angle by choice), not the filming technique. |
| Sora as a supported generator | Never existed in the product; removed. | Gemini (Nano Banana / Veo), Runway Gen 4.5, Kling, Seedance. |
| "harsh noon" / "overcast" lighting | These lighting names do not exist in the app. | Use only the 5 real names below. |
| lowercase "golden hour" | The live v1.8 display name is capitalized. | "**Golden Hour**" |
| ~~v1.8.2 "6 environments"~~ — MOVED, now verified below (Aug 3) | — | — |
| "storyboard" as a feature/keyword | Corrected by user Aug 4 — the app has nothing to do with storyboards. `storyboard` was in the legacy App Store keyword field and got carried forward by mistake; the Contact Sheet / Turnaround Sheet tools are not storyboarding. | Don't use "storyboard" anywhere — keywords, captions, or copy. |
| "tuned for Gemini, Runway, Kling, and Seedance" phrased as the full list | Corrected by user Aug 4 — reads as exclusive/locked-to-4-tools, when the real claim is universal. | "Works with any AI image or video generator — including Gemini, Runway, Kling, and Seedance" (name them as examples, never as the closed set). |

## ALLOWED — the true, current edges (v1.8 live)

- **Fewer wasted credits / lands more often.** Lead with the pain (wasted credits) before the relief.
- **Style, lighting AND camera angle — all by choice.** This is the core differentiator.
- **5 daylight lighting conditions:** dawn, sunny, Golden Hour, blue hour, night. (Use these exact names.)
- **6 camera angles (v1.8):** Bird's Eye, Centered Eye-Level, Slight High, Dramatic Low, Close-Up, Front 3/4.
- **12 art-directed styles** (exact names in the app source).
- **Prompts are portable across every generator** (Gemini/Runway/Kling/Seedance) — the real honest edge vs competitors' UI controls locked to one platform.
- **Marketing Prompts (v1.8):** Cinematic Ads / Product Photography / Fashion Photography, plus studio lighting — broadens the audience to sellers/brands.
- **6 product environments (v1.8.2, VERIFIED Aug 3 2026 against `mrwolfcineprompts-daca2fe5-main/src/lib/promptGenerator.ts`):** Seamless White Sweep, Neutral Studio Backdrop, Lifestyle Scene (Living Space), Nature Setting, Futuristic Environment, Luxury Interior. Safe to market as soon as 1.8.2 is confirmed live on the App Store.
- **12 cinematic styles, verified unchanged in the 1.8.2 source:** Tokyo Noir, Mexico City, Napoli, Nature Documentary, Historical Documentary, Post Apocalyptic, Prenzlauer Berg, 90s Indie, 70s Gritty, Black & White, In India, Seen by Alien.

## The verification rule
The app **source code is always ahead of what's shipped.** Before marketing any feature you
haven't been explicitly told is live, re-verify it's actually in the current App Store build —
don't assume code = shipped. Current-version facts live in `brand/positioning.md`.

---
*Seeded 2026-08-03 from the corrections logged in PROTOKOLL.md. Add every future claim ruling here.*

## Verified combination counts (2026-08-30, from `promptGenerator.ts`)

**870 user-chosen setups total.** The two surfaces use different dials — never attribute one
surface's output to the other's inputs:

| Surface | Dials | Combinations |
|---|---|---|
| Cinema | 12 styles × 5 daylight × 6 camera angles | 360 |
| Product Photography | 6 lighting × 5 angles × 8 environments | 240 |
| Cinematic Ads | 6 lighting × 5 angles × 8 ad environments | 240 |
| Fashion Photography | 6 lighting × 5 angles | 30 |

**BANNED phrasing:** "360 cinematic *and marketing* looks from 12 styles, 5 daylight conditions
and 6 camera angles." Those are cinema-only axes; marketing does not derive from them. Say
"870 setups", or scope 360 explicitly to cinema.

**Fashion caveat:** its environment is `pick(FASHION_ENVIRONMENTS)` — random, not user-selected.
So "chosen, not guessed" is true of lighting and angle across all three marketing categories,
but not of the fashion backdrop. Don't claim full environment control for Fashion.

**Environments:** 8 for Product/Fashion, 8 for Cinematic Ads, but two labels (Urban Daylight,
Architectural Glass Atrium) appear in both — **14 unique**, not 16.

**Shipping status:** ✅ developer-confirmed 2026-08-30 that the two added environments
(Urban Daylight, Architectural Glass Atrium) are in the **1.8.4** build, so **8 is safe to
publish** once 1.8.4 is live. The 1.8.3 listing still says 6 — do not state 8 until 1.8.4
is actually released.
