---
name: init-workspace
description: 'Initialize a structured Obsidian-style workspace for learning, research notebooks, papers, academic applications, talks, test preparation, theory, and similar note-centric knowledge work. Use when the user asks to set up, start, initialize, scaffold, or bootstrap a vault/workspace for work organized primarily through notes and written artifacts. Do not use for software repositories, software applications, experiment codebases, or other coding projects. Ask one short intake batch covering the work and its definition of done, project title plus confirmed target directory, and any differences from the typical case. Then use a ready template as-is, adapt the closest template while keeping its contract internally consistent, or synthesize a lean bespoke vault when none fits. Write only into the confirmed target vault; never modify this skill''s templates during a run. This skill creates structure and routing, not the downstream content itself.'
---

# init-workspace

Scaffold a ready-to-work, note-centric knowledge project from a short clarifying
round followed by either a heavy, self-contained template or a bespoke scaffold
built in the same style. Each result includes a folder tree and an `AGENTS.md`
that documents the layout and routes work to the right skills. Add
workspace-local `references/` and an Obsidian `_dashboard/` (Dataview) when the
selected template or intake justifies them.

## When to use

The user wants to **start a note-centric knowledge project** and have its
structure + conventions laid down. Trigger on "set up / start / initialize /
scaffold / bootstrap a workspace or vault for …" when the work is learning,
research, writing, academic applications, test preparation, presentations,
theory, or another activity whose primary artifacts are notes and documents.
Requests in this scope that do not match the seven templates use the bespoke path.

## When NOT to use

- The user wants the actual downstream work (mark this essay, write my intro,
  prove this lemma). Route to the domain skill, not here.
- The project already exists and is structured — this skill scaffolds, it does
  not reorganize. (Re-running is safe — see *Merge rules* — but it won't
  restructure an existing layout.)
- For structuring an experiment **codebase** (source layout for fast hypothesis
  testing), use `research-codebase`. The `paper` template here is the *writing*
  vault and defers code structure to that skill.
- The user wants a software repository, application, package, website, data
  pipeline, or other coding project. This skill creates knowledge-work vaults,
  not source-code scaffolds, even when the user says "start a project."

## Template menu

The seven templates are the **starting points**, not a closed set — see
*Clarifying intake* below for how a request that doesn't cleanly match one of
these still gets scaffolded.

| Type | Use it for | First skill the AGENTS.md routes to |
|---|---|---|
| `learn-a-topic` | Breadth-first onboarding into an unfamiliar area | `flow-learn-new-topic` |
| `ielts` | IELTS Writing practice loop (attempts → feedback → progress) | `ielts-learning-planner` |
| `paper` | One research paper, idea → submission → artifact | `flow-paper-lifecycle` |
| `phd-application` | A full PhD/research application cycle | `flow-phd-application` |
| `research-notebook` | Ongoing research questions, ideas, evidence, decisions, and synthesis | `whiteboard-peer` |
| `talk` | A talk/presentation, narrative → slides | `research-talk-planner` |
| `theory` | A theory/proof project, claim → proof → stress-test | `flow-idea-to-proof` |

The `ielts` template ships **AGENTS.md only** (plus folders + dashboard): the
installed `ielts-*` skills already carry the band descriptors and feedback
aggregation, so the vault doesn't duplicate them. Every other template seeds its
own `references/` so the workspace is self-contained.

### Shared research pipeline

The research pipeline is identical across templates, so it lives once at
`templates/_shared/agents/pipeline.md` (the single source of truth) rather than
being duplicated per template. It is a single four-pass protocol — **evidence →
draft → review → verify** — run *inside the artifact's own file*: the evidence
table and open review items live in the working file while the pipeline runs and
are compressed into a final Sources section, so the pipeline never creates
per-stage side files (no `research.md`/`draft.md`/`review.md`/`cited.md`) and
its net output is exactly one file. A size gate restricts it to substantial
artifacts; small notes are covered by the Operating contract in a single pass.
It is generalized and agent-portable: it names capabilities, integrity rules,
and an output contract without binding to a particular runtime's tools. At
scaffold time it is copied into the vault at `<vault>/agents/`, so the workspace
stays self-contained and portable.

