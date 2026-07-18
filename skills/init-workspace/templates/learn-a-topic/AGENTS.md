# AGENTS.md — Learning: <TOPIC>

Orientation for any agent operating on this learning vault. This file is the map
and the rules; the teaching and literature-mapping live in the installed skills
this file routes to. The vault supports breadth-first onboarding into an
unfamiliar area, with every claim traceable to a source.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with
your own default behavior, this file wins, so the vault behaves the same across
agents instead of varying with each one's defaults.

- **This is learning/synthesis work, not coding.** Produce source notes,
  summaries, a concept map, and exercises. Do **not** write code unless the user
  explicitly asks (an `exercises/` re-derivation may use it when requested).
- **Substantial syntheses go through the pipeline — in one file.** For any
  non-trivial summary or map note, run the four-pass pipeline in
  `agents/pipeline.md` — **evidence → draft → review → verify** — inside that
  note: read the actual `sources/` and `notes/` and collect only what they
  support; draft; check for claims that outrun the sources, missing caveats, or
  conflated ideas; then anchor every claim to a `sources/` note per
  `references/source-grounding-rules.md`, demoting unsupported claims to
  `open-questions.md`. The pipeline produces exactly one file; never create
  per-stage side files. Small notes skip the pipeline (the rules below still
  apply).
- **Synthesis is source-grounded.** Follow `references/source-grounding-rules.md`:
  nothing in `summaries/` or `map/` is asserted without a link to a `sources/`
  note that supports it.
- **Mark uncertainty explicitly.** Record your grasp honestly (`confidence:` in
  source frontmatter); tag anything you believe but cannot source as an entry in
  `open-questions.md`, not as fact.
- **Report what you actually did, not what you intended.** Before marking a step,
  section, or check done, point to the artifact or source that shows it. If a step
  was skipped or a result is unverified, say so plainly — never present intended,
  plausible, or in-progress work as completed.
- **Check inputs before running a skill; ask for what's missing.** Each skill/stage
  draws from specific folders (see *Layout*) — `sources/` is the root: synthesis,
  maps, and exercises all build on populated source notes. Before running one,
  confirm its input folder(s) actually contain the needed notes; if a required
  input is empty or missing, **stop and ask the user to add the source (or say
  where it lives) — do not proceed on an empty folder or fabricate the input.**

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
search-log.md     # queries, tool/recommender trails, inclusion/exclusion rationale
open-questions.md # running list of unknowns and confusions
glossary.md       # terms, defined as they appear
references/       # study-method, source-grounding-rules
agents/           # pipeline.md: evidence → draft → review → verify (one file)
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
title: "Stochastic Blockmodels: First Steps"   # quote any value with a colon
authors: Holland, Laskey, Leinhardt
year: 1983
type: paper            # paper | book | talk | post | course
subtopic: graph-generative-models
role: canonical        # seed | canonical | survey | dissenting | tool-suggested | background
status: read           # queued | reading | read
confidence: medium     # low | medium | high (your grasp of it)
---

## Why it matters
...

## Key claims (with where to find them)
...

## Why this source is in the vault
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
  reading note in `notes/` of the same name. Record in `search-log.md` how the
  source was found and why it belongs: keyword search, citation trail, survey
  pointer, recommendation system, LLM suggestion, advisor suggestion, or
  deliberate dissenting/counterexample source.
- **Synthesising:** run the four-pass pipeline (`agents/pipeline.md`) in
  `summaries/<subtopic>.md` — read the sources, draft *across* them, review for
  over-reach, verify every claim links to a `sources/` note.
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
- **Keep the search trail visible.** Do not let semantic search, recommender
  systems, or LLM-suggested reading lists silently define the field. Log the
  queries and tool suggestions you used, then deliberately add at least one
  source from outside the dominant recommended cluster when mapping a new area.
- **Synthesise, don't collect.** A pile of reading notes isn't understanding;
  the value is in `summaries/` and `map/` that connect sources.

## Obsidian formatting rules

A few silent failures: the file saves fine but renders broken in Obsidian. Follow
these whenever you write a note here.

- **Frontmatter must be valid YAML and start on line 1** — nothing before the
  opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid
  YAML and makes Obsidian render the whole block as raw text. Use a quoted list
  on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Quote any frontmatter value that contains a colon** (and values starting with
  `[`, `{`, `#`, `@`, `` ` ``, `!`, `&`, `*`, `>`, `|`, or a quote). A colon-space
  inside an unquoted value — most often a paper title with a subtitle,
  `title: Stochastic Blockmodels: First Steps` — makes YAML read it as a nested
  key, so the whole block fails to parse and renders as raw text. Wrap the value
  in double quotes: `title: "Stochastic Blockmodels: First Steps"`. The same goes
  for `authors`, `aliases`, or any field whose value has a `:` in it.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an
  aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table
  (stray `label]]` leaks into a phantom column). In a table use an unaliased link
  `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just
  never inside a table.
- **Inline math in a table must not contain a bare `|` either, and `\|` does not
  fix it.** The table parser splits the cell on `|` first, so `$d \ll |V|$`
  fragments into phantom columns. And `\|` is the wrong repair: inside `$...$` it
  renders as the norm symbol `‖`, silently changing the meaning. Use the LaTeX
  command for the bar you mean — cardinality / absolute value `|V|` →
  `$\lvert V\rvert$`, norm `\|x\|` → `$\lVert x\rVert$`, conditional `P(u|v)` →
  `$P(u \mid v)$`.
- **A bare `$` in prose can open math mode.** A second `$` later on the same line
  — a price like `$30k … $45k`, "raise $5M" — makes everything between the two
  render as italicised math. Escape literal dollar signs: `\$30k`.
- **`#` without a trailing space is a tag, not a heading.** `#Results`, `#1`, or a
  mid-line `#` (e.g. `C#`) silently becomes a tag. Write `# Heading` with a space,
  or escape it as `\#`.
