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
*Seeded 03.08.2026 from the corrections logged in PROTOKOLL.md. Add every future claim ruling here.*

## Verified combination counts (30.08.2026, from `promptGenerator.ts`)

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

**Only TWO dials are universal — lighting and camera angle (added 02.09.2026).** This is the rule
that stops the recurring misattribution. Per surface:

| Dial | Cinema | Cinematic Ads | Product | Fashion |
|---|---|---|---|---|
| Lighting | ✅ (5 daylight) | ✅ (6 studio) | ✅ (6 studio) | ✅ (6 studio) |
| Camera angle | ✅ (6) | ✅ (5) | ✅ (5) | ✅ (5) |
| Style | ✅ (12) | ❌ | ❌ | ❌ |
| Environment | ❌ | ✅ (8 ad) | ✅ (8) | ❌ random |

So **"pick the lighting and the camera angle" is the only dial phrase that can be attached to the
870 figure.** *Style* is true of 360; *environment* is true of 480 (Ads + Product) and is picked
at random for Fashion. Adding either to a universal-sounding sentence ("…on every shot") is the
same misattribution as the banned sentence below, just harder to spot — it has now been caught
twice in two days on the same field. Scope them or leave them to the description.

**Surface names are not a flat list (added 02.09.2026).** The four surfaces are **Cinema,
Cinematic Ads, Product Photography, Fashion Photography** — *Marketing Prompts* is the parent
containing the last three. Never write "cinema, marketing, product and fashion": it lists a
parent beside two of its own children and silently drops Cinematic Ads, a 240-combination
surface. Correct short form: **"cinema, ads, product and fashion."**

**Fashion caveat:** its environment is `pick(FASHION_ENVIRONMENTS)` — random, not user-selected.
So "chosen, not guessed" is true of lighting and angle across all three marketing categories,
but not of the fashion backdrop. Don't claim full environment control for Fashion.

**Environments:** 8 for Product/Fashion, 8 for Cinematic Ads, but two labels (Urban Daylight,
Architectural Glass Atrium) appear in both — **14 unique**, not 16.

**Shipping status:** ✅ developer-confirmed 30.08.2026 that the two added environments
(Urban Daylight, Architectural Glass Atrium) are in the **1.8.4** build, so **8 is safe to
publish** once 1.8.4 is live. The 1.8.3 listing still says 6 — do not state 8 until 1.8.4
is actually released.

## Ruling 06.09.2026 — the four-dial screenshot slogan

**Proposed for the App Store cover screenshot:** *"Select the Style, Lighting, Camera Angle,
Environment and generate Prompt (Less wasted credits)"* — over a **Fashion Photography** image.

**BANNED as written**, on two counts:
- **The four dials never coexist on any screen.** Per the verified table above, only *Lighting* and
  *Camera Angle* are universal. *Style* is Cinema-only. *Environment* is Product + Cinematic Ads;
  **Fashion picks it at random.** So the list describes no surface that exists.
- **The image makes it concrete.** On a Fashion shot, *two of the four listed dials are false for
  the very picture they are printed on.* This is the "harder to spot" misattribution the
  02.09.2026 note warns about — a screenshot is the worst place for it, because the picture is the
  claim's own counter-example.
- **"Less wasted credits" → "Fewer wasted credits."** Count noun, and "fewer" is the approved
  wording.

**Approved replacement (shipped on the cover):**
> FEWER WASTED CREDITS
> **Pick the light. Pick the angle.**
> We write the prompt. **870 setups** across cinema and marketing.

**Why this keeps the intent:** the two universal dials carry the "you choose it" spine truthfully,
and **870** carries the breadth that *Style* and *Environment* were reaching for — while mapping to
the app's own two top-level buttons (Cinematic Prompts / Marketing Prompts) rather than implying a
combination. **General rule: a dial list on a screenshot must be true for the image beside it.**

## Ruling 06.09.2026 — generator ATTRIBUTION on App Store assets is allowed, and often required

**Approved on the cover screenshot:** *"Image generated with Nano Banana — from a prompt written in
this app."*