Only the **full-pipeline** templates get the `agents/` folder: `paper`, `theory`,
`learn-a-topic`, and `research-notebook`. Their `AGENTS.md` *Operating contract*
routes substantial research artifacts through the four passes. The `talk`,
`phd-application`, and `ielts` templates use a **lighter grounding-only
contract** (no-code + source-grounded + mark-uncertainty, without the pipeline),
so they do **not** receive the `agents/` folder.

## Clarifying intake

Before touching the menu, ask a short, single-batch round of clarifying
questions — a handful, not an interview:

1. **What is the work, and what does "done" look like?** The user's own
   description of the project and its end deliverable (a submitted paper, a
   passed test, a scheduled talk, an admitted application, a mastered topic, or
   another note-centric knowledge outcome).
2. **Project title and target directory.** Propose the current directory as the
   default by naming its exact path, and ask the user to confirm it or provide a
   replacement. Their answer to this intake item is the write confirmation; do
   not ask for the same confirmation again.
3. **What, if anything, is different from the typical case?** E.g. a survey
   instead of a single paper, a co-authored or panel talk, a combined test-prep
   track, a non-research proof project, a multi-paper application cycle — this
   is what decides *use as-is* vs *adapt* vs *bespoke* below. If the answer is
   "nothing, it's a standard X," that's a valid answer and keeps the template
   as-is.

Keep this to one round. If the original request already supplies an answer,
include the understood value in the batch instead of asking for it from scratch.
Don't loop back for more detail than these three answers give you: after the
user answers, the scaffold should land in that same turn.

## Procedure

