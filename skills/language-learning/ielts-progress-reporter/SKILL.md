---
name: ielts-progress-reporter
description: Read marked IELTS Writing feedback in a practice vault and produce a periodic progress report with band trends, recurring errors, revision gains, next priorities, and spaced re-probes of older errors. Use whenever the user asks to "summarise my IELTS progress", "how am I doing", "write a progress report", "track my band scores over time", "what errors keep coming up", "are my essays improving", "review an old error", or requests a monthly/weekly writing report. Also use when the user answers a re-probe recorded in `_dashboard/ielts-reprobe-ledger.yaml`. Read existing feedback; do NOT mark new drafts — use ielts-writing-task1 or ielts-writing-task2. Never invent bands for unmarked attempts and never let recent errors crowd older due errors out of review.
---

# IELTS Progress Reporter

A single essay mark tells the candidate how one draft went. A progress report tells them whether they are actually getting better, which weaknesses keep recurring, and where the next hour of study should go. This skill reads the feedback files an IELTS practice vault has already accumulated and turns the recorded bands and error tags into that picture.

The feedback files are the source of truth. Each one in `feedback/` opens with YAML frontmatter holding the per-criterion bands and a list of error tags (schema below). This skill only reads and aggregates what is already there — it does not re-mark drafts and never fabricates a band for an attempt that has no feedback file yet.

## Use this when

- The user wants an overview of how their IELTS Writing is trending across many attempts.
- The user asks which errors recur most, or whether a weakness is improving.
- The user wants a weekly/monthly report, or a running all-time snapshot.
- The user points at a `feedback/` folder or `_dashboard/` and wants it summarised.

## Do not use this when

- The user wants a single draft marked → use `ielts-writing-task1` or `ielts-writing-task2`.
- The user wants a study plan/schedule → use `ielts-learning-planner`.
- There are no feedback files yet → say so; there is nothing to aggregate. Do not estimate bands from raw drafts.

## Feedback frontmatter schema (what gets read)

The vault's `AGENTS.md` is authoritative; this is the shape the report depends on:

| Field | Meaning |
|-------|---------|
| `task` | `1` or `2` |
| `prompt_id`, `version` | identify the attempt; revisions share a `prompt_id` |
| `date` | ISO date, drives period bucketing |
| `band_overall`, `band_cc`, `band_lr`, `band_gra` | overall + Coherence/Cohesion, Lexical Resource, Grammatical Range & Accuracy |
| `band_ta` (Task 1) / `band_tr` (Task 2) | first criterion: Task Achievement / Task Response |
| `errors` | list from the vault's fixed tag vocabulary |

`band_ta` and `band_tr` are mutually exclusive per file. The report unifies them into a single "first criterion" trend line so Task 1 and Task 2 progress can sit side by side, while still labelling each correctly.

---

## Process

### Step 1 — Locate the vault and feedback files

Find the `feedback/` directory. Usually it sits at the vault root next to `attempts/` and `_dashboard/`. If the user pointed at a specific folder, use that. If you cannot find a `feedback/` folder with `.md` files, stop and tell the user — there is nothing to report on.

### Step 2 — Decide the scope (ask only if genuinely ambiguous)

Two scopes are supported; the user picks at runtime:

- **Cumulative** — one running snapshot of every attempt to date. Good for "where do I stand overall".
- **Period** — bucket attempts by `date` into **weekly** or **monthly** windows and show the trend across them. Good for "am I improving".

Infer from the request when you can ("monthly report" → period/monthly; "how am I doing overall" → cumulative). Only ask if the request is truly unclear. You may also narrow by task (`1`, `2`, or both) or by a date range if the user mentions one.

### Step 3 — Run the aggregation script

Do **not** read and tally the bands by eye — half-band averages and error counts across dozens of files are easy to get wrong, and a progress report loses all value if a number is off. Use the bundled script, which parses every feedback file's frontmatter and returns exact figures as JSON:

```bash
python3 scripts/aggregate_feedback.py --vault <VAULT_ROOT> --mode cumulative
# or, for a trend:
python3 scripts/aggregate_feedback.py --vault <VAULT_ROOT> --mode period --period monthly
```

