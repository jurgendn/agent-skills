# Experiment Index

Dataview over `experiments/`. Requires the Obsidian **Dataview** plugin. Reads
the frontmatter schema defined in `AGENTS.md` (`exp`, `status`, `verdict`,
`hypothesis`, `result`, `date`).

## All experiments

```dataview
TABLE WITHOUT ID file.link AS Exp, status AS Status, verdict AS Verdict, result AS Result, date AS Date
FROM "experiments"
SORT date DESC
```

## By status

```dataview
TABLE WITHOUT ID status AS Status, length(rows) AS Count, rows.file.link AS Experiments
FROM "experiments"
GROUP BY status
```

## Supports vs refutes the claim

```dataview
TABLE WITHOUT ID verdict AS Verdict, length(rows) AS Count, rows.file.link AS Experiments
FROM "experiments"
WHERE verdict
GROUP BY verdict
```

## Still open (planned / running)

```dataview
LIST
FROM "experiments"
WHERE status = "planned" OR status = "running"
SORT date ASC
```
