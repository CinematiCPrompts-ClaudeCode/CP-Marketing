# Performance log — weekly grades and predictions

Append-only, **newest entry at the top**. Format and grading rules:
`.claude/skills/marketing-weekly-review/references/log-format.md`.

The point of this file is accountability: each entry quotes the previous week's prediction
verbatim before grading it, so the system is on record being right or wrong.

---

## Week of 2026-08-13

**Posted this week:** the sea-otter "five real lights" package — Instagram (Aug 18), Facebook
(Aug 18 **and** Aug 19), YouTube (Aug 20). TikTok did **not** go out.

**Results** (revised 2026-08-20 once Meta was restored and the YouTube tail recovered — the
first version of this entry was written while IG/FB were stale and YouTube was truncated):
- TikTok: **not posted.** Last post Aug 12 (230). Source still down — see caveat below.
- Instagram: **11** (August avg 21.4, n=5) — below its own recent average.
- Facebook: **5** (Aug 18) and **2** (Aug 19, duplicate). August avg 6.1, n=7.
  _(Logged as 3 and 1 in the first draft; those were the last-known-good values preserved
  during the Meta outage. They have since ticked up. The verdict below is unaffected.)_
- YouTube: **4** — but published **Aug 20, the day of this review**. Far too early to read;
  carry it to next week rather than grading it. Title used the package copy verbatim.
- Downloads this week: **24** (Aug 13–20); all-time **355**.

**Grading last week's prediction:**
First logged week — no prior prediction to grade. (`performance-log.md` was referenced by
`CLAUDE.md` and the weekly-review skill but had never actually been created; this entry starts
the loop.)

**Experiment status:**
Facebook reach diagnostic. Stop rule as written: *"clears 150 → the Aug collapse was
content/duplication and nature-doc still works here; stays sub-30 → the problem is
account/reach-level, stop rewriting captions and audit Meta Business Suite instead."*
Result: **3 and 1 views. Decisively sub-30 → the rule fires. VERDICT: KILL the caption work.**
Facebook copy is not the problem. Stop iterating on it and audit the account: reach settings,
posting method, any restriction on the Page. Two posts is a small sample, but this is consistent
with a four-month monotonic decline (512 → 319 → 157 → 6.1), not with caption quality.

**What I changed and why:**
- Dropped wildlife-as-subject from the TikTok lead copy after the August post-mortem: safari
  framing got 230 and hunter framing 279, while product-pain framing got 821-859.
- Converted the Facebook block from a Grounding to an Experiment. Citing June's 1096 as if still
  achievable would have been dishonest at a 6.1 average.
- Tightened Instagram to the ultra-short two-line shape that produced 717 / 301 / 272.

**What went wrong operationally (worth more than the view counts this week):**
1. **Facebook posted twice again** (Aug 18 and 19) despite an explicit "POST ONCE" instruction
   in the package. Third occurrence — also happened Jul 10 and Jul 27. Likely a scheduler
   double-fire, not a human slip. Needs investigating at the tool level.
2. **TikTok never went out** — the single strongest platform (avg 588) and the one the package
   led with. The week's best-grounded copy went unposted. This is the biggest single miss of
   the week: the copy was written for TikTok first and the platform that actually converts
   views got nothing.
3. **The reel's blocking defects** — the banned "NO WASTED CREDITS" end card, the invented
   "MIDDAY" label, the reversed dawn/midday order — were flagged before posting. Whether the
   IG/FB posts used a corrected re-render is **unverified**; if not, a banned claim is live.

**Data caveat (do not skip):** the Aug 20 refresh lost TikTok and YouTube to a silent API
failure, and the Meta token was separately invalidated by a password change (code 190/460).
Status after the fixes:
- **Meta: restored.** 49 IG + 44 FB rows, live. `scripts/meta_token.py` now mints replacements.
- **YouTube: restored to 45 of 47** (8,278 views). The curated playlist still dies at its
  poisoned entry, but the channel's uploads playlist paginates cleanly, so `refresh.py` now
  fills the missing tail from there — recovering the 10 most recent videos, which is precisely
  the range a weekly review depends on. The 2 still missing are Private uploads.
- **TikTok: still down.** Needs `scripts/tiktok_auth.py` re-run, and the client secret rotated
  first (it was hardcoded in that script and reached a commit). **No TikTok number in this
  entry is current** — the platform is invisible, not zero.

**Prediction for next week:**
If the framing lesson holds, the TikTok post — once it actually goes out with the product-pain
hook rather than wildlife framing — should **clear 500** (vs. 230-290 for the last three
August posts). Instagram is predicted to stay **flat, in the 10-25 band**: nothing changed about
IG's structural reach this round, and its one great month (June, 150.9 avg) was driven by three
coastal posts that have not reproduced since. If TikTok comes in **under 300**, framing is not
the whole story and the next hypothesis should be posting cadence or account-level reach.
