# Schools Tracker

The master clock for this cycle. Keep one note per school in `fit-notes/` (or add frontmatter to a per-school note) and let Dataview roll them up here, or maintain the table by hand. Requires the Obsidian **Dataview** plugin for the queries.

## Manual tracker

Sort by deadline. Status: `researching` → `drafting` → `ready` → `submitted`.

| School | Program | Deadline | Fit | SOP | Letters | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## Dataview (if you put frontmatter on `fit-notes/fit-{school}.md`)

Expected frontmatter per fit note:

```yaml
---
school: MIT
program: EECS PhD
deadline: 2026-12-15
fit_score: high          # high | medium | low
sop_status: drafting     # researching | drafting | ready | submitted
letters_status: 1/3
status: drafting
---
```

```dataview
TABLE WITHOUT ID school AS School, program AS Program, deadline AS Deadline, fit_score AS Fit, sop_status AS SOP, letters_status AS Letters, status AS Status
FROM "fit-notes"
WHERE deadline
SORT date(deadline) ASC
```

## Upcoming deadlines (next to act on)

```dataview
LIST WITHOUT ID school + " — " + deadline
FROM "fit-notes"
WHERE deadline AND status != "submitted"
SORT date(deadline) ASC
LIMIT 5
```
