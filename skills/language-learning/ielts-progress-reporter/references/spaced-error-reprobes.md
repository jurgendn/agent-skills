# Spaced Error Re-probes

Use this protocol to prevent progress reports from attending only to recent errors.
The feedback files remain the evidence; this ledger controls when an old error
returns.

## Ledger

Store runtime state at `_dashboard/ielts-reprobe-ledger.yaml`:

```yaml
errors:
  - tag: article
    source_date: 2026-06-01
    source_file: t2-001-v1.md
    due_date: 2026-06-08
    interval_stage: 1
    status: scheduled
    probe_history: []
```

Use these fields:

- `source_date` and `source_file`: the feedback occurrence that opened or reset the
  item.
- `due_date`: next re-probe date in ISO format.
- `interval_stage`: stage of the next re-probe; 1 means 7 days, 2 means 30 days, and
  3 or later means 90 days.
- `status`: `scheduled` or `needs-work`.
- `probe_history`: date, stage, cue angle, exact prompt, and verdict for every
  attempt.

On first use, seed at most the three most frequent error tags. Use each tag's latest
feedback occurrence as its source and schedule stage 1 seven days later. Do not seed
every tag: the ledger is a retrieval queue, not a duplicate error index.

## Cue rotation

Before constructing a re-probe, inspect `probe_history`. Never repeat an exact prompt
or recycle the source sentence. Rotate by stage:

1. **transfer** — a new topic or sentence structure with the same underlying error;
2. **boundary** — a case where the usual correction may not apply;
3. **perturbation** — change one feature and ask what must change with it;
4. **why** — produce the correction and explain the load-bearing rule in one clause.

Cycle again after stage 4, always with fresh language. Require production: write or
correct a sentence and give a short reason. Multiple choice, recognition, and merely
naming the grammar rule do not pass.

## Updating the schedule

- On pass, append the attempt, increment `interval_stage`, keep `status: scheduled`,
  and set the next date from the pass date: 30 days for stage 2, then 90 days for
  stage 3 and later.
- On fail, append the attempt, set `status: needs-work`, and retain the current stage
  and due date so the item remains visible. After a corrected unaided response,
  increment and reschedule it.
- If the same tag appears in new marked feedback, treat that as fresh evidence of
  failure: set `status: needs-work`, update the source fields, retain the stage, and
  surface it before lower-priority scheduled items.

Run at most one re-probe per report. Show how many additional items remain due.
