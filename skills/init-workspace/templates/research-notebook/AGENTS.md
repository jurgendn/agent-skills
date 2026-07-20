# AGENTS.md — Research Notebook: <PROJECT TITLE>

Orientation for any agent operating on this research notebook. This file is the map and the rules; the actual reasoning, literature, experiment-planning, and writing knowledge lives in the installed skills this file routes to. The vault holds evolving research thought and evidence as notes. It does not hold source code, raw data, or a paper's final submission package.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with your own default behavior, this file wins, so the vault behaves the same across agents instead of varying with each one's defaults.

- **This is research note-taking, not coding.** Produce questions, ideas, reading notes, evidence notes, decisions, meeting notes, and syntheses. Do **not** write or store code, scripts, or computational notebooks in this vault. If the user requests implementation work, route it to a separate code repository and record only the resulting notes or artifact links here.
- **Small captures stay small; substantial syntheses use the pipeline.** Inbox entries, individual questions, meeting notes, and decision records do not need a four-pass process. For any synthesis or research-position note a reader will rely on, run `agents/pipeline.md` — **evidence → draft → review → verify** — inside that note, grounding it in `reading/` + `evidence/` + `decisions/`. The pipeline produces exactly one file; never create per-stage side files.
- **Separate evidence from interpretation.** A source claim points to a `reading/` note or checkable source; an observed result points to an `evidence/` note or external artifact; an interpretation is marked as an inference. Do not turn a plausible idea into an established finding.
- **Mark uncertainty explicitly.** Give questions and ideas honest statuses; tag unsupported beliefs as `(inference)` or `#unverified`, and state what observation, source, or argument would change the assessment.
- **Report what you actually did, not what you intended.** Before marking a question answered, an idea supported, or a review complete, point to the note or source that establishes it. If a check was skipped, say so plainly.
- **Check inputs before running a skill; ask for what's missing.** Literature synthesis needs populated `reading/`; idea assessment needs the relevant `questions/`, `ideas/`, and `evidence/`; decision review needs the original `decisions/` record. If a required input is empty or missing, stop and ask the user to add it or identify where it lives. Never fabricate the input.

## What this vault is

An ongoing research notebook for turning fragments into traceable research judgment. Capture quickly in `inbox/`, promote durable questions and ideas into their own notes, connect them to reading and evidence, record consequential decisions, and periodically synthesize what changed. The vault optimises for recovering *why you currently believe something* without turning note-system maintenance into the research itself.

## Layout

```text
inbox/            # quick captures awaiting classification; not permanent storage
questions/        # one research question per note, with status and resolution evidence
ideas/            # hypotheses, mechanisms, method directions, and partial arguments
reading/          # one note per external source, grounded in the source actually read
evidence/         # observations, result summaries, artifact links, and negative results
decisions/        # consequential choices, alternatives, rationale, and revisit triggers
meetings/         # advisor/collaborator notes with decisions and assigned actions
syntheses/        # substantial cross-note maps, positions, and periodic research summaries
reviews/          # weekly/monthly notebook reviews and unresolved-item audits
references/       # note-types-and-review-rhythm
agents/           # pipeline.md: evidence → draft → review → verify (one file)
_dashboard/       # research-overview: open questions, active ideas, evidence, decisions
```

## Filename conventions

```text
questions/  q-{NNN}-{shortname}.md           # q-001-why-role-splitting.md
ideas/      idea-{NNN}-{shortname}.md        # idea-003-directed-objective.md
reading/    src-{NNN}-{shortname}.md         # src-012-barber-bimodularity.md
evidence/   ev-{NNN}-{shortname}.md          # ev-007-seven-edge-witness.md
decisions/  dec-{YYYY-MM-DD}-{shortname}.md  # dec-2026-07-20-baseline-first.md
meetings/   {YYYY-MM-DD}-{shortname}.md       # 2026-07-20-advisor-sync.md
reviews/    {YYYY}-W{NN}.md                   # 2026-W30.md
```

Zero-pad sequence numbers. Prefer stable descriptive names over generic files such as `notes.md` or `thoughts-2.md`.

## Core note format

Durable notes in `questions/`, `ideas/`, `evidence/`, and `decisions/` open with valid YAML frontmatter so `_dashboard/` can surface their state:

```markdown
---
id: q-001
kind: question          # question | idea | evidence | decision
title: "Can role splitting improve directed community recovery?"
status: active          # open | active | supported | refuted | answered | parked
confidence: low         # low | medium | high
created: 2026-07-20
updated: 2026-07-20
related: ["[[idea-003-directed-objective]]", "[[ev-007-seven-edge-witness]]"]
---

## Statement
...

## Why it matters
...

## Current evidence
...

## What would change my mind
...

## Next check
...
```

Use only statuses that make sense for the note type; do not mark a question `answered` or an idea `supported` without linking the resolving evidence.

## Routing

