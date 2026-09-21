# Marketing System Protokoll

Running log of changes, fixes, and decisions. Newest first.

---

## 21.09.2026 — Weekend check-in: FB double-posted again, downloads flat, no new ad ran

- **User flagged "another dismal weekend, 2 downloads despite new screens."** Refreshed
  (`./run.sh`) and checked directly rather than taking the frustration at face value.
- **"The ad" is not new** — checked `AppleAds/` (one screenshot from 08.09, nothing since) and the
  funnel for a paid-style impression spike (none since 10–13.09). This is the same Search Ads test
  from two weeks ago, already concluded and already actioned ("not worth continuing, better work
  on the organic"). Nothing changed there this week.
- **The Vespa package did ship**, but not cleanly: TikTok posted on schedule (18.09, 264 views —
  in line with recent normal range). **Facebook double-posted again** (19.09, 265 + 282 views) —
  a day late and the first duplicate since 03.09's fix. See `LESSONS.md` — this is the 5th
  occurrence and the mechanism still isn't known. Instagram posted with different copy than
  drafted (6 views, unremarkable — the account's known ceiling). YouTube isn't due until 22.09.
- **Downloads: 1 on 19.09, 0 on 20.09 (partial/backfill pending)** — roughly matches the user's "2"
  once App Store Connect's faster real-time count is accounted for. ~800 combined views this
  weekend against 1–2 downloads is not a new finding — it's the same "social views don't predict
  downloads" result this system has now shown for 200+ days. Not this weekend's failure specifically.
- **The one place a real signal could actually show up — the tile-fix window — is 3 days into 14.**
  18.09: 8.22% CTR (6/73). 19.09: 3.12% (2/64). Both at-or-above the 3.36% baseline, tiny samples,
  too early to call either way. Nothing here says the new gallery is failing.
- **Asked the user directly how Facebook is actually being posted** — this repo doesn't auto-post,
  so after 5 occurrences the duplicate has to be either the posting flow or a Meta-side artifact,
  and that's answerable only with information this system doesn't have.

## 18.09.2026 — Red Vespa 4-platform package written ahead of the clip, CLEAR

- **User announced a weekend reel** — one red Vespa, Cinematic Ads, Dramatic Low Angle, cut across
  all four supported generators (Gemini, Runway, Kling, Seedance) to prove portability. **No
  generator named on-screen or in copy**, decided mid-session — the four-clip cut is the receipt.
- **Real grounding found before writing anything:** `LESSONS.md` already has "A luxury Vespa ad"
  at **782 on TikTok**, product-pain-framing cohort (with "No studio. No photographer. No shoot."
  859). So the hook is pain/promise ("Stop rewriting your prompt for every generator"), not a
  feature-list ("works on 4 platforms!") — the dataset is explicit that feature-lists lose on
  TikTok (297, 291, 266) regardless of how true they are.
- **Written and shipped as descs only — the clip itself hasn't arrived.** User was in a rush;
  produced `packages/2026-09-18-red-vespa-four-generators.md` from the concept alone since
  everything the copy needed (subject, angle, generator count, no-names decision) was already
  pinned down. Flagged in the file itself that times/on-screen beat may need a one-line adjust
  once the actual edit is seen.
- **`./check.sh` caught three real things on the first pass, not busywork:**
  1. `#aiproductphotography`'s context-fit check failed on Instagram/YouTube/Facebook because the
     prose never said the word "product" — true content, unstated in the copy. Fixed by naming it
     a **product ad** in each caption (accurate: Cinematic Ads *is* the product/ad surface).
  2. The Facebook Grounding line split across two source lines in the draft; `has_grounding()`
     only checks for a digit on the *same* line as `Grounding:`, so a wrapped line with the numbers
     one line down reads as ungrounded. **Lesson: keep the Grounding line unbroken, numbers and
     all, even if it runs long** — a wrap that looks fine to a human fails the gate.
  3. The YouTube block's own reminder to "confirm Public — this channel has shipped Private 3×
     before" tripped the anti-Private check by containing the word "Private" in a warning *against*
     shipping Private. Reworded to avoid the literal word while keeping the warning.
- **Still open:** the actual clip. Once it lands, re-check the on-screen beat and posting times
  against the real edit — the copy and gate pass are final, the times are not load-bearing yet.

## 18.09.2026 — 1.8.7 confirmed live. Refreshed the data; a real organic keyword win

- **1.8.7 is live**, per the user this morning. Yesterday's entry logged the release as clearing
  review "today" (17.09) — it actually landed 18.09. **The tile-fix window is set to 18.09.2026 →
  ~02.10.2026.** Same decision rule as before, only the date moves again.
- **`./run.sh` re-run.** Funnel feed (impressions/page views/taps) only covers through **16.09** —
  no visibility yet into 1.8.7 or the new gallery, which is the expected 1-2 day lag on the
  ONGOING analytics feed, not a problem. Downloads data runs through 17.09 (reads 0, the known
  partial-last-day backfill on the Sales feed). **Nothing in this refresh can be read as caused by
  1.8.7 yet — too early, check again once 18–19.09 land.**
- **12–16.09 in the interim (still pre-public-gallery): 2.17% · 2.22% · 17.78% · 8.97% · 1.45%
  CTR.** Bounces around the 3.36% baseline on 50–100 daily impressions — small-sample noise, not a
  signal. The 14.09 spike (16/90) predates the gallery going public and is consistent with the
  poster-frame swap alone (`plans/2026-09-14-tile-fix.md` step 1, no-release), at a sample size too
  small to lean on.
- **★ Real organic signal, independent of the tile read: "ai prompt generator runway" now ranks
  #6 in App Store search** (user-checked today). `runway` has been a live keyword since 1.8.4
  (`plans/2026-08-30-appstore-1.8.4-launch.md`), and this is the first confirmation it's actually
  surfacing the app on a generator-name search — not just drawing paid impressions the way the
  14.09 ad showed `veo`/`kling` doing. Consistent with, and now a second line of evidence for, the
  generator-keyword strategy the 12.09 hold parked for the next metadata release.

- **Android platform created — Play Store is now a live track.** The app repo
  (`~/Desktop/Cinematic Prompts - Claude Only/…`) has an `android/` folder as of today, scaffolded
  fresh from the canonical source (Capacitor 8, Gradle 9.5 / AGP 9.3.2), `versionCode 1`,
  `versionName 1.8.7` — matching the iOS build that went live today. A debug APK installs and
  generates prompts on an emulator; `bundleRelease` produces an AAB. The Lovable clone's android
  folder was NOT reused: its `src/` is behind canonical, so it would have shipped an older app
  than iOS. **Marketing consequence: nothing is postable about Android yet** — no store listing,
  and a Play listing needs a *publicly hosted* privacy policy, which doesn't exist yet (the policy
  only lives in-app). That hosting is the one hard blocker on the Play timeline.

## 17.09.2026 — CORRECTION: the 15.09 gallery wasn't public. It goes live today with 1.8.7

- **Staged in Connect ≠ live.** The 15.09 entry below says "New gallery live" — wrong word.
  What happened 15.09 was the upload to App Store Connect, attached to the pending 1.8.7
  submission. Until today, the App Store has still been showing **the video + the old step
  slides** to every searcher and every organic visitor. **The video + the new 3-slide gallery
  (cover / dials / scene) go public for the first time today, when 1.8.7 clears review.**
- **★ LESSON — the tile-fix measurement clock starts on public release, not on upload date.**
  The 15.09 baseline math and the pre-registered 2-week read in
  [plans/2026-09-14-tile-fix.md](plans/2026-09-14-tile-fix.md) assumed the new gallery had
  already been serving impressions for two days. It had not served any. **The window is
  reset to today → ~01.10.2026**, not 15.09 → 29.09. Nothing about the pre-registered decision
  rule changes, only the dates. Added to `LESSONS.md` so this stops being a recurring trap —
  screenshot/preview changes attached to a version submission don't go live until that version
  clears App Review, however early they were uploaded.
- **Consequence for the before/after slides (apocalyptic-portrait pair) discussed this session:**
  the hold stands, and the date moves with it — build now, ship after the window closes
  **~01.10.2026**, not 29.09. Shipping them with 1.8.7 today would mean the tile-fix experiment
  has never run clean for a single day.

**Before/after pair built, phone + iPad, banked for ~01.10.2026 — not uploaded today.**

- **Source photos** (`Marketing-Examples/Best-of/without-cp.jpg`, `apoc-closeup.jpg`) copied into
  `brand/assets/` as `tile-before-photo.jpg` / `tile-after-photo.jpg`. Same generator (Gemini)
  behind both, named identically on each credit line, so the only variable the pair demonstrates
  is whether a prompt came from the app — a controlled comparison, not just two nice photos.
- **Verified against ground truth before building anything:** Post Apocalyptic, Golden Hour and
  Close-Up are all real, live v1.8 Cinema-screen dials (`brand/claims.md`), and style + lighting +
  camera angle are the one trio that actually coexists on one screen — no repeat of the 06.09
  four-dial ruling.
- **Copy, simplified per user direction mid-session:** eyebrow → **Before** / **After**, headline →
  **Just a prompt.** / **Chosen, not guessed.** — dial receipt and the Gemini credit line stay
  underneath on both.
- **Two real layout defects found and fixed by rendering and measuring pixels, not by eyeballing
  the HTML** — same discipline as the 14.09 tile work:
  1. The after-tile's credit line initially collided with the photo's top edge once the copy
     block grew past the cover tile's length. Fixed by cutting the headline to one short line and
     moving the dial values to the amber sub-line instead of stacking both in the headline.
  2. **Both photos used `object-fit:cover`, which is wrong for a 768×1376 source going into a
     1284×1560 box** — it left the after-tile's face small and high with a wall of empty scarf
     below crowding the footer, and cropped the before-tile's woman off at the ankles beneath a
     mostly-empty storefront. **Fixed with a manual pixel crop** (explicit width/height/top/left
     on the `<img>`, not `object-position` percentages) on both tiles, then re-fit to the same
     source y-window for the iPad pair's taller, narrower column. **Object-fit:cover is fine for
     a target box close to the source's own aspect ratio; for a narrow tall box against a
     4:3-ish or full-figure source, it needs checking by rendering, every time — this is now the
     second tile session in a row this exact class of bug has shown up.**
- **iPad pair** (2064×2752) built on the existing side-by-side pattern from `tile-cover-ipad.html`
  — photo pinned right, type column left — with the same manual-crop math re-solved for the
  taller box rather than re-guessed.
- **Exported to `Marketing-Examples/Cinematic Prompts/Appstore /Previews/`** as `04-before-...` /
  `05-after-...` in both `iPhone/` and `iPad/`, continuing the existing `01`–`03` numbering.
  **Staged for handoff only — not uploaded to App Store Connect.**

## 15.09.2026 — New gallery live: 3 CI-built screenshots, the five old step slides deleted

- **Uploaded:** poster frame repointed to the red-dress opening, then three new screenshots —
  the B&W portrait cover, "Style. Light. Angle." (the dials + five lights shown), and
  "Style it. Place it. Frame it." (12 styles · 8 ad environments · 6 camera angles, 26 outputs).
  **All five old step slides deleted.** 1 preview + 3 screenshots.
- **Built to the developer's CI** (`docs/brand/corporate-identity.html`, 14.09.2026): black→#222
  gradient ground, Jost for everything read, Playfair for the wordmark only, Space Mono for values,
  amber `#F4AA34` as the single accent, Paper `#F5F4F0` never pure white. Every count and every
  product name verified against the live 1.8.6 source, not the CI's vocabulary list — which is how
  the six studio lights it omits were found.
- **Deleting the old slides is the right trade, and it is fully reversible** — screenshots need no
  release. The old slides were redundant with the preview video, off-CI on `#4d4d59`, and sat in
  slots 4–8 where only someone already scrolling the product page would see them.
- **★ The change is separable, which is rare here.** It falls exactly along the funnel's own split:
  · **impression → page view** measures the TILE (first tiles only)
  · **page view → install** measures the PAGE (the slides that were deleted)
  So for once two simultaneous changes can be read apart.
- **Baseline recorded before the change**, 25.08–12.09 excluding the paid window 10–13.09:
  **2,437 impressions → 82 page views = 3.36% CTR**, and **82 page views → 42 downloads = 51%**.
- **Decision rule, pre-registered:**
  · CTR up, install rate holds → unambiguous win, leave it.
  · CTR up, install rate down → a real trade; quantify it before judging.
  · **Install rate falls below ~40% → put two step slides back in slots 4–5.** That is the page
    doing work we removed.
  · CTR flat after two weeks → the tiles were not the bottleneck and the **icon** is the remaining
    variable.

## 12.09.2026 — HOLD: no metadata until the release after 1.8.6. Let the ad and the reel finish

- **User's call, and it is the right one.** Too many variables have been moving at once. **1.8.6
  ships as a pure bug-fix with metadata unchanged**, same as 1.8.5 — so three releases in a row
  leave the keyword index alone. **The listing does not change until the release after it (1.8.7
  unless renumbered).**
- *Version numbering has drifted in this project before* — commit `f5cc6f6` is literally "Correct
  the release version: 1.8.4, not 1.8.5". **Record the number that actually shipped, not the one
  that was planned.**
- **Parked until then:** the keyword-field rewrite (generator names — `kling`, `seedance`, `veo`,
  the 3–4/5 popularity terms currently missing), the preview's closed-set phrasing, and Golden Hour
  capitalisation in chapter 04. All drafted, none urgent.
- **Correction to an earlier false urgency:** Apple Search Ads reporting **persists after a campaign
  ends**. There was no need to pull the per-keyword numbers before 13.09 21:00; they can be read any
  time afterwards.
- **Two results still to come in, and they are the only things being waited on:**
  1. **Search Ads** ends 13.09 21:00 — per-keyword impressions and TTR, three readings
     pre-registered in `plans/2026-09-08-search-ads-probe.md`.
  2. **The reel** across the weekend — Facebook is the live experiment, **clears 200 → the caption
     formula is the driver; under 50 → content type was.**
- **Next checkpoint: a weekly review around 16–17.09**, once both have landed. That review grades
  the reel against its signal, reads the ad data, and turns both into the next metadata payload.
- **Still running quietly:** daily organic impressions (recovering — 50 → 116 pre-ad), and the
  campaign-link/Pinterest work, which needs no release.

## 12.09.2026 — The collapse was transient. Impressions recovered, downloads reversed, revert is off

- **1.8.6 shipping as a pure bug-fix release, no metadata touched** — after a Claude Code review of
  the Lovable app found extensive errors, cleaned them and tested. **Correct call, and the right one
  for measurement too:** three releases in a row with unchanged metadata keeps the keyword index
  stable, so rank position stays readable and the recovery below can be attributed.
- **★ THE RE-INDEX DIAGNOSIS HELD. Organic impressions recovered before any paid traffic started:**
  06.09 **50** → 07.09 **56** → 08.09 **99** → 09.09 **116**. The Search Ads campaign did not begin
  serving until 09.09 19:00, so that climb is organic. The 249→68 collapse was a transient
  re-index, exactly as called on 08.09 — **not a permanent loss from the 1.8.4 subtitle.**
- **★★ THE DOWNLOAD DECLINE REVERSED.** Weekly: 27 → 25 → 20 → 14 → **12** → **21 in five days**
  (week of 07.09, tracking toward ~28). Daily 07–10.09: **7, 6, 5, 3** against 1–3/day the week
  before. **The lift began 07.09, two days BEFORE the ad started** — so ads are not the driver,
  though they may contribute from 10.09.
- **CTR is up too** in the pre-ad window: 08.09 hit **7.1%** (7 page views on 99 impressions), the
  best day in the series, against an August mean of 2.42%.
- **CONSEQUENCE: the 20.09 subtitle revert is off the table** unless something reverses again. The
  case for it rested on impressions never recovering. They recovered. Watch rank position instead,
  as agreed — but the burden of proof has flipped.
- **10.09's 551 impressions are mostly PAID** — the first full ad day. Roughly 435 paid on top of
  ~116 organic, which is consistent with impressions being free under a cost-per-tap model. **Do
  not read 551 as organic recovery**; the honest organic figure is the 116 from 09.09.
- **The quality release is likely the most valuable work of the fortnight and will not show up in
  any funnel we watch for weeks.** Crashes and broken outputs feed reviews and ratings, which feed
  both ranking and conversion. It is a slow input with no dashboard row.
- **Caveats held:** 11.09 reads 0 and is the known partial tail; version bumps add a freshness
  effect on top; the numbers are small. Consistent with, not proof of.

## 10.09.2026 — 1.8.5 shipped with the preview video. Sora fix landed; two items went live unfixed

- **The critical fix is in.** The re-rendered preview (`App-Store-Intro.mp4`, 886×1920 — the other
  valid 6.5" preview size) no longer names **Sora**. Chapter 06 now reads *"Built for your model.
  Veo 3, Runway Gen 4.5, Kling, Seedance — image or video prompt."* Correct list, and it matches
  the app's own Target Platform panel. The false support claim never reached the store.
- **Two items shipped unfixed, both minor, both for the next release:**
  · The four-name list is still the **closed-set construction** banned on 04.08 — it reads as
    "locked to these four" and throws away portability, which is the actual edge. Approved form:
    *"Works with any AI image or video generator — Veo, Runway, Kling, Seedance."*
  · Chapter 04 still reads *"golden hour"* lowercase where the app's own UI shows **Golden Hour**.
- **★ CORRECTED same day — NO metadata was changed in 1.8.5** (user's confirmation). Only the
  preview video was added. **So there is no second re-index** — re-indexing is triggered by
  metadata changes, not by shipping a binary, and a preview carries no indexed keywords. My
  "probably a second re-index" was wrong and would have led to writing off a measurement that is
  partly still readable.
- **What 1.8.5 actually confounds, precisely:**
  · **A "recently updated" freshness bump** — temporary, affects ranking for a few days.
  · **★ The preview autoplays in App Store SEARCH RESULTS, so it changes the tile itself** — which
    is the CTR variable. From here, subtitle and preview are confounded *with each other*. Not
    fatal, but CTR can no longer be attributed to the subtitle alone.
  · **Rank position for the target phrase stays clean**, because the keywords did not move.
- **Revised grading split:** grade the **subtitle on rank position** (uncontaminated), and grade
  **CTR on "the tile as a whole"** rather than on any single field. Search Ads keyword data is
  unaffected by listing churn and remains the cleanest instrument available.
- **Silver lining worth watching:** with metadata unchanged, if organic impressions recover over the
  coming week that *confirms* the 249→68 collapse was the 1.8.4 re-index settling, exactly as
  diagnosed on 08.09. 1.8.5 accidentally provides the control.
- **Still 5 of 10 screenshots** — the cover is not uploaded, so tonight's ad shows the new preview
  against the old screenshot set.
- **Fixed a false positive in `check_video.sh`:** "every time" was on the banned list, but the
  approved promotional text legitimately reads *"Pick the lighting and the camera angle every
  time"*. Narrowed to the outcome-guarantee forms only. A gate that flags approved copy trains
  people to ignore it.

## 09.09.2026 — App Store preview is close, but it names Sora

- **`App Store Intro.mp4` — 28s, 1080×1920, silent, clean app capture with no cursor or window
  chrome.** Structurally this is right: nine numbered chapters (01 DESCRIBE → 09 CONTACT SHEETS),
  inside the 15–30s preview window, at a valid preview resolution. **And "NO WASTED CREDITS" is
  gone** — yesterday's block was actioned.
- **BLOCKED on chapter 05:** *"Built for your model. Veo 3, Runway Gen 4.5, Kling, **Sora** — syntax
  tuned per platform."* Sora has never been in the product. That is a false support claim on the
  App Store listing itself, and **the app's own Target Platform UI in the same shot shows Seedance 2,
  not Sora** — the caption contradicts the screen it captions. The four-name list is also the banned
  closed-set phrasing. Ruling logged in `brand/claims.md` with the approved replacement.
- **Two smaller fixes in the same pass:** chapter 03 says *"golden hour"* lowercase where the app's
  own UI shows **Golden Hour** two frames earlier; the end card says *"LESS WASTED CREDITS"* where
  the allowlist wording is **FEWER**.
- **`./scripts/check_video.sh` found all of it in ~40 seconds**, one day after being written. Two
  rendered assets checked, two blocked — both for claims that would otherwise have shipped as
  pixels. The gate is now carrying its own weight.

## 08.09.2026 — Marketing reel BLOCKED: "NO WASTED CREDITS" burned in again. Pixel gate now exists

- **`Marketing-Prompts-Reel.mp4` (31s, 1080×1920, silent) cannot ship as delivered.** The end card
  carries **"✦ NO WASTED CREDITS"** next to the App Store badge — verbatim the most-banned claim in
  `brand/claims.md`, and the **same claim in the same place** as the 14.08 otter reel. Twice in 25
  days.
- **The 14.08 countermeasure was a sentence asking a human to read rendered frames. It failed on
  its first test.** Replaced with a tool: **`./scripts/check_video.sh <video>`** — one frame per
  second, OCR through Vision (`scripts/ocr_frames.swift`), matched against the banned list, exit 1
  on a hit. Caught this in ~40 seconds and prints every line of on-screen text for eyeballing.
  OCR language correction is off on purpose so garbled AI text is not silently auto-corrected.
- **Second defect, same end card: garbled label text.** `SPARALING REPRESHNENT / NATURALLY
  FLAVOARED` on the soda bottle — in a reel selling shot-ready product photography, on the most-
  viewed frame. The main lockup (MRWOLF / LEMON SODA) renders clean; the small sub-line does not.
- **Flagged, not blocking:** the title card's *"shot-ready in seconds"* compresses the generator
  step out of existence — the app writes the prompt in seconds, the image still takes a generation.
  Same family as the banned "lands first try".
- **Credit where due — the reel is structurally right.** Not the gallery I warned against: a UI
  walkthrough establishing the mechanism, then 14 outputs each labelled ENVIRONMENT / LIGHTING /
  CAMERA ANGLE. **And it never says "style"** — which is the exact per-surface distinction
  `claims.md` has been caught on twice. Whoever cut it got the hard part right.
- **Also noted:** no audio track (fine for Facebook's muted autoplay, weak for TikTok/IG), and 31s
  is over the 30s App Store preview ceiling — though it could not be a preview anyway, being a
  produced edit rather than device capture.

## 08.09.2026 — Session close: Pinterest opened, attribution problem solved on paper

- **Pinterest added as a channel**, business account confirmed under `contact@wolfram-brandhoff.com`
  (the gate for analytics). Setup and 30-day test in `plans/2026-09-08-pinterest-setup.md`;
  20 pins written from existing stills in `packages/2026-09-08-pinterest-batch-1.md`.
- **Why a fifth channel is defensible when four are barely working:** Pinterest is a **search
  surface that links out**, and it reports **outbound clicks** — so for the first time a social
  channel is measurable on something that proxies App Store page views (+0.76) rather than views
  (+0.19). **Measured on outbound clicks only. Signal: 30 in 30 days → keep; under 10 → close.**
- **★ The find of the day is not Pinterest, it is App Store CAMPAIGN LINKS.** A `ct=` token on the
  product URL makes each channel a named row in App Analytics — the same feed `refresh.py` already
  reads. Our entire off-platform history currently reads **"Web referrer: 3 page views, all-time."**
  This closes the hole under every social conclusion this system has drawn since 29.08, **including
  the +0.19 correlation itself.** Generate five: pinterest, facebook, tiktok, youtube, instagram.
- **Board naming caught repeating the App Store mistake.** The existing board is named for what we
  are ("Cinematic Prompts — Prompts for AI image and video") rather than what people search — the
  same error that produced a subtitle aimed at a 1/5-popularity phrase. Boards renamed around search
  phrases; Pinterest indexes board name, board description and pin description, and **does not use
  hashtags** — keywords in the description are what rank.
- **Flagged: the user's App Store link is storefront-locked** (`/de/…?l=en-GB`). Verified
  `https://apps.apple.com/app/id6757644087` redirects each visitor to their own storefront — use
  that as the base for all tagged links.
- **DEFERRED to next session: short links.** Recommendation on the table is redirects on
  `wolfram-brandhoff.com` (`/pin`, `/fb`, `/tt`, `/yt`, `/ig`) rather than a public shortener —
  branded, trusted on Pinterest, and repointable without editing pins. **Must verify the `ct=`
  parameter survives the redirect**; a stripped query string fails silently and would read as
  "Pinterest sent nobody".
- **Held back from Pinterest:** the 9 Prenzlauer Berg night stills — they are the likely subject of
  the Facebook replication and should not be seeded on a second channel before that reports.
- **Gate gap noted:** `brand/registry.json` has no `pinterest` block, so `./check.sh` cannot cover
  the batch. Claims checked by hand. Add the block if the channel survives its 30 days.

### Open items, in priority order

1. **Watch daily organic impressions** — 53–54/day. Waiting for a plateau (3 consecutive days
   within ±25%) to restart the suspended CTR clock. **Revert trigger: still under ~120/day on
   20.09**, measured on organic only with ad impressions subtracted.
2. **Search Ads probe** starts 09.09 19:00, runs to 13.09. Read per-keyword impressions
   Wednesday; three outcomes pre-registered in `plans/2026-09-08-search-ads-probe.md`.
3. **Facebook replication** — waiting on the marketing stills. Caption formula and gate-safe
   hashtags staged; signal clears 200 / under 50. This is the only live experiment that can report
   before the 20.09 decision.
4. **Campaign links** — five of them, before any more content goes out.
5. **Short links** — deferred, see above.
6. **App Store preview video** — screen recording in the works; uploads 21.09 with the cover.
7. **Cover + 5 slides** ready at 1284×2778; frozen until 21.09.
8. **Next release's keyword field** — draft written, targets generator names. Needs a version to
   ship; do not change subtitle, keywords and categories together again.

## 08.09.2026 — Search Ads probe live; Apple's popularity tool answered most of it for free

- **Campaign created** — Search Results, DE/GB/US, Manage Bids at €0.67, €2/day, 09.09 19:00 →
  13.09 21:00 (~€8). One ad group, Search Match OFF, five Exact keywords: `ai prompt generator for
  video` (control), `kling`, `seedance`, `veo`, `gemini`. No negatives — Exact match makes them
  pointless. As-built detail in `plans/2026-09-08-search-ads-probe.md`.
- **★ The probe's main question was answered before it ran, at zero cost.** Apple's keyword
  popularity scores, read off the Add Keywords screen: **`gemini` 5/5, `veo` 4/5, `kling`/
  `seedance`/`runway` 3/5 — and `ai prompt generator for video` 1/5**, along with `prompt
  generator`, `generator`, `prompt`, `image`, `filmmaker`, `marketing`, `ads`, all 1/5.
  **The phrase the entire 1.8.4 subtitle was built around has minimal search volume.**
- **The volume/intent distinction is the durable lesson.** `angle` and `fashion` also score 3/5 but
  the searchers want protractors and clothes — volume without intent. That is exactly August's
  signature (impressions 116→249/day while CTR fell 4.9%→2.42% and install rate 61%→45%).
  **Generator names are the only cells where volume and intent both align.**
- **`Discovery` ad group dropped.** Its question was answered free, and it would have starved
  `Thesis` on a shared €2 cap.
- **Apple's recommendations are a positioning signal in themselves:** capcut, picsart, inshot
  (video editors), grok, meta ai, dola ai (chatbots). **Apple does not classify us as a prompt
  tool.** Relevant to the next release's category choice.
- **Next check 10.09**, with three pre-registered readings — see the plan.

## 08.09.2026 — Phrase test PASSED (indexed, bottom-ranked); Search Ads probe specced

- **The organic phrase check came back: the app IS returned for "AI prompt generator for video"** —
  it was not before. The plan's "clean pass/fail on the whole ASO change" is a **PASS**; the
  subtitle indexed. **But it ranks at the bottom**, which earns almost no impressions and explains
  most of the 249→68/day collapse. Graded in the 1.8.4 plan.
- **The mistake it exposes: we chose the phrase for relevance and never asked if we could win it.**
  Rank follows download velocity on the term; at ~12/week a head phrase is unwinnable. Long-tail is
  the only winnable ground — `kling` and `seedance` are missing from the keyword field while
  `gemini` and `runway` are in it.
- **Revert plan revised: watch RANK, not just impression count.** We never knew what the old
  subtitle ranked for either (Apple exposes no organic search terms), so a revert is a blind swap
  between two unmeasured keyword sets — and 1.8.4 also moved categories, so it would not undo the
  whole change. If anything is reverted, one field at a time.
- **Probe specced and written to `plans/2026-09-08-search-ads-probe.md`** — paste-ready. Advanced,
  US/GB/DE, €2/day for ~5 days (~€10), two ad groups: four exact-match keywords at €0.70 CPT, plus
  a Search Match discovery group at €0.45 whose search-terms report is the real deliverable.
  **Search Ads bills per tap, so impressions — the data we want — are free.** Signals
  pre-registered so the result cannot be rationalised afterwards. Campaign creation is the user's
  to run; it is their ad account and their spend.
- **Recorded the organic baseline before any paid traffic:** 53–54 impressions/day, ~1–2 page
  views/day. The 20.09 revert trigger is measured on organic impressions only, ad impressions
  subtracted.

## 08.09.2026 — Impressions collapsed 73% after 1.8.4; the CTR window is suspended

- **Asked to analyse a download slowdown and whether 1.8.4 has landed. It has not — and it cannot
  be read yet**, but something else showed up that matters more.
- **Search impressions, time-locked to the 03.09 release:** 162 → 176 (release) → 114 → 54 → 53.
  Baseline 249/day, now **68/day**. **Verified real**, not a partial tail: each ONGOING analytics
  instance carries a rolling 3-day window and the values never move after publication. (This
  corrects my 07.09 lesson, which wrongly extended the sales feed's partial-last-day behaviour to
  the analytics feed. Only downloads backfill.)
- **It is a re-index, not a penalty and not better targeting.** The drop is uniform across every
  territory (US −65%, GB −87%, DE −63%, CN −97%) and entirely in search; browse is unchanged. A
  targeting improvement would have spared DE/IN and killed AU/CA/JP.
- **The download decline started before the release.** July→August the app bought volume and lost
  quality: 116→249 imp/day while CTR fell 4.9%→2.42% and the install rate fell 61%→45%. Weekly
  downloads 25 → 20 → 14 → 12. The release then removed the volume too. **Page views are down 55%.**
- **CTR window SUSPENDED** in the 1.8.4 plan. Restart the 14-day clock when impressions plateau
  (3 consecutive days within ±25%). **Revert trigger:** still under ~120 imp/day on 20.09 and
  reverting the subtitle goes on the table.
- **Process lesson logged:** never change subtitle, keywords and categories in one release — this
  dip cannot be attributed to any single field.

## 08.09.2026 — `./run.sh` was not stuck, it was a runaway burning the YouTube quota

- **Reported as "stuck" at "Discovering YouTube (playlist) …".** It was not. `lsof` showed the
  process opening **~6 new HTTPS connections per second** for 12 minutes — several thousand calls
  to the YouTube API with no output. `sample` showed continuous TLS handshakes alongside socket
  reads, which is the tell: a stalled read shows only reads.
- **Cause:** both pagination loops exited solely on `if not token: break`. A playlist that returns a
  repeating `nextPageToken` loops forever, and this one does.
- **The real cost is the quota**, not the wait — 10,000 units/day at 1 unit per call means the day's
  allowance is gone in under 30 minutes, which resurfaces as the logged `quotaExceeded` 403 and an
  empty YouTube history.
- **Fixed** in `scripts/refresh.py`: repeated-token detection plus a 40-page cap, in both
  `youtube_uploads()` and `_uploads_tail()`. Syntax checked.
- **`dashboard/data.js` was never touched** — the script writes only at the end, so nothing was
  corrupted and the 07.09 data stands.
- Diagnostic worth keeping: `ps -o etime,time,%cpu` plus two `lsof -a -i` samples a second apart
  distinguishes a hang from a runaway in about five seconds. Logged in LESSONS.

## 07.09.2026 — Weekly review: Facebook 537, and the plan had written Facebook off

- **The user posted to Facebook on 05.09 with their own caption and got 537 views** — against an
  August median of **4.5**. Best FB post since 27.07. Full grading in `data/performance-log.md`.
- **The "Facebook is suppressed" hypothesis is dead** and the header in LESSONS is retired. A
  throttled account does not return 537.
- **My planning was the failure, and the user said so.** Facebook had been parked as "structurally
  collapsed — needs diagnosis, not content," so the 03.09 package was deliberately Instagram-only.
  New rule in LESSONS: **do not park a channel on an unfinished diagnosis — keep posting to it
  while you diagnose, or the diagnosis never gets tested.**
- **An accidental controlled experiment settled Instagram.** The same asset went to all four
  platforms in one week: **FB 537 · TikTok 243 · IG 3 · YT 2.** Content held constant, 179× gap
  between FB and IG. **Instagram copy experiments: KILL.** The next IG test is account-level or
  there is not one. The 03.09 return-to-form package was never posted, so its stop rule is VOID,
  not graded.
- **Last week's download prediction MISSED** (17–26 predicted, 11 recorded) and landed on the 15
  line that entry named as its own falsification trigger — but 1.8.4 shipped 03.09 inside the same
  window, so the trigger does not fire cleanly. Flag, not reversal.
- **Operational catch:** Apple's final daily row is partial and fills in later (03.09 read 0 on
  04.09, reads 2 today). Trailing 1–2 days must be dropped from every window, **including the
  07.09→20.09 CTR read**.
- **Prediction set:** next FB post, same caption formula, same content type → **clears 200**;
  under 50 → the 537 was a one-off. Downloads are not expected to move and that is not the test.

## 07.09.2026 — "Enhance your prompt" considered and declined for the cover; kept as a keyword

- **User's question:** Runway and Seedance both have an *Enhance* option that improves a prompt the
  way we do, and "Enhance your Prompt" is already on our splash screen — should the cover use it?
- **Checked the source first:** "enhance" appears nowhere in the app UI or the iOS assets. It shows
  up only as an adjective inside generated prompt text. It is splash-graphic wording, not a feature.
- **Declined for the cover.** Their Enhance is a *free button inside the generator the user already
  pays for*; naming ourselves after it invites the comparison we lose, and it describes the
  commodity half of the product rather than the dials. Full reasoning in LESSONS.
- **Kept as a backend App Store keyword** — real search demand from Runway/Seedance users at zero
  positioning cost, and keyword lines are the one place generator-adjacent terms are allowed.
- **Rendered both covers side by side** so the choice was not made blind; they are visually
  equivalent, which is why it turned on positioning rather than looks.
- **Also established: we cannot A/B this.** Product Page Optimization is the right tool and is out
  of reach at 6.6 page views/day — ~4 months to resolve a 10-point swing, ~16 months for 5 points.
  Logged in LESSONS as a second argument for fixing the impression→page-view step first.
- **The measurement window opens today** (07.09 → 20.09). Listing frozen; cover, preview and any
  keyword edit go up 21.09.

## 06.09.2026 — Listing gallery planned: preview video → cover → the 5 feature slides

- **Confirmed the shape the user asked about.** App previews play first in the gallery (up to 3),
  screenshots follow (up to 10). The existing 5 numbered slides become 2–6, so the set uses 6 of 10.
  **What matters: in SEARCH RESULTS Apple shows the autoplaying preview or the first screenshots** —
  so the video and the cover are the two assets doing the work at the 4.62% impression→page-view
  step. They are not decoration; they are the lever.
- **The proposed cover slogan was blocked and rewritten** — ruling logged in `brand/claims.md`.
  It listed Style + Lighting + Camera Angle + Environment as one set over a *Fashion* image, where
  Style does not exist and Environment is random. Only lighting and camera angle are universal.
  Shipped instead: **"Fewer wasted credits / Pick the light. Pick the angle. / We write the prompt.
  870 setups across cinema and marketing."** Checked legible at search-result thumbnail size.
- **Cover built at the real 6.5" size (1242×2688)**, `~/Desktop/cover.html` → renders through
  headless Chrome; drops in `cover-source.png` automatically when the photo lands. Same type system
  as the video's title card, so the listing reads as one campaign.
- **★ The supplied image had a Gemini watermark on it.** `Marketing-Examples/Reels-August/
  Diverse-Set-Change/Stills/fashion.png` carried Google's four-point sparkle in the lower right —
  a third-party generator's mark, which does not belong on our own listing. Removed by cropping the
  bottom 12% (delogo and a texture patch both left a visible rectangle on the flat concrete).
  Logged in LESSONS as a standing check on every generated still.
- **Resolution handled, not ignored.** Source is 768×1376 against a 1242×2688 slot. Rather than a
  1.95× stretch to full-bleed, the photo sits at native width across the top 73% (1.62× lanczos
  upscale with a light unsharp) and the type sits on solid ground below it. **Re-export the still
  larger when possible** — this is mitigation, not a fix.
- **Cover rendered:** `~/Desktop/cinematic-prompts-cover.png`. Verified legible at search-result
  thumbnail size; the red dress reads as a strong colour block at that scale, which is the job.
- **v2 same day — the user re-exported at 1536×2752**, so the cover is now full-bleed at
  1242×2688 with no meaningful resampling (crop the watermark, 1.09× lanczos, centre crop). The
  scrim was softened so the dress stays visible behind the type instead of dissolving into flat
  black. **The watermark sits lower than first measured** — cropping to y<2440 of the upscale is
  what actually clears it; a 2600 crop left it in frame.
- **v3 — the user's copy call, and it is the better one.** Headline is now **"WRITE BETTER
  PROMPTS"** with **"Fewer wasted credits."** under it. Reasoning (user's): it makes clear the app
  generates *text*, not the photograph. That is the same overclaim-by-implication the attribution
  line addresses, solved higher up and more visibly — the biggest words on the cover now name the
  actual output. It also reads better at thumbnail size than the previous two-sentence headline,
  which is the only test that matters for the search-result tile. The dials survive as a small
  third line ("Pick the light and the camera angle. 870 setups across cinema and marketing.").
  Corrected "less" → **"Fewer"** wasted credits, per the allowlist.
- **v5 — rebuilt in the existing deck's language.** Found the real set at
  `Marketing-Examples/Cinematic Prompts/Appstore /Finals/1-8-2-{One..Five}.jpg` and sampled it
  rather than eyeballing: background **#4d4d59** flat, badge amber **#fbbf23**, card box x117–1176
  with a light hairline over #111924, headline from y≈164 in **sentence case**, headline ~110px.
  The cover now uses all of that, with the photo in the same rounded card the phone mockups sit in.
  **Answered the open question: all five slides are already 1284×2778**, so the set uploads together.
- **One deliberate departure:** the cover headline is 152px against the deck's ~110px. At the
  132px search-result tile, 110px lands around 11px and stops being readable — the cover is the
  tile, so it gets the larger type. **The same problem applies to slides 1–5**, whose headlines are
  at 110px; worth rebuilding them louder in Affinity before the 21.09 upload.
- **Typeface is a near-match, not exact.** The deck's humanist sans could not be recovered from
  `iphone.af` (compressed) and is not in `~/Library/Fonts`; the cover uses Avenir Next as the
  closest available. One-line swap once the name is known.
- **v4 — user's correction: "these are App Store miniatures, not social."** Right, and it was the
  wrong frame to design in. Subject re-cropped ~290px higher so the face and the red block sit in
  the top half; headline up from 142px to **196px** across three lines; support line 62px → 84px;
  the dial line dropped entirely (unreadable at tile size, and slides 2–6 already teach it).
  **Verified at 132px — the real search-result width** — where headline and support line both hold.
  Sizing rules logged in LESSONS.
- **Format moved to 1284×2778** (Apple's 6.5" alternative), rebuilt from the upscale with no
  meaningful resampling. **All screenshots in one set must share a size** — the existing 5 slides
  need to be 1284×2778 too, or they will not upload alongside this.
- **Attribution added at the user's request: "Image generated with Nano Banana — from a prompt
  written in this app."** Ruling logged in `brand/claims.md`: naming a generator as ATTRIBUTION on
  a store asset is allowed and arguably required, because the app writes prompts and does not
  generate images — an uncredited photo implies otherwise. What stays banned is naming generators
  as a closed supported set in caption copy, and carrying their watermark.
- **Both the cover and the preview are inside the freeze** (07.09 → 20.09) because screenshot 1 is
  part of the search-result tile. Build now, upload 21.09.2026.

## 06.09.2026 — The screen recording can't be the App Store preview; cut it into a social asset instead

- **User supplied `screen-recording.mov`** (18.35s, 1166×2118, 60fps, no audio) and asked for an
  intro. It cannot become the App Store preview, for three reasons — the first two fatal:
  · **Not device capture.** A macOS arrow pointer and a windowed title bar are visible throughout.
    Apple requires an iPhone preview to be captured on device; this is a windowed desktop capture.
  · **It's a scroll-through, not a demo.** Nothing is used — no prompt typed, no style chosen, no
    Generate pressed, no output shown. That is the variety/showcase content type LESSONS bands at
    255–303 against 784–859 for single-subject demos, and it is the weakest possible thing at the
    impression step, muted.
  · **Generator names are burned into the pixels** (Target Platform, ~5.5s–8.8s). New LESSONS rule:
    the app's own UI contains a banned claim, so any full-screen recording ships one for free.
- **Built instead: a 13.4s social cut** (`~/Desktop/cinematic-prompts-social-cut.mp4`, 1080×1920,
  30fps). Intro card designed in HTML/CSS and rendered at full size through headless Chrome — the
  ground is the app's own Cinematic Contact Sheet, blurred, with a Golden Hour key light from the
  lower left. Hook: **"STOP REWRITING PROMPTS / TO FIX THE LIGHTING"**, which is Instagram's #3
  post of all time (272) and the one hook shape proven on TikTok, IG and FB simultaneously.
  The edit crops the title bar out, cuts the generator block entirely, slows the
  lighting-and-camera-angle stretch 1.85× so the money shot lingers, and drops the static tail.
- **The App Store preview still needs a fresh iPhone capture** of the actual use flow. Shoot it
  now, upload **after 09-20** — the listing is frozen 09-07 → 09-20 for the subtitle measurement.
- **Not yet gated:** the cut has no caption package, so `./check.sh` has not run on it. It is an
  asset, not a shippable post, until that exists.

## 04.09.2026 — The funnel numbers were wrong. Fixed, and they point somewhere else entirely

- **The three numbers on the dashboard — "Impressions 0 · 686 page views · 56.0%" — were all
  wrong.** The zero was the tell: page views cannot exist without impressions. Three bugs in
  `appstore_analytics()`, all fixed today (detail in LESSONS):
  · the parser read Apple's `Engagement Type` column instead of its `Event` column, which dropped
    every impression and counted every product-page `Tap` as a page view;
  · it summed `Standard` + `Detailed` + `Web Preview` across two overlapping report requests,
    multiplying whatever survived — now one report, merged per date with **max, never sum**;
  · `index.html` divided **all-time** downloads by a **119-day** page-view window and printed 56%.
- **The real funnel, 16.01.2026 → 02.09.2026 (230 days): 17,981 impressions → 836 product page
  views (4.65%) → 384 downloads (45.9%).** `data.js` and the dashboard now carry these, and the
  funnel section prints its own date range so a window mismatch can't hide again.
- **This flips the priority.** The product page is not the bottleneck — it converts 40–67% every
  single month. **95% of the loss is in the search result**, before anyone reaches the page. At
  August's volume each **+1 point of CTR ≈ +73 page views ≈ +33 downloads/month**, which is larger
  than anything nine weeks of caption work produced.
- **Impressions are growing without help:** 116/day (July) → 236/day (August). Downloads per 1,000
  impressions fell 30.2 → 12.6 over the same period. The reach is arriving and the tile wastes it.
- **The app preview video stops being optional.** It autoplays muted in App Store *search results* —
  at the impression step, i.e. the step losing 95%. It has been open-item #4, "not blocking", since
  08-30. It is now the highest-value unshipped asset in the system.
- **New leading indicator: product page views per day.** It tracks daily downloads at **+0.76**
  (n=230) against **+0.19** for social views — earlier signal, 2–3× the sample size.
- **A third grading test added to the 1.8.4 plan.** Baseline to beat: August's **2.8% CTR / 6.6 page
  views per day**; pass is a 14-day CTR clearing 4.5%. Graded on a fixed top-5 territory set and
  split by Source Type, because August's aggregate CTR drop is partly mix (AU 0.3%, CA 0.9%,
  JP 0.9%, IT 0.8% against IN 4.9%, DE 17.0%) and because the category move to Grafik und Design +
  Foto und Video changes browse impressions, which convert at 1.86% against search's 4.64%.
- **Not changed:** the download-week test (clears 35, must survive into week two) still stands. The
  CTR test is more sensitive, not a replacement.

## 03.09.2026 — 1.8.4 PUBLISHED. Clocks started, ad scheduled, Instagram back to the 717 shape

- **1.8.4 is live** (manual release clicked today). The subtitle drafted 08-13 —
  `AI Prompt Generator for Video` — is finally on the store after three weeks of it being written
  and never shipped, plus a day of my own wrong advice that it was locked.
- **Schedule agreed with the user, and the user's sequencing beat mine.** I wanted the €5 Search
  Ads probe delayed two weeks so it could not contaminate the download measurement. Wrong: the
  week *of* release is already discarded because of Apple's "recently updated" bump, so a probe
  inside it costs nothing and buys the keyword data a fortnight earlier. **Rule kept: put cheap,
  repeatable tests inside already-confounded windows; protect the expensive one-shot measurement.**
  · Fri 09-04 → Sun 09-06: €5 probe, Advanced, €1–2/day, 4 exact-match keywords
  · Sat 09-05 / Sun 09-06: search "AI prompt generator for video" — the organic pass/fail
  · Mon 09-07 → Sun 09-13: the graded download week (clears 35 → the lever is real)
  · Week of 09-14: the gain must survive the update bump to count
- **Account decisions from the user: keep all four accounts, no double posting.** The seven
  duplicate Facebook uploads since July 1 stop here.
- **The user made the sharpest content point of the cycle:** Instagram hit 717 / 301 / 272 earlier
  this year and now sits at 6–15, and that peak was this system working. Checked it — all three
  were pain-first direct statements on a single subject, and the 717's coastal subject is the same
  one behind TikTok's 805. What replaced them was variety reels and narrative-title reposts, which
  the bands cap at 255–303 on TikTok and single digits on IG.
- **New package: `packages/2026-09-03-instagram-return-to-form.md`. Gate CLEAR, exit 0.**
  Deliberately Instagram-only — re-running the exact shape that produced the 717 with one variable
  changed (content type back to single-subject pain-first), not four platforms at once.
  **Signal: clears 60 → content type was the problem; under 25 → the next test is account-level
  (reach, Page-vs-profile), not copy.** August median 12, best 38, last two posts 9 and 9.
- **Views and downloads are both down, stated plainly by the user and not disputed here.** Nine
  weeks of caption work moved neither, which is the whole reason effort moved to the App Store.

## 02.09.2026 — Session close

- **Dashboard protocol updated** — three entries added (1.8.4 submitted, Analytics enabled,
  the Facebook suppression finding). Verified rendering: 37 entries, newest three at top,
  no console errors.
- **Date correction:** I dated this session's entries 31.08.2026 throughout. Today is
  **02.09.2026**. Corrected across PROTOKOLL, LESSONS, claims.md, data-sources.md, the 1.8.4
  plan and index.html (22 replacements). The Aug-31 datapoint in `data.js` is a real Apple
  download figure and was deliberately left alone. This mattered because the review timeline
  is graded off these dates.

### ✅ RESOLVED same session — `dashboard/CLAUDE.md` deleted (user approved)

A second CLAUDE.md existed at `dashboard/CLAUDE.md` — an OLD copy of the root instructions, loaded
by any session working inside `dashboard/`. It instructed the agent to make **three separately
banned claims**:

- *"No guessing, no wasted credits"* — the single most-corrected claim in this project's history
- *"prompts that land the first time"* — banned; no first-try guarantee is truthful
- *"golden hour, blue hour, harsh noon, overcast"* — *harsh noon* and *overcast* do not exist in
  the app, and *golden hour* must be capitalised

It also predates camera angles (v1.8), the ship gate, `LESSONS.md`, `brand/claims.md`, and it
points at the frozen legacy CSV as if it were live. **This was a live source of exactly the
regression the claims allowlist exists to prevent** — an agent working in `dashboard/` would have
been *instructed* to write the banned claims, and would have had no reason to doubt it.
**Deleted 02.09.2026 with the user's approval** (`git rm`; tracked, so recoverable with
`git checkout be72d5e -- dashboard/CLAUDE.md` if ever needed). `./CLAUDE.md` at the repo root is
now the only instruction file, confirmed by a repo-wide search.

**The general rule this establishes:** a nested CLAUDE.md is a silent fork of the instructions.
It does not announce itself, it overrides by proximity, and it ages badly — this one still
described a v1.7 product. **Keep exactly one CLAUDE.md, at the root.** If a stray one ever
appears, treat it as a claims risk, not a housekeeping detail.

### Open items, in priority order

1. **Meta Account Status** — request sent; read the answer on both FB and IG.
2. **~48h after 1.8.4 goes live** (release is *manuell* — it does not ship until clicked):
   search the App Store for "AI prompt generator for video". Appearing = the subtitle worked.
3. **Run `./run.sh`** once Apple produces the first analytics instance; fix the CSV column
   mapping against real data, then read the summer's real conversion history.
4. **App preview video** — 0 of 3, and it autoplays muted in App Store *search results*, so it
   works at the impression step. Needs a fresh screen recording (the reels cannot be reused).
5. **`refresh.py`: carry last-known-good views forward when a YouTube video goes private**
   (see LESSONS) — today it writes null and the history is lost.
6. Downloads graded on the first FULL week after release, not the week of. Clears 35 → the
   App Store lever is real. Must survive into week two to beat Apple's update bump.

## 02.09.2026 — 1.8.4 submission-ready: every field verified, both localisations, build 2

- **Final state, all verified against Apple's own counters rather than by eye**, in BOTH
  Englisch (Kanada) (primary) and Englisch (USA): Untertitel 1 · Name 13 · Schlüsselwörter 2 ·
  Werbetexte 3 · Beschreibung 2.664 · Neues in dieser Version 3.756.
- **The subtitle shipped.** `AI Prompt Generator for Video` — the fix drafted 08-13, never
  shipped, and wrongly believed locked earlier today. The fallback keyword compromise is void;
  the 98/100 line is in, which does not waste characters duplicating the subtitle.
- **Categories swapped** from Produktivität → **Grafik und Design** (primary) + **Foto und
  Video**. Productivity was an unwinnable category and contradicted the positioning.
- **Age rating: 4+ held across 172 countries**, which is the proof the new social-media
  questionnaire was answered correctly (all six rows Nein).
- **Google Fonts removed from the app itself** — 7 self-hosted WOFF2, no third-party request at
  launch, 176 KB, no visual change. This made three existing claims true rather than nearly
  true: the privacy policy's "completely private and offline", "never leaves your device", and
  the listing's "100% on-device". Also removed the GDPR exposure (LG München I, Az. 3 O
  17493/20) that applies to a German developer shipping into the EU.
- **Build 2 selected** (the post-font-fix upload). `ITSAppUsesNonExemptEncryption = false` is
  already in Info.plist, so export compliance resolves without a prompt.
- **Still unclaimed, none blocking:** 0 of 3 App-Vorschauen, 5 of 10 screenshots, empty
  Marketing-URL. The preview is the real one — it autoplays muted in App Store SEARCH RESULTS,
  so it works at the impression step, not just on the product page. It can be added to the live
  listing without a new build.

## 02.09.2026 — App Store funnel added to the dashboard

- **New section between the hero and Key metrics: impressions → product page views → downloads**,
  with the conversion rate on each step. Rates under 3% (impression→view) and 25% (view→install)
  render in rose, so a weak step reads as weak instead of needing arithmetic.
- **Why this shape:** it splits the two failure modes the system has been unable to tell apart.
  A weak FIRST step is an ASO problem (subtitle/keywords — what 1.8.4 changes). A weak SECOND
  step is a product-page problem (screenshots, the missing app preview, description). Until now
  the only App Store number on the dashboard was a single download total, which cannot
  distinguish them.
- **`refresh.py` now calls `appstore_analytics()`** against the Analytics Reports API, with the
  two guards this codebase has needed before: it never raises into `main()`, and it returns `{}`
  rather than zeros when a fetch fails — so a failed pull cannot masquerade as "no impressions".
  An empty pull keeps the previous funnel rather than blanking the section.
- **Verified in the browser**, both states: pending renders em-dashes plus a "Waiting for Apple"
  note (this is the correct state today, not an error), and populated renders the numbers with
  colour-coded rates. Checked at desktop and 375px; no console errors.
- **NOT yet verified: the CSV column mapping.** Apple's analytics column names drift between
  report versions, so `_pick_col()` matches on substrings, and if a real instance parses to zero
  rows the run prints the columns it actually saw instead of failing silently. That mapping gets
  confirmed against real data when the first instance lands.

## 02.09.2026 — Analytics Reports API finally enabled; release unblocked

- **The measurement gap flagged on 08-29 as "the single highest-value change available" is
  closed.** `ONGOING` = `d2fcc92e-c855-4827-bce2-140dcf5ea674`, `ONE_TIME_SNAPSHOT` (≈1y history)
  = `56dfb2b7-94bd-4ae3-944a-4e8266471c24`. Written up in `data-sources.md` with the read path.
- **Why it was never found:** there is no toggle in the App Store Connect UI. The feed is
  request-driven — you POST an `analyticsReportRequest` and Apple starts generating dailies. The
  system had been looking for a setting that does not exist. New script:
  `scripts/enable_analytics.py` (read-only by default, `--create --snapshot` to arm).
- **Two of my own bugs, both caught by running it rather than reasoning about it:** I sent a
  `name` attribute that Apple rejects 409 (`accessType` is the only writable one), and the script
  printed "Done" after both calls had failed. The second is the worse bug — a false success on a
  measurement tool is how the YouTube-Private and Facebook-double-fire failures survived for
  weeks. Now exits non-zero with NOTHING WAS CREATED.
- **The snapshot is the interesting one.** ~1y of impressions / product page views / conversion
  arrives within ~24–48h, which tests the assumption the entire 1.8.4 push rests on: that App
  Store discovery has been flat all summer. That has never been checked, only inferred from a
  download total sitting in an 18–30 band.
- **Release unblocked.** The precondition set earlier today ("wire the measurement before, not
  after") is met.

## 02.09.2026 — The account-health finding, and why it does NOT transfer to the App Store

- **User challenged the whole system: "the agent has throttled all 4 accounts — how do I know the
  App Store changes won't do the same?"** Checked it rather than defended it. The challenge is
  substantially correct on the social side and does not apply on the App Store side. Full finding
  in LESSONS; summary: FB main account July median **164.5** → August **4.0**, while a second
  accidental account under the same name, posting the same content, medians **~229**. Content is
  held constant, so content is not the variable.
- **Probable cause is our own operational bug, not our copy.** `data.js` holds **7 duplicate
  uploads since July 1** on Facebook, second upload losing every time. The double-fire was logged
  4× as an operational annoyance and never as a distribution risk. That was a misclassification.
- **Not proven.** New-account cold-start boost explains part of any such gap for ~2–3 weeks. The
  two separating tests are written into LESSONS: read Meta Account Status directly, and run the
  same asset on both accounts the same day.
- **The App Store answer, and it is not "don't worry":** the failure mode does not exist there —
  no engagement-velocity loop, no account-level spam suppression, metadata is static rather than
  a stream. The genuine analog is the **conversion-rate feedback loop** (wrong-intent traffic →
  lower tap-to-install → lower ranking), plus normal re-indexing volatility after a subtitle
  change. **We currently cannot see that loop, because the App Store Connect Analytics Reports
  API is still not wired up** — flagged as the highest-value measurement work on 08-29 and still
  outstanding. So the honest answer to "how do I know" is: not until that is on. Making it a
  precondition of the release rather than a follow-up.
- **Release call: ship 1.8.4 anyway.** App Store metadata is reversible — promo text without a
  build, subtitle/keywords with the next version — where account suppression is not. The risk is
  different in kind and cheaper to undo.

## 02.09.2026 (third check) — Two localisations, and the PRIMARY one is still on the old copy

- **The language dropdown, opened, shows the actual problem:** *Englisch (Kanada)* — **Primär** —
  and *Englisch (USA)*, currently ticked. All the verified metadata went into **USA only**.
  Apple serves the **primary** localisation to every storefront without its own, so the US page
  is correct and the rest of the world is still on the 1.8.3 listing. Fixing the language picker
  last round solved half the problem and looked like it solved all of it.
- **Action: paste all five fields into Englisch (Kanada) as well** — subtitle, keywords,
  promotional text, description, What's New. Recommended over switching the primary language,
  which Apple restricts and which would be a larger change than this release needs.
- **Logged as a durable rule in LESSONS.md**, because both localisations look identical on the
  form until the dropdown is opened — this will silently recur on every future release.
- **Unchanged and still verified on the USA localisation:** Werbetexte 3 remaining, Beschreibung
  2,671 remaining (1,329), Neues in dieser Version 3,756 remaining (244), *Anmeldung
  erforderlich* unticked. Keywords still the fallback line; the subtitle state is still unknown
  and is now a two-localisation question.
- **Still blocking:** no build, and the age-rating questions due 7 Sept 2026.

## 02.09.2026 (second check) — Metadata verified byte-exact; only the keyword decision is open

- **All three copy fields now match the plan, confirmed by Apple's own counters, not by eye:**
  Werbetexte **3 remaining** (167/170), Beschreibung **2,671 remaining** (= exactly 1,329),
  Neues in dieser Version **3,756 remaining** (= exactly 244). The description and What's New
  rewrites both landed — "870 prompt combinations", and style scoped to cinema in both places.
- **Fixed since the first check:** metadata language now reads **Englisch (USA)** (was Englisch
  (Kanada) — that would have put the whole ASO push on the wrong storefront), and *Anmeldung
  erforderlich* is unticked, so App-Prüfung no longer contradicts "No account" in the listing.
  Screenshots are inherited from the EN-CA set, which is normal and needs no action.
- **One decision still open: the keyword field still holds the FALLBACK line** (`video,generator,
  …,kling`, 100/100). That is only correct if the subtitle was NOT changed. Subtitle lives on
  App-Informationen and is not visible on this screen, so it can't be verified from the form.
  If the subtitle now reads "AI Prompt Generator for Video", *video* and *generator* are being
  paid for twice and the field must be swapped to the 98/100 line.
- **Still blocking submission:** no build uploaded, and the social-media age-rating questions are
  due **7 Sept 2026**. *Zur Prüfung hinzufügen* has gone blue because the metadata is complete,
  not because the version is submittable.
- **Unclaimed:** 0 of 3 App-Vorschauen, Marketing-URL empty, 5 of 10 screenshots.

## 02.09.2026 (App Store Connect check) — Fields verified; subtitle was never locked

- **Checked the live 1.8.4 form against the plan.** Promotional text and keywords are in
  correctly and both counters confirm it: Werbetexte shows **3 remaining** (167/170) and
  Schlüsselwörter shows **0 remaining** (100/100). Description body, version and copyright match.
- **★ The subtitle is not locked — I gave the wrong location.** It is not on the version page
  (correctly absent from the screen showing Werbetexte/Beschreibung/Schlüsselwörter); it sits
  under **Allgemein → App-Informationen**. 1.8.4 is *In Vorbereitung zur Übermittlung* with no
  build uploaded, so nothing is frozen by review. The whole fallback keyword compromise was
  built on my bad advice. Plan corrected.
- **Two copy landmines still in the form**, both the same universal-dial error: What's New said
  the style/lighting/angle are "all yours to choose" across film *and* commercial work, and the
  description opener still read "870 setups". Both rewritten in the plan.
- **Flagged for the user to verify, not assertions:** the metadata language selector reads
  **Englisch (Kanada)** — if English (U.S.) is the primary localisation, these edits are landing
  on the wrong storefront. And App-Prüfung has *Anmeldung erforderlich* ticked with demo
  credentials while the description promises "No account."
- **Blocking submission regardless:** no build uploaded, and the new social-media age-rating
  questions are due **7 Sept 2026**.
- **Unused lever: 0 of 3 App-Vorschauen.** A year of social video exists on disk and none of it
  is on the product page; only the first 3 screenshots appear on install sheets.

## 02.09.2026 (later) — Second pass on the promo text; the dial rule generalised

- **User's next draft ran 204/170 — over Apple's limit by 34 characters.** It also swapped the
  style misattribution for an environment one: *"pick the lighting, environment and the camera
  angle on every shot"* is false for Cinema (no environment dial at all) and for Fashion (the
  backdrop is `pick(FASHION_ENVIRONMENTS)`, random). True of 480 of 870, not all.
- **Same error class caught twice in two days on the same field**, so the rule got generalised
  rather than patched again: `brand/claims.md` now carries a **per-surface dial table**. Only
  **lighting and camera angle** are universal; style = 360, environment = 480. Nothing else may
  be attached to the 870 figure without scoping.
- **Also fixed a taxonomy error:** the draft said "cinema, marketing, product and fashion."
  Marketing Prompts is the *parent* of Ads + Product + Fashion, so that lists a parent beside
  two of its children and drops Cinematic Ads — a 240-combination surface — entirely. Ruling
  added to claims.md: the correct short form is "cinema, ads, product and fashion."
- **Kept from the draft: the wasted-credits pain.** It is selling point #1 and it was absent
  from the field. Corrected to **"fewer"** wasted credits (count noun; claims.md's sanctioned
  wording) and cut "better results" as unverifiable filler.
- **Shipping line, 167/170:** `870 prompt combinations for cinema, ads, product and fashion.
  Pick the lighting and the camera angle every time. Less guessing, fewer wasted credits. Free,
  no account.` The environment-forward cut is parked in the plan as the two-week A/B variant.

## 02.09.2026 — Promo text revised: "prompt combinations", and the style dial scoped to cinema

- **User proposed "870 prompt combinations" in place of "870 setups." Adopted.** *Setup* means
  camera position in film vocabulary — wrong sense for a prompt app — and "prompt combinations"
  names what the number counts while putting the category word in the first visible line of the
  product page. Promo text isn't indexed by Apple, so this is conversion copy, not ASO; the word
  earns its place on clarity alone.
- **Caught while checking it: the style dial was attached to all 870.** Style is cinema-only
  (12 × 5 × 6 = 360); the other 510 run lighting × angle × environment. `brand/claims.md` bans
  the numeric form of that misattribution — this was the same error in loose phrasing, and it
  had been sitting in the locked FINAL block since 08-30. New ruling added to claims.md: light
  and angle apply everywhere, style gets scoped.
- **Shipping line, 154/170:** `870 prompt combinations across cinema, ads, product and fashion.
  Pick the light and the camera angle on every shot, the style on cinema. Free, no account.`
  Updated in `plans/2026-08-30-appstore-1.8.4-launch.md`. No other FINAL field touched.
- No banned phrase, no competitor comparison, no generator name, real lighting vocabulary.

## 23.08.2026 — TikTok 255: the prediction missed and the framing rule got revised

- **The Set Change reel went out on TikTok Fri 08-22 evening: 255 views.** My written stop rule
  was "clear 600, kill under 350". 255 fired the kill condition. Graded MISS in
  `data/performance-log.md`. Running score: **2 HIT, 1 MISS.**
- **Revised the framing rule rather than defending it.** On 08-21 I promoted "product-pain
  framing beats showcase framing, 3.5×" to a default rule off a single pair (230 vs 805). The
  very next post used the same framing and landed 255 — 3.2× below 805. So framing alone was
  never the driver. LESSONS now says: **content type sets the band, framing moves you within
  it.** Single-subject demo + pain hook 784–859; variety/showcase 255–303 (one outlier, 768).
  The 805 is better explained by the coastal otter *subject* — the same subject behind
  Instagram's best-ever 717.
- **Remaining schedule for this package** (user's dates): Instagram **Tue 08-25 19:00**,
  YouTube **Wed 08-26 19:00**. Facebook still deliberately unwritten.
- **YouTube slot moved 16:30 → 19:00 CEST, user's call**, to reach North America. Logged as a
  test because it runs against my (weak) bucket data: 15–19 CEST median 192 n=12 vs 19–24
  median 90 n=18. Also worth knowing — 19:00 CEST is 13:00 ET / 10:00 PT, i.e. NA *lunchtime*;
  US prime time would be 01:00–03:00 CEST. **Signal: clears 120 → adopt 19:00; under 40 →
  revert to ~16:30.**
- **Fixed: a YouTube 403 was killing the whole refresh.** `quotaExceeded` raised straight out of
  `fetch_youtube` through `main()`, so Meta, App Store and TikTok never ran and `data.js` was
  never written. Now returns `{}` with the reason Google actually gave. Subtler half: when
  discovery succeeds but stats fail, `main()` hands over an **empty** list rather than 49 rows
  of `views=None` — null rows would read as a successful pull and overwrite real history.
  Verified live against the ongoing 403; YouTube kept all 49 rows and was flagged STALE.
  **57 tests.**
- **The quota itself is unexplained.** A full run costs ~10 units against 10,000/day, the key
  isn't embedded in the app source or used anywhere else on disk, and the quota was already
  exhausted ~2h after the midnight-Pacific reset. That pattern points at the project's quota
  *allocation* rather than real usage — check Google Cloud Console → APIs & Services → YouTube
  Data API v3 → Quotas. YouTube numbers are frozen at last-known-good until it returns.

### Session close — the week ahead

**The Set Change reel across all four platforms, all at 19:00 CEST:**

| Platform | When | State |
|---|---|---|
| TikTok | Sat 22.08.2026 | **POSTED — 255** (prediction MISSED, kill rule fired) |
| Instagram | Tue 25.08.2026 | pending |
| YouTube | Wed 26.08.2026 | pending — set **Public**; also the 19:00-vs-16:30 hour test |
| Facebook | Thu 27.08.2026 | pending — YouTube description verbatim, no tuning, **post once** |

**Review: Saturday 29.08.2026.** Three things resolve by then, each with its number already
written down so the answer can't be argued after the fact:

1. **Instagram** — its band is 11–38, best August post 35. This one is grounded on that exact
   35 ("No separate tool for film, product, or fashion") and the reel *is* that caption's
   subject. Anything under ~20 means the grounding didn't transfer and IG needs a different
   lever entirely, not another caption.
2. **YouTube hour test** — **clears 120 → adopt 19:00 as default; under 40 → revert to ~16:30.**
   Confounded by the quota outage if it persists (views can't be read while YouTube is stale).
3. **CTA / downloads experiment** — **clears 30 in the week of Aug 24 → keep privacy in the CTA
   permanently; under 22 → privacy isn't the lever, move the test to the App Store page.**
   Baseline: 25 / 21 / 29 / 19 over the last four weeks.

**What I'd expect, on the record so Saturday can grade it:** Instagram lands **15–40** (its
structural band; the grounding is good but IG reach hasn't moved all year), and downloads land
**20–28** — i.e. the privacy CTA probably does *not* clear 30 on its own, because a 255-view
TikTok week gives it much less traffic to convert than the 805 week did, and even that week
produced only 19.

**The strategic read going into Saturday:** variety content caps around 300 on TikTok regardless
of caption. The next reel should hold pain framing constant and change subject back to a single
scene — the transformation concept in `plans/2026-08-14-next-reel-concepts.md` (2 generations,
grounded 1987/845) is the cheapest test of that.

**Still unresolved and worth a minute on Saturday:** whether the otter reel was ever re-rendered.
If it shipped with the original end card, the banned "NO WASTED CREDITS" claim is live on four
platforms and has been for over a week.

## 22.08.2026 — Refresh hung on a stalled socket; timeout added

- **`./run.sh` hung, it didn't fail.** The traceback was a `KeyboardInterrupt` mid-SSL-read:
  `refresh.py` set **no timeout on any request**, so urllib blocked forever on a stalled TLS
  read. Ctrl+C was the only way out, and that loses the whole pull.
- **Fixed:** `socket.setdefaulttimeout(45)` covers every `urlopen` in the file (override via
  `REFRESH_TIMEOUT` in `.env`). A timeout now raises like any other error, so the per-source
  staleness guard keeps last-known-good rows instead of wiping them. Two tests pin it — **52
  passing**.
- **The API itself was fine** — a direct call answered in 0.4s. The re-run completed (exit 0)
  but took **13m20s at 1% CPU**: almost entirely network wait, not a hang. The App Store part
  only re-fetches ~16 days (416 cached), so the bulk is **Meta's per-post insight calls** —
  49 IG + 44 FB posts, several metrics each, all sequential. If that slowness recurs, the fix
  is caching post insights the way App Store daily reports already are; older posts' counts
  barely move, so re-querying all 93 every run is mostly waste. Not done yet — it was a slow
  network, not a code regression.
- **Numbers after the pull:** YouTube **49** (up from 45 — the playlist reached further this
  run), Instagram 49, Facebook 44, TikTok **42**, downloads **359** (355 → 359). Nothing stale.
- Note on this log: the pre-2026-08-13 history lives in `archive/2026-08-13/PROTOKOLL.md`
  (continuous June → 10.08.2026, 29 dated entries). The live file restarted on 08-13 **by
  design** — the old ledger had accumulated corrections-on-corrections that were themselves
  causing repeat mistakes. It is not missing; it is archived.

## 21.08.2026 — All four sources live; framing win confirmed; next package built

**The week's result: the framing change worked.** The sea-otter package hit **805 on TikTok**
(Aug 17) — 3.1× the August average of 262. Both predictions HIT (TikTok "clear 500", Instagram
"flat 10-25" → 11). The controlled comparison is clean: two nature posts five days apart, same
channel, differing only in caption frame — wildlife-as-subject 230 vs product-pain **805**.
Promoted from experiment to a default rule in LESSONS.

**But the KPI didn't move, and that's the finding that matters.** The 805-view week produced
**19 downloads — the lowest of the last four weeks** (25 / 21 / 29 / 19). Views tripled, installs
fell. Getting views on TikTok is now solved; converting them is not. Next package therefore
tests the CTA, not the hook.

**All four sources live for the first time.** A long credential fight, most of it self-inflicted:
- Meta died twice — first a password change (code 190/460), then an expired short-lived token
  (190/463). Added `scripts/meta_token.py` + a CREDENTIALS section; **use the PAGE token**, it
  doesn't expire. `refresh.py` only understood user tokens, so following that advice broke it
  (`/me/accounts` doesn't exist on a Page) — now handles both.
- **TikTok was broken by my own commit.** Moving credentials out of the source into `.env`
  silently switched apps: `.env` held `sbawa5c7mkdgoxox43` (the Lovable upload app), not the
  working `sbaw38iz0q3h0sm8ga`. Six rounds of console reconfiguration chased the wrong app. The
  user's "this worked before the deploy" was right; I twice concluded otherwise. Restored.
- YouTube recovered 35→45 videos via the uploads-playlist fallback.

**Bugs found and fixed:** a dead guardrail (`#aiproductphotography`'s commerce check scanned the
hashtag line, and the tag contains "product", so it always passed itself); the partial-failure
data wipe; the YouTube playlist truncation hiding the *recent* tail; `refresh.py` discarding
publish timestamps, which made all posting-time advice unevidenced.

**Repo work:** `git init` → https://github.com/MisterWolf1965/Marketing-Agent (private).
50 tests (34 preflight + 16 refresh). `.gitignore` hardened — it would have committed a live
TikTok OAuth token and an SFTP password. `data/performance-log.md` created and running: 2 HIT
predictions, 2 KILL verdicts. Brand assets + design system stored in `brand/assets/`.

**Shipped:** `packages/2026-08-21-diverse-set-change.md` (gate CLEAR) — 28s variety reel, film +
commerce. Facebook deliberately unwritten; its stop rule fired at 7 and 2. Cover + credits-led
end card designed to the real CI, inside social safe zones.

**Open for next session:**
1. **Was the otter reel re-rendered?** The banned "NO WASTED CREDITS" end card and invented
   "MIDDAY" label were flagged pre-post and never confirmed fixed. If not, a banned claim is live.
2. **Facebook audit** — Meta Business Suite reach settings / Page restrictions. Not a copy problem.
   Also: the same post has now double-fired three times (Jul 10, Jul 27, Aug 18/19).
3. **YouTube visibility discipline** — Private shipped 3×; Aug 12 = 1 view, Aug 20 = 5 views.
   A 20-40× effect, far bigger than posting hour.
4. The ~15s Instagram cut of the 28s reel (IG's band is 7-15s; it sits at 11 views).
5. Grade the CTA experiment: downloads clear 30 → keep privacy in the CTA; under 22 → move the
   test to the App Store page.

## 20.08.2026 — Repo groundwork + two real bugs found
- `git init` + first commit (75 files). Wrote `README.md` for an outside reader. Hardened
  `.gitignore` — it would otherwise have committed the live TikTok OAuth refresh token and
  `dashboard/.deploy.env` (contains an SFTP password).
- Added `tests/test_preflight.py` (34 tests). Writing them immediately exposed a **dead
  guardrail**: `#aiproductphotography`'s commerce-fit check scanned the hashtag line, and the tag
  contains "product", so it always passed itself. Fixed.
- Diagnosed the Aug 20 data loss: TikTok + YouTube were wiped to 0 rows. Cause was a broken
  playlist entry (~position 36-40) making any page spanning it 404, plus an expired TikTok token —
  and the all-sources-empty guard didn't fire because Meta succeeded. `refresh.py` now preserves
  per-source history, pages at 35, keeps partial results, and backfills from `videos.csv`.
  YouTube recovered 35 of 47 videos. **TikTok still needs `scripts/tiktok_auth.py` re-run.**
- Created `data/performance-log.md` (referenced everywhere, never actually existed). First entry
  grades the Facebook reach experiment: 3 and 1 views → sub-30 → **stop rewriting FB captions,
  audit the account.**
- Open: the otter package went out on IG/FB but **not** TikTok or YouTube; FB duplicated again
  (3rd time). Whether the posted reel used a corrected re-render is unverified.

## 13.08.2026 — Fresh start (memory wiped, machine kept)
- Archived the accumulated lessons / log / packages / grades to `archive/2026-08-13/`. Kept all plumbing, the dashboard, the API connections, `brand/registry.json` (the code-enforced gate rules), CLAUDE.md, and the package template.
- Reason: the system was built by incremental learn-and-tweak, and the memory had accumulated corrections-on-corrections that were themselves causing the repeated mistakes. Early runs performed well from a clean base — resetting to one.
- Next: re-analyse `dashboard/data.js` from scratch and rebuild `LESSONS.md` → *What wins* from the real numbers. See `first-run.md`.
