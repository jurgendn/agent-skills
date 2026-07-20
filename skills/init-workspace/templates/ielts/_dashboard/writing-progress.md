# Writing Progress

Dataview dashboard over `feedback/`. Requires the Obsidian **Dataview** plugin. All numbers come from the fixed feedback frontmatter (`band_*`, `errors`, `date`, `task`, `prompt_id`, `version`) defined in `AGENTS.md`. For trend statistics and revision deltas across the whole vault, run the `ielts-progress-reporter` skill (it reads the same `feedback/*.md` files).

## Latest marks

```dataview
TABLE WITHOUT ID
  file.link AS Attempt,
  task AS Task,
  (band_ta + "" + band_tr) AS "TA/TR",
  band_cc AS CC,
  band_lr AS LR,
  band_gra AS GRA,
  band_overall AS Overall,
  date AS Date
FROM "feedback"
SORT date DESC
LIMIT 20
```

## Overall band by date

```dataview
TABLE WITHOUT ID date AS Date, band_overall AS Overall
FROM "feedback"
WHERE band_overall
SORT date ASC
```

## Task 2 only

```dataview
TABLE WITHOUT ID file.link AS Attempt, band_tr AS TR, band_cc AS CC, band_lr AS LR, band_gra AS GRA, band_overall AS Overall, date AS Date
FROM "feedback"
WHERE task = 2
SORT date DESC
```

## Task 1 only

```dataview
TABLE WITHOUT ID file.link AS Attempt, band_ta AS TA, band_cc AS CC, band_lr AS LR, band_gra AS GRA, band_overall AS Overall, date AS Date
FROM "feedback"
WHERE task = 1
SORT date DESC
```

## Revision deltas (multi-version prompts)

Prompts you revised — compare the earliest and latest version of the same `prompt_id` to see whether revising moved the band.

```dataview
TABLE WITHOUT ID prompt_id AS Prompt, rows.version AS Versions, rows.band_overall AS "Overall by version"
FROM "feedback"
GROUP BY prompt_id
WHERE length(rows) > 1
SORT prompt_id ASC
```

## Recurring errors

```dataview
TABLE WITHOUT ID error AS Error, length(rows) AS Count
FROM "feedback"
FLATTEN errors AS error
GROUP BY error
SORT length(rows) DESC
```