| Folder / task | Skill to use |
|---|---|
| unfinished question, idea, or mechanism | `whiteboard-peer` |
| turning an idea into a paper direction | `paper-idea-and-scope-brainstormer`, then `research-idea-stress-test` |
| `reading/`, comparing or mapping sources | `literature-triangulation`; use `citation-auditor` for source-claim checks |
| extracting and motivating a research gap | `gap-finder` → `gap-motivation-builder` |
| formal claim or proof direction | `flow-idea-to-proof` |
| experiment or evaluation notes | `experiment-design`, `benchmark-and-baseline-selector`, `hypothesis-and-ablation-planner` |
| ownership of an AI-assisted result | `knowledge-debt-audit` |
| finished synthesis judged against a reader | `professor-critic` |
| experiment source code | `research-codebase` in a separate repository |

Use `whiteboard-peer` as the first skill when the notebook begins from an unfinished research question or partial idea.

## Default actions

- **Capturing:** put an unclassified fragment in `inbox/` with a date and enough context to understand it later. If its type is already clear, create the durable note directly instead of manufacturing an inbox step.
- **Promoting a question or idea:** create the numbered durable note, link the source capture, state what would resolve or falsify it, and connect any current reading or evidence. Do not delete the original capture until the durable note preserves its useful context.
- **Adding reading or evidence:** describe only the source actually read or the observation actually made. Link the URL, vault note, repository path, result file, or other checkable artifact. Keep interpretation in its own paragraph and label inference explicitly.
- **Recording a decision:** state the choice, alternatives considered, evidence available at the time, tradeoff accepted, and the condition that should trigger reconsideration. A decision note is a rationale record, not proof the choice was correct.
- **Reviewing weekly:** empty or triage `inbox/`; surface stale active questions; connect orphan ideas to evidence or mark them parked; inspect recent decisions for triggered revisit conditions; write `reviews/{YYYY}-W{NN}.md` describing what actually changed and what remains unresolved.
- **Synthesising:** run the four-pass pipeline in the final file under `syntheses/`. Build from existing notes, resolve or retain review warnings, and verify every factual claim before marking `pipeline: verified`.

## Rules

- **One durable note, one research unit.** A question, idea, source, evidence item, or decision gets its own note; `syntheses/` connects units across notes.
- **Do not manufacture closure.** `parked`, `refuted`, and `inconclusive` are legitimate outcomes. Status reflects evidence, not the desire for progress.
- **Keep provenance visible.** Preserve the link from a synthesis to its source notes, from an idea to the question that motivated it, and from a decision to the evidence available when it was made.
- **No raw data or source code.** `evidence/` stores summaries and pointers. Put executable work in a separate code repository.
- **Review the research, not the filing system.** Add folders, tags, or fields only when a real retrieval or synthesis problem justifies them. Follow `references/note-types-and-review-rhythm.md` for the lightweight review loop.

## Obsidian formatting rules

A few silent failures: the file saves fine but renders broken in Obsidian. Follow these whenever you write a note here.

- **Use soft wrapping, not hard wrapping.** Keep each prose paragraph or list item on one physical line and let Obsidian wrap it visually. Do not insert manual line breaks merely to satisfy a column width. Start a new physical line only for a new paragraph or Markdown structure such as a heading, list item, block quote/callout, table row, or code fence.
- **Frontmatter must be valid YAML and start on line 1** — nothing before the opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid YAML and makes Obsidian render the whole block as raw text. Use a quoted list on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Quote any frontmatter value that contains a colon** (and values starting with `[`, `{`, `#`, `@`, `` ` ``, `!`, `&`, `*`, `>`, `|`, or a quote). A colon-space inside an unquoted value — most often a paper title with a subtitle, `title: Stochastic Blockmodels: First Steps` — makes YAML read it as a nested key, so the whole block fails to parse and renders as raw text. Wrap the value in double quotes: `title: "Stochastic Blockmodels: First Steps"`. The same goes for `authors`, `aliases`, or any field whose value has a `:` in it.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table (stray `label]]` leaks into a phantom column). In a table use an unaliased link `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just never inside a table.
- **Inline math in a table must not contain a bare `|` either, and `\|` does not fix it.** The table parser splits the cell on `|` first, so `$d \ll |V|$` fragments into phantom columns. And `\|` is the wrong repair: inside `$...$` it renders as the norm symbol `‖`, silently changing the meaning. Use the LaTeX command for the bar you mean — cardinality / absolute value `|V|` → `$\lvert V\rvert$`, norm `\|x\|` → `$\lVert x\rVert$`, conditional `P(u|v)` → `$P(u \mid v)$`.
- **A bare `$` in prose can open math mode.** A second `$` later on the same line — a price like `$30k … $45k`, "raise $5M" — makes everything between the two render as italicised math. Escape literal dollar signs: `\$30k`.
- **`#` without a trailing space is a tag, not a heading.** `#Results`, `#1`, or a mid-line `#` (e.g. `C#`) silently becomes a tag. Write `# Heading` with a space, or escape it as `\#`.
