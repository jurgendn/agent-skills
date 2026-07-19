---
name: gre-learning-planner
description: Build a personalised GRE study plan — diagnostic baseline, Verbal/Quant/Writing time allocation, weekly schedule, vocabulary pipeline, official practice-test milestones, and coordination with grad-school application deadlines. Use this skill whenever the user asks how to prepare for the GRE ("GRE study plan", "8 weeks to the GRE, where do I start", "target 325+, currently 310", "how do I balance verbal and quant prep", "when should I take the GRE for fall applications"), wants to know whether/when to retake, or wants their GRE prep integrated with PhD application timelines. Routes actual practice to gre-verbal-reasoning, gre-reading-comprehension, gre-quant-coach, gre-issue-essay, and gre-vocabulary-builder. For IELTS planning use ielts-learning-planner.
---

# GRE Learning Planner

A GRE plan is calibrated to three numbers — baseline, target, weeks — plus one profile fact: which section carries the gap. Verbal and Quant improve on completely different timelines (vocabulary is long-lead; quant test-behavior fixes are fast), so generic "study 2 hours a day" plans misallocate badly.

## Use this when

- The user wants a structured GRE study plan or weekly schedule.
- The user asks how to split time across Verbal, Quant, and Analytical Writing.
- The user asks when to take (or retake) the GRE relative to application deadlines.
- The user wants practice-test milestones and a way to tell whether the plan is working.

## Do not use this when

- The user wants actual practice or feedback — route to the section skills (`gre-verbal-reasoning`, `gre-reading-comprehension`, `gre-quant-coach`, `gre-issue-essay`, `gre-vocabulary-builder`).
- The user is planning IELTS prep — use `ielts-learning-planner`.
- The user is deciding which programs to apply to — use `apply-program-fit-mapper`.

## Volatile facts — verify live, never assert from memory

Whether target programs require, recommend, or ignore the GRE (many went GRE-optional and policies change yearly), score percentile tables, test fees, retake spacing rules, and at-home testing policies: check the current program pages and https://www.ets.org/gre at planning time. Scores are valid for five years — that fact is stable; per-program cutoffs are not.

---

## Step 1 — Diagnostic

Establish before planning anything:

| Question | Why it matters |
|----------|----------------|
| Baseline scores (V / Q / AW) from a real practice test | The gap per section, not overall, drives allocation |
| Target scores | Set by target programs' admitted-student profiles (verify live), not round numbers |
| Test date, or application deadlines if undecided | Sets timeline and the take/retake buffer |
| Study hours per week | Determines what is realistic |
| Profile | STEM/research background → usually strong-Q/weak-V; humanities → often the reverse |
| English-medium test experience | An IELTS-band-7+ user starts GRE Verbal from a different place than the raw score suggests |

**No baseline yet?** The first action of any plan is a full official **POWERPREP** practice test (free from ETS) under real timing. Third-party app quizzes systematically miscalibrate; do not plan from them.

**Score-gap timelines** (at ~10–15 focused hrs/week; rough, section-dependent):

| Gap (per section) | Realistic timeframe |
|-------------------|---------------------|
| +2–3 points | 3–5 weeks |
| +4–6 points | 6–10 weeks |
| +7–10 points | 3–5 months |

Quant gaps close faster than Verbal gaps of the same size when the cause is test behavior rather than content (see `gre-quant-coach`'s diagnosis); Verbal gaps built on vocabulary are the slowest — which is why vocabulary starts on day 1 regardless of the schedule's emphasis.

## Step 2 — Allocation logic

1. **Weakest-section-first**, weighted by target: a 168Q/155V STEM applicant to CS programs needs Verbal hours, not more quant drills — but check what the target programs actually weigh (CS committees read Q; humanities read V and AW).
2. **Vocabulary is a daily fixed cost**, not a scheduled block: 20–30 min/day via `gre-vocabulary-builder`, every day, from day 1 to test day. It compounds; cramming it does not work.
3. **AW gets little but non-zero time**: one timed essay per week (via `gre-issue-essay`) is enough for most users, ramping to two in the final fortnight. Most programs care that AW clears a bar (often 4.0+ — verify per program), not that it is maximized.
4. **Never zero out the strong section** — one maintenance set per week keeps it from decaying and keeps pacing sharp.

Suggested weekly split by weak section (excluding the daily vocab slot):

| Weak section | V : Q : AW |
|--------------|-----------|
| Verbal | 55 : 30 : 15 |
| Quant | 30 : 55 : 15 |
| Balanced | 40 : 40 : 20 |

## Step 3 — Weekly template (example: 12 hrs/week + daily vocab, weak Verbal)

| Day | Activity | Skill to invoke |
|-----|----------|-----------------|
| Daily | 25 min vocabulary (due re-probes first, then new words) | `gre-vocabulary-builder` |
| Mon | TC/SE drill set + error-log review (60 min) | `gre-verbal-reasoning` |
| Tue | RC: 2 passages untimed with passage maps (60 min) | `gre-reading-comprehension` |
| Wed | Quant mixed set, miss classification (60 min) | `gre-quant-coach` |
| Thu | TC/SE timed set (45 min) + leech-word rework (15 min) | `gre-verbal-reasoning` |
| Fri | Timed Issue essay + scoring (60 min, weekly) | `gre-issue-essay` |
| Sat | Timed mixed verbal section (41 min) + full review (60 min) | both verbal skills |
| Sun | Quant weak-topic drill (45 min) + week review: error logs across all skills (30 min) | `gre-quant-coach` |

Adjust proportions from the diagnostic; the invariants are the daily vocab slot, at least one *timed* block per section per week, and review time ≥ half of drill time. Untimed accuracy work dominates early weeks; the timed share grows every week until the final two weeks are mostly full-length timed sections.

## Step 4 — Milestones and the final approach

- **Practice-test checkpoints every 3–4 weeks**, official POWERPREP material only, full test at real timing. Compare per-section scores AND the error-log composition (miss classes shrinking?) — score alone is noisy at ±2–3 points.
- **Stagnation rule**: two flat checkpoints in a section means the plan is wrong for it — rediagnose with the section skill (usually the miss class shifted and the drills didn't).
- **Final 2 weeks**: no new vocabulary, no new content — timed sections, review, and the test-day script (section order, the skip/mark/return pass, QC discipline, essay clock).
- **Scheduling around applications**: work backward from the earliest deadline — score reporting takes ~1–2 weeks after the test, and a retake needs its own prep window plus ETS's minimum spacing (verify current rule). Practically: first attempt ≥ 2.5–3 months before the earliest deadline preserves a real retake option without colliding with SOP-writing season (see `flow-phd-application` for the wider timeline).
- **Retake decision**: retake only if a specific section is below the target programs' profile *and* the checkpoint trend says more points are available. A 1-point-overall bump is rarely worth the prep time it steals from SOPs and outreach.

## Plan output format

1. **Diagnostic summary** — baseline, targets (with "verify against program pages" flag), gap per section, weeks, hrs/week.
2. **Allocation** — weekly hours per section + the daily vocab slot.
3. **7-day schedule** — concrete activities with durations and which `gre-*` skill runs each.
4. **Checkpoint calendar** — practice-test dates and what "on track" looks like at each.
5. **Test-date recommendation** — with the retake buffer against the user's application deadlines.

Keep it realistic: a plan the user won't follow is worse than none. At 5 hrs/week, say plainly that the timeline stretches ~2×, and protect the daily vocabulary slot before everything else.
