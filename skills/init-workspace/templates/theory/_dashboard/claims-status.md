# Claims Status

Dataview over `claims/`. Requires the Obsidian **Dataview** plugin. Reads the
frontmatter schema in `AGENTS.md` (`claim`, `status`, `statement`,
`assumptions`, `proof`, `date`).

## All claims

```dataview
TABLE WITHOUT ID file.link AS Claim, status AS Status, statement AS Statement, date AS Date
FROM "claims"
SORT date DESC
```

## By status

```dataview
TABLE WITHOUT ID status AS Status, length(rows) AS Count, rows.file.link AS Claims
FROM "claims"
GROUP BY status
```

## Open (conjecture / sketched — still need work)

```dataview
LIST
FROM "claims"
WHERE status = "conjecture" OR status = "sketched"
SORT date ASC
```

## Assumptions in play

Which assumptions the active claims rely on — a wide-spread assumption is a
single point of failure worth scrutinising.

```dataview
TABLE WITHOUT ID assumption AS Assumption, length(rows) AS "Used by"
FROM "claims"
FLATTEN assumptions AS assumption
WHERE status != "refuted"
GROUP BY assumption
SORT length(rows) DESC
```