1. **Run the clarifying intake** (above) and decide the path:
   - **Use as-is** — the description matches one of the seven template types
     with no stated differences. Proceed with that template unchanged.
   - **Adapt** — matches one type but with named differences. Use that
     template as the base and adjust only what the differences require: add or
     remove folders in the Layout, add or trim `references/` files, and edit
     the AGENTS.md prose (title, Layout, routing, type labels, and path-specific
     Operating-contract wording) to reflect them. Preserve the behavioral
     guarantees that apply to the base template — non-coding knowledge work,
     source grounding or non-fabrication, explicit uncertainty, faithful
     reporting and input checks where present, the one-file pipeline rules
     where present, *Merge rules*, and Obsidian formatting — but update folder
     names and type-specific statements so the contract matches the adapted
     Layout.
   - **Bespoke** — none of the seven fit. Synthesize a scaffold *for this vault
     only* (never write into this repo's `templates/`) that follows the same
     shape as the others: a folder tree sized to the actual answers, a full
     `AGENTS.md` with the same required sections (title, Operating contract,
     Layout, routing to whichever existing skills fit the work, Obsidian
     formatting rules). Its Operating contract must define the work as
     note-centric and non-coding, prohibit fabrication, require source grounding
     and marked uncertainty where claims are involved, report only completed
     work, and check required input notes before running downstream skills. If
     the work is a substantial source-grounded synthesis or research artifact,
     also copy `templates/_shared/agents/pipeline.md` into `agents/`, exactly
     like the full-pipeline templates do. Skip a
     `_dashboard/` or `references/` unless the answers clearly call for one;
     a bespoke scaffold should be as lean as the intake justifies, not a
     eighth heavy template.
   If the intake still leaves real ambiguity between two types, ask which —
   don't guess.
2. **Use the confirmed target directory.** The user's answer to intake item 2
   is the confirmation. State the resolved path in the progress update, but do
   not pause for a second confirmation.
3. **Read the template.** For *use as-is* or *adapt*, open
   `templates/<type>/AGENTS.md` — its *Layout* section is the authoritative
   folder list (start from it, then apply any *adapt* changes). For *bespoke*,
   there is no template file to read; draft the `AGENTS.md` and Layout
   directly from the intake answers, matching the structure of the closest
   existing template as a shape reference.
4. **Create the folder tree.** Make every folder in the (possibly adapted or
   bespoke) Layout, adding a `.gitkeep` to any that starts empty.
5. **Copy or write the seeded files.** For *use as-is*, copy the template's
   `AGENTS.md`, `references/`, and `_dashboard/` into the target unchanged (see
   *Merge rules*). For *adapt*, copy them and then apply the stated edits. For
   *bespoke*, write the `AGENTS.md` (and any `references/`/`_dashboard/` the
   intake justified) directly. For templates or bespoke scaffolds carrying the
   full-pipeline contract (`paper`, `theory`, `learn-a-topic`,
   `research-notebook`, or a bespoke source-grounded synthesis/research
   artifact), also copy
   `templates/_shared/agents/pipeline.md` into
   `<vault>/agents/` so the research pipeline travels with the vault. `talk`,
   `phd-application`, `ielts`, and any bespoke non-research scaffold use the
   lighter grounding-only contract and get no `agents/` folder.
6. **Write the entry-file stub.** Write `<vault>/CLAUDE.md` containing exactly
   one line, `@AGENTS.md`. This makes the operating contract auto-load on Claude
   Code (which reads `CLAUDE.md` and follows `@` imports) while staying inert for
   agents that read `AGENTS.md` natively (Codex, etc.) — so `AGENTS.md` remains
   the single source of truth and the vault behaves the same on every runtime. Do
   this for every path, including `ielts` and bespoke. (See *Merge rules* —
   never clobber an existing `CLAUDE.md`.)
7. **Fill the one-line title.** Replace the project-title placeholder at the top
   of the `AGENTS.md` with the user's project name if they gave one; otherwise
   leave the placeholder.
8. **Report.** List what was created, say which path was taken (as-is / adapt
   / bespoke) and why, and name the first skill to run (the table above, or —
   for bespoke — whichever existing skill(s) fit), so the user knows the next
   move.

## Merge rules

Re-running on an existing directory is safe: **merge, never overwrite.** These
rules apply the same way to a *use as-is*, *adapt*, or *bespoke* result. When the
user explicitly identifies an already-scaffolded vault, use the intake only to
confirm that target and any missing facts needed to fill gaps; do not re-derive
or redesign the existing workspace.

- Create missing folders; leave existing ones untouched.
- Write a seeded or bespoke file only if no file of that name already exists
  at the destination. Never clobber an existing `AGENTS.md`, reference,
  dashboard, `agents/` file, or any content file — those may hold the user's
  work or edits.
- **Legacy pipeline migration (the one exception).** If `<vault>/agents/`
  contains the retired four role files (`researcher.md`, `reviewer.md`,
  `verifier.md`, `writer.md`), those are seeded files from the old per-stage
  design, not user content: offer to delete them and install `pipeline.md` in
  their place so the vault does not carry two conflicting protocols. Confirm
  with the user before deleting, and keep any of the four they say they have
  modified.
- If `AGENTS.md` already exists, do not replace it; report that the workspace
  already has one and stop touching it.
- If `CLAUDE.md` already exists, do not replace it — the user may have their own
  imports or memory there. If it does not already pull in `AGENTS.md`, report
  that so the user can add `@AGENTS.md` themselves.

## Notes

- Templates assume an **Obsidian vault** (YAML frontmatter, `[[wikilinks]]`,
  `_dashboard/` Dataview). The folders are plain folders, so a code editor works
  too; only the dashboard is Obsidian-specific.
- Seeded and generated Markdown uses **soft wrapping, not hard wrapping**: keep
  each prose paragraph or list item on one physical line and let Obsidian wrap
  it visually. Insert new physical lines only for new paragraphs or Markdown
  structure, never merely to satisfy a column width.
- The clarifying round is intentionally short — three questions, one batch, one
  turn — not a requirements interview. Its job is to route to *use as-is* /
  *adapt* / *bespoke* and fill the title and directory, not to extract a full
  spec. Most requests that clearly name one of the seven types with no stated
  differences still resolve to *use as-is* and stay as zero-customization as
  before.
- The repo's `templates/` directory is never written to by a run of this
  skill. *Adapt* and *bespoke* output only ever land in the target vault;
  growing the durable template set is a separate, deliberate repo change (see
  this repo's `CLAUDE.md` skill-authoring conventions), not something this
  skill does on a user's behalf mid-scaffold.
- This skill is self-contained: every template lives under `templates/` here.
