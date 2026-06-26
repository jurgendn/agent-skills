# AGENTS.md — Learning: <TOPIC>

Orientation for any agent operating on this learning vault. This file is the map
and the rules; the teaching and literature-mapping live in the installed skills
this file routes to. The vault supports breadth-first onboarding into an
unfamiliar area, with every claim traceable to a source.

## What this vault is

A workspace for learning a new topic well enough to summarise it, use it, and
know what you don't know. One note per source, synthesised summaries per
subtopic, a concept map, and a running list of open questions and terms. It
optimises for *grounded* understanding — nothing asserted that a `sources/` note
doesn't support.

## Layout

```text
sources/          # one note per source (paper/book/talk/post) + bib info
notes/            # reading notes per source (mirrors sources/ filenames)
summaries/        # synthesised summaries per subtopic (across sources)
map/              # concept / landscape map of the area
exercises/        # practice problems, self-tests, re-derivations
open-questions.md # running list of unknowns and confusions
glossary.md       # terms, defined as they appear
references/       # study-method, source-grounding-rules
_dashboard/       # topic-map (coverage + confidence by subtopic)
```

## Filename conventions

```text
sources/   src-{NNN}-{shortname}.md     # src-001-attention-is-all-you-need.md
notes/     src-{NNN}-{shortname}.md     # same name as the source it annotates
summaries/ {subtopic}.md                # attention.md, optimization.md
```

Zero-pad numbers. A reading note in `notes/` shares the filename of the
`sources/` note it covers.

## Source note format

Every file in `sources/` opens with YAML frontmatter so `_dashboard/` can track
coverage and confidence:

```markdown
---
src: src-001
title: Attention Is All You Need
authors: Vaswani et al.
year: 2017
type: paper            # paper | book | talk | post | course
subtopic: attention
status: read           # queued | reading | read
confidence: medium     # low | medium | high (your grasp of it)
---

## Why it matters
...

## Key claims (with where to find them)
...
```

## Routing

| Folder / task | Skill to use |
|---|---|
| onboarding sequence | `flow-learn-new-topic` (orchestrates the whole path) |
| `map/`, comparing sources | `literature-triangulation` |
| understanding a hard concept | `professor-mentor-technical-teaching` |
| turning it into a survey/Related Work | `related-work-writer` |
| testing a derivation/claim you learned | `theory-derivation-auditor`, `theory-to-toy-cases` |

## Default actions

- **Adding a source:** create `sources/src-{NNN}-…md` with frontmatter, then a
  reading note in `notes/` of the same name.
- **Synthesising:** write/extend `summaries/<subtopic>.md` *across* sources;
  every claim links to the `sources/` note it came from.
- **As you go:** add new terms to `glossary.md` and unknowns to
  `open-questions.md`; update `_dashboard/topic-map.md` confidence.
- **To check understanding:** create an exercise in `exercises/` and try to
  re-derive or explain without looking (`study-method.md`).

## Rules

- **Ground every claim.** Nothing in `summaries/` or `map/` is asserted without a
  link to a `sources/` note that supports it (`source-grounding-rules.md`). Mark
  unsourced beliefs as open questions, not facts.
- **Note your confidence honestly.** `confidence: low` on a source is a signal to
  revisit, not a failure. The dashboard surfaces weak spots.
- **Keep the glossary and open-questions live** — they are the cheapest measure
  of progress.
- **Synthesise, don't collect.** A pile of reading notes isn't understanding;
  the value is in `summaries/` and `map/` that connect sources.

## Obsidian formatting rules

Two silent failures: the file saves fine but renders broken in Obsidian. Follow
these whenever you write a note here.

- **Frontmatter must be valid YAML and start on line 1** — nothing before the
  opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid
  YAML and makes Obsidian render the whole block as raw text. Use a quoted list
  on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an
  aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table
  (stray `label]]` leaks into a phantom column). In a table use an unaliased link
  `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just
  never inside a table.
