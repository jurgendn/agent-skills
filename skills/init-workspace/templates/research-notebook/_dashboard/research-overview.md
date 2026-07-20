# Research Overview

Dataview over the research notebook. Requires the Obsidian **Dataview** plugin. Durable notes use the frontmatter schema documented in `AGENTS.md` (`id`, `kind`, `title`, `status`, `confidence`, `created`, `updated`, `related`).

## Open and active questions

```dataview
TABLE WITHOUT ID file.link AS Question, status AS Status, confidence AS Confidence, updated AS Updated
FROM "questions"
WHERE status = "open" OR status = "active"
SORT updated ASC
```

## Active ideas

```dataview
TABLE WITHOUT ID file.link AS Idea, status AS Status, confidence AS Confidence, updated AS Updated
FROM "ideas"
WHERE status = "open" OR status = "active"
SORT updated DESC
```

## Evidence needing attention

```dataview
TABLE WITHOUT ID file.link AS Evidence, status AS Status, confidence AS Confidence, updated AS Updated
FROM "evidence"
WHERE confidence = "low" OR status = "open" OR status = "active"
SORT updated ASC
```

## Recent decisions

```dataview
TABLE WITHOUT ID file.link AS Decision, status AS Status, updated AS Updated
FROM "decisions"
SORT updated DESC
LIMIT 10
```

## Synthesis pipeline status

Which `syntheses/` notes have entered the four-pass pipeline (`agents/pipeline.md`). Each pass records itself in frontmatter as `pipeline: evidence`, `drafted`, `reviewed`, or `verified`. A note absent here has not entered the pipeline.

```dataview
TABLE WITHOUT ID file.link AS Synthesis, pipeline AS "Last pass", updated AS Updated
FROM "syntheses"
WHERE pipeline
SORT updated DESC
```

## Review history

```dataview
LIST
FROM "reviews"
SORT file.name DESC
LIMIT 12
```