Useful flags: `--feedback-dir <PATH>` (if `feedback/` is not under the vault root), `--task 1|2|all`, `--since YYYY-MM-DD`, `--until YYYY-MM-DD`. The script has no third-party dependencies.

The JSON gives you: coverage counts, per-criterion averages (`criterion1` is the unified TA/TR line), `error_frequency` (most common first), `revision_deltas` (band change from first to latest version of each multi-version prompt), and — in period mode — the same broken out per `periods[]` bucket.

### Step 4 — Surface one spaced old-error re-probe

Read `references/spaced-error-reprobes.md` and maintain
`_dashboard/ielts-reprobe-ledger.yaml`. Seed it from recorded feedback when absent.
If any re-probe is overdue, include exactly one — oldest due first — before selecting
priorities. Do not replace it with a more recent error merely because the recent one
appears more often.

### Step 5 — Compose the report

Turn the JSON into the template below. The script owns the numbers; your job is the interpretation — naming the weakest criterion, the trend direction, the most persistent errors, and the priorities. Round displayed bands to half-bands the way IELTS does (`6.25` average → describe as "around 6", not a fake half-band the candidate could never receive). Be honest: if there are only two or three attempts, say the trend is not yet meaningful rather than over-reading noise.

For Task 1 attempts, respect the vault's data-accuracy rule: the bands already reflect whatever was assessable, so report them as recorded and do not re-litigate data accuracy here.

### Step 6 — Write the report to the vault

Write to `_dashboard/` as a **dated** file so history is preserved — e.g. `_dashboard/progress-2026-06-24.md` (cumulative) or `_dashboard/progress-2026-06.md` (monthly). Do not overwrite an existing dated report; if the exact filename exists, append a short suffix or confirm with the user. The vault's living `_dashboard/writing-progress.md` (if present) is Dataview-driven — leave it alone unless the user explicitly asks you to update it.

After writing the file, give the user a 3–4 line summary in chat: current standing, trend direction, top recurring error, and the single highest-leverage next focus. Tell them where the file was written.

---

## Report structure

Use this template. Drop sections that have no data (e.g. no revisions yet) rather than padding them.

```markdown
# IELTS Writing Progress — <scope label, e.g. "Cumulative as of 2026-06-24" or "May 2026">

**Attempts covered:** <n> (<by task>) across <distinct_prompts> prompts
**Date range:** <earliest> → <latest>

## Band summary
| Criterion | Average | Read as |
|-----------|--------:|---------|
| Task Achievement / Response | x.x | ~band |
| Coherence & Cohesion | x.x | ~band |
| Lexical Resource | x.x | ~band |
| Grammatical Range & Accuracy | x.x | ~band |
| **Overall** | x.x | ~band |

One or two sentences: which criterion is the weakest anchor, which is the strength.

## Trend            <!-- period mode only -->
| Period | Attempts | Overall | TA/TR | CC | LR | GRA |
|--------|---------:|--------:|------:|---:|---:|----:|
| ...    | ...      | ...     | ...   | ...| ...| ... |

One or two sentences on direction (improving / flat / noisy), with the honesty caveat if the sample is small.

## Recurring errors
| Error tag | Count |
|-----------|------:|
| ...       | ...   |

Name the 2–3 most persistent tags and what they signal. Link to the vault's error notes where useful, e.g. [[errors/article]].

## Revision gains          <!-- only if multi-version prompts exist -->
| Prompt | v→v | Overall change |
|--------|-----|---------------:|
| t2-001 | 1→2 | +0.5 |

Did revising actually move the score? One sentence.

## Old error due now       <!-- only when a re-probe is overdue -->
**Error:** <tag>
**Fresh cue:** <one new sentence or micro-task>

Answer without opening the old correction. Require production or correction plus a
brief reason; recognition and rule naming do not pass.

## Top 3 priorities for the next stretch
1. ...
2. ...
3. ...
```

Priorities should follow from the data: the weakest criterion, the most frequent error tag, and whichever skill is flat or declining. Keep them concrete and few — a report that lists ten things to fix gets ignored.

## Hand-offs

- Mark a new draft → `ielts-writing-task1` or `ielts-writing-task2`
- Turn the report into a schedule → `ielts-learning-planner`
- Build targeted vocabulary practice → `ielts-vocabulary-builder`
