# Topic Map

Dataview over `sources/`. Requires the Obsidian **Dataview** plugin. Reads the
frontmatter schema in `AGENTS.md` (`src`, `title`, `subtopic`, `status`,
`confidence`, `type`, `year`). This is the coverage view; the conceptual
landscape lives in `map/`.

## Coverage by subtopic

```dataview
TABLE WITHOUT ID subtopic AS Subtopic, length(rows) AS Sources, rows.file.link AS Notes
FROM "sources"
GROUP BY subtopic
SORT length(rows) DESC
```

## Confidence (where you're weak)

```dataview
TABLE WITHOUT ID confidence AS Confidence, length(rows) AS Count, rows.file.link AS Sources
FROM "sources"
GROUP BY confidence
```

## To revisit (low confidence)

```dataview
LIST
FROM "sources"
WHERE confidence = "low"
SORT subtopic ASC
```

## Reading queue

```dataview
LIST WITHOUT ID title + " (" + year + ")"
FROM "sources"
WHERE status = "queued" OR status = "reading"
SORT year DESC
```
