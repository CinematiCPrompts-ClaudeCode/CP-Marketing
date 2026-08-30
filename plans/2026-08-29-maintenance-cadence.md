# Social maintenance cadence — from 2026-08-29

**Decision: keep presence on all four platforms, but stop spending the week on four bespoke
copy sets.** The nine-week analysis (`data/performance-log.md`, week of 08-29) found views and
downloads uncorrelated (+0.19 across an 8.5× view swing), so per-platform caption craft has no
measurable payoff. Presence itself is nearly free. Effort is what was expensive.

This replaces the "one post a week, TikTok only" line in the 08-29 report — presence on all four
is the user's call and it costs almost nothing to honour.

---

## The rhythm: one asset, four posts, one hour

**One asset per week.** Not four. The same clip goes everywhere.

| Platform | Effort | Copy |
|---|---|---|
| **TikTok** | The only one that gets real thought | Fully grounded, gate-checked, written fresh |
| **Instagram** | Reuse | TikTok copy, trimmed to 2 lines, exactly 5 tags |
| **YouTube** | Reuse | Searchable title + TikTok body as description |
| **Facebook** | Reuse | YouTube description verbatim, no tuning |

**Why TikTok gets the thought:** it is the only channel producing real view volume
(255–805 vs Instagram 7–38, Facebook 1–4, YouTube 3–218). If any channel can be moved by
writing, it is that one.

**Why the others are reuse, not neglect:** their numbers do not respond to copy quality. The
clearest proof is this week — Instagram's post was grounded on its own best-ever post (35) and
returned **7**. Better writing did not transfer. So write once, adapt mechanically, move on.

## Weekly checklist

1. **Pick the asset** — one clip, single subject preferred (see the band table in `LESSONS.md`:
   single-subject demos run 784–859 on TikTok, variety reels 255–303).
2. **Write the TikTok caption properly** — grounded on a real number, per the gate.
3. **Adapt mechanically** for the other three. No new angles, no fresh hooks.
4. **Run `./check.sh`** — non-negotiable, still catches banned claims and bad tags.
5. **Post one platform per day**, so each upload's visibility toggle and duplicate-check get
   verified individually. Both of the recurring operational failures — YouTube shipping Private
   (3×) and Facebook double-firing (4×) — happen when four uploads go out in one sitting.

**Budget: about an hour a week**, versus most of a working day for four bespoke packages.

## What still gets real attention

Effort moves off captions and onto the two things that plausibly touch installs:

- **The App Store listing.** Subtitle + keyword change written 2026-08-13, still unshipped. The
  app cannot surface for "AI prompt generator for video" because neither word is in the title or
  subtitle. This is the only channel with demonstrated download traffic.
- **App Store Connect Analytics Reports API.** Until it is wired, impressions, product-page views
  and conversion are invisible and every attribution claim stays inferred. This is what would
  make the next nine weeks measurable instead of circumstantial.

## The one experiment still worth running

**The transformation reel** (`plans/2026-08-14-next-reel-concepts.md`, concept #1). Two
generations. Grounded on the best post in the dataset — "Amateur to Hollywood in 1 click", 1987 —
and on 845 and 301 for the same before/after shape.

It settles a real open question: whether **single-subject** content beats **variety**, which is
what the 805-vs-255 pair suggests but has never been tested directly. Hold the pain framing
constant, change the subject back to one scene.

**Signal: clears 600 on TikTok → single-subject is confirmed as the content rule and it becomes
the default asset type. Under 350 → content type is not the lever either, and social moves to
pure maintenance with no further testing.**

## What "maintenance" explicitly does not mean

- Not stopping the gate. `./check.sh` still runs on every package — banned claims and unverified
  tags do not become acceptable because the stakes dropped.
- Not stopping the log. Weekly grades continue in `data/performance-log.md`; a prediction that
  goes unrecorded cannot be graded.
- Not abandoning Facebook or Instagram. They stay posted. They just stop consuming writing time
  until an account-level audit explains why Facebook fell 512 → 3.
