---
name: marketing-weekly-review
description: Weekly performance-review loop for the Cinematic Prompts marketing system — the thing that closes the learn-and-improve cycle. Use this whenever the user wants to log a week's results, review how recent posts did, check whether last week's prediction or experiment worked (e.g. the Instagram boost experiment), grade the campaign week-over-week, or decide what to change next. Trigger on phrases like "log this week," "how did we do," "review performance," "did the Instagram experiment work," "weekly review," or whenever the user pastes recent view counts expecting a read. Always GRADE the previous prediction and VERDICT any running experiment against its stop rule — never just report raw numbers.
---

# Marketing Weekly Review

This skill runs the weekly accountability loop for the Cinematic Prompts campaign. The marketing system makes predictions and runs experiments; this skill is where you come back and check whether they worked, then decide the next move. Without this loop, the dashboard is just numbers. With it, each week sharpens the last.

It pairs with the `cinematic-prompts-marketing` skill (which generates content and plans). That skill makes the bets; this one settles them.

## The loop (run in this order)

1. **Get the current numbers.**
   - In the marketing repo (Claude Code): run `scripts/snapshot.py` from the project root — it parses `dashboard/data.js` and prints each platform's post count, total/avg views, the newest post, and downloads (all-time / last 30d / last 7d). Run `python .claude/skills/marketing-weekly-review/scripts/snapshot.py` (adjust path to wherever the skill lives).
   - Outside the repo (Cowork / Claude app): ask the user to paste this week's post(s) and their view counts per platform, plus downloads if they have them.

2. **Read last week's entry.** Open `data/performance-log.md` and read the most recent entry (top of file) to recover (a) the prediction made last time and (b) any running experiment and its stop rule. If the file doesn't exist yet, this is the first logged week — note that and skip grading.

3. **Grade last week's prediction.** Quote it verbatim, state the actual outcome, verdict it HIT / MISS / PARTIAL. Be honest; a miss is useful data.

4. **Verdict the running experiment against its own stop rule.** The current one is the **Instagram experiment**: pain-first caption + exactly 5 targeted hashtags + visual cold-open (no text first 1.5s). Its stop rule: *if two posts stay under ~15 views, rest the account 7 days before trying again; success signal is per-post views back above 30.* Call it CONTINUE / KILL / REST based on what the numbers actually did — don't override the rule because you want to keep going.

5. **Write the new entry.** Append a dated entry at the **top** of `data/performance-log.md` in the exact format in `references/log-format.md`. (Outside the repo: output the entry text for the user to paste/save.) Always end the entry with a fresh, single, testable **prediction for next week**.

6. **Summarize in chat — three lines:** what worked, the experiment verdict, and the one change you're making next. Then, if content is needed, hand off: "want me to build next week's package?" (that's the `cinematic-prompts-marketing` skill's job).

## Read this first

Before writing the entry, read `references/log-format.md` — it has the exact entry template, the grading rules, and the honesty rules. Follow the honesty rules strictly:

- One post is a signal, not proof — name the sample size.
- View counts show correlation, not causation — say "consistent with," not "proves."
- Compare each platform to its **own** recent average, never across platforms (different scales).
- If it's flat or down, say so plainly and propose the next change.

## What good looks like

A weak review just lists this week's views. A strong review says: "Last week I predicted IG would clear 30 with the hashtag fix; it hit 41 across two posts — HIT, though that's a small sample. Experiment: CONTINUE. TikTok slipped to 480 (below its ~590 avg) — the promo-style cut underperformed the narrative format, so next week I'm going back to story-led. Prediction: narrative TikTok clears 600; IG holds above 30." Specific, graded, traced to numbers, and it sets up the next check.