This is not a reversal of the generator-name rule; it is the other side of it. **The gate blocks
generator names in social caption copy, where naming Gemini/Runway/Kling/Seedance reads as
"locked to these four tools."** An attribution line under a photograph does the opposite job:

- **The app writes prompts. It does not generate images.** A beautiful fashion photo on a store
  screenshot, with no credit, implies the app made the picture — an overclaim by implication, and
  the most expensive kind because it survives into the user's expectation and then into a refund.
  The credit line is what removes that implication.
- **Name generators as an EXAMPLE, never as the supported set.** "Generated with Nano Banana" is a
  fact about one picture. "Works with Gemini, Runway, Kling and Seedance" as a closed list stays
  banned (see the table above).

**A generator's WATERMARK is still not allowed** — that is uncontrolled third-party branding sitting
in the middle of our own listing, and it reads as a defect. Crop it out and write your own credit.
The two are different things: one is their placement, one is ours.

## Ruling 09.09.2026 — "Sora" resurfaced, on the App Store preview itself

`App Store Intro.mp4`, chapter 05 / TARGET PLATFORM, caption reads:
> *"Built for your model. **Veo 3, Runway Gen 4.5, Kling, Sora** — syntax tuned per platform."*

**BLOCKING, on two separate counts.**

1. **Sora has never been in the product.** It is listed as removed in the banned table above. This is
   not an exaggeration, it is a false statement about what the app supports — placed on the App
   Store listing, which is where Apple reviews and where a user's expectation is set. **The app's
   own UI in the very same shot shows `Seedance 2`, not Sora**, so the caption contradicts the
   screen it is captioning.
2. **The four-name list is the banned closed-set construction.** "Veo 3, Runway Gen 4.5, Kling,
   Sora — syntax tuned per platform" reads as locked to four tools, which is the exact phrasing
   ruled against on 04.08.

**Approved replacement:**
> Built for your model.
> Works with any AI image or video generator — Veo, Runway, Kling, Seedance.

The honest claim is also the stronger one: **portability is the edge** over competitors whose
controls are locked to a single platform. A closed list throws that away and adds a false name.

**Also corrected in the same video:** chapter 03's *"Dawn, sunny, golden hour, blue hour, night"* →
**Golden Hour** capitalised (the app's own UI shows it capitalised two frames earlier), and the end
card's *"LESS WASTED CREDITS"* → **FEWER**.

**Process note:** all of this was found by `./scripts/check_video.sh` in about forty seconds, the
day after that script was written. The pixel gate is now doing the job the prose rule could not.

## Ruling 14.09.2026 — "more than just daylight" is TRUE; the four-dial list is still not

**Verified today against the LIVE source** (`~/Desktop/Cinematic Prompts - Claude Only/
mrwolfcineprompts-daca2fe5-main`, the canonical copy — not the stale Lovable clone):

- `src/pages/Index.tsx` (cinema) renders **Cinematic Style · Lighting Condition · Camera Angle**.
  **No Environment.**
- `src/components/MarketingSection.tsx` renders **Environment · Lighting · Camera Angle**.
  **No Style.**

**So Style and Environment still never appear on the same screen.** A tile reading
*"Cinematic Style / Environment / Lighting / Camera Angle"* as one list is the same construction
ruled against on 06.09 — it describes a screen that does not exist.

**But the user is right about lighting, and our copy has been underselling it.** The lighting dial
is no longer five daylight conditions. Two full sets ship:

| Surface | Lighting |
|---|---|
| Cinema | Dawn · Sunny · **Golden Hour** · Blue Hour · Night |
| Marketing (Ads / Product / Fashion) | Warm Studio Light · Cool High-Tech Light · Natural Daylight · Dramatic Contrast Light · Soft Diffused Light · Softbox / Diffused Lighting |

**Stop writing "5 daylight conditions" as the whole lighting story.** Correct forms:
- *"Daylight for cinema, studio lighting for commercial work."*
- *"Eleven lighting setups across the two surfaces"* — if the count is wanted.

**Approved way to say what the user was reaching for**, without inventing a screen:
> **Cinema:** style, light, angle.
> **Marketing:** environment, light, angle.

Two columns, both true, and it shows more breadth than the false single list would — because it
reveals there are two workflows rather than one menu.
