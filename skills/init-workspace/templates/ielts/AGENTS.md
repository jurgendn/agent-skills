# AGENTS.md

Orientation for any agent operating on this IELTS practice vault. This file is the map and the rules; it does **not** contain marking knowledge. Read the relevant IELTS skill and band-reference material before scoring.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with your own default behavior, this file wins.

- **This is IELTS marking/practice work, not coding.** Do **not** write code.
- **Never fabricate.** Do not invent a band, a figure value, or an example you cannot see in the attempt file. Mark only what the draft (and any provided figure data) actually contains; when something needed for scoring is missing, say so explicitly rather than guessing (see the Task 1 data-accuracy rule).

## What this vault is

A practice loop for IELTS Writing. Each attempt is a self-contained Markdown note containing the prompt and the candidate's draft. Feedback is written as a separate mirrored Markdown note. The vault is optimised for studying progress and recurring error patterns, not for deep exercise-folder nesting.

## Layout

Canonical layout:

```text
attempts/
  t1-001-v1.md       # Task 1 attempt: prompt/figure data + draft
  t2-001-v1.md       # Task 2 attempt: prompt + draft
  t2-001-v2.md       # revised draft of the same prompt

feedback/
  t1-001-v1.md       # mark of attempts/t1-001-v1.md
  t2-001-v1.md       # mark of attempts/t2-001-v1.md
  t2-001-v2.md       # mark of attempts/t2-001-v2.md

errors/
  article.md
  weak-thesis.md
  comma-splice.md

_dashboard/
  writing-progress.md

references/
  ielts-band-descriptors.md
  anchor-essays-task1.md
  anchor-essays-task2.md
```

Filename convention:

```text
t{task}-{prompt_id}-v{version}.md
```

Examples:

- `t1-001-v1.md` = Task 1, prompt 001, version 1.
- `t2-014-v3.md` = Task 2, prompt 014, version 3.

Use zero-padded prompt numbers: `t2-001-v1.md`, never `t2-1-v1.md`.

`feedback/<same-filename>.md` marks `attempts/<same-filename>.md`. The filenames must always correspond exactly.

"Latest" means the highest numeric version for the same task and prompt prefix, not the most recently modified file. For example, among `t2-001-v1.md`, `t2-001-v2.md`, and `t2-001-v3.md`, the latest is `t2-001-v3.md`.

## Attempt file format

Every file in `attempts/` should be self-contained: include the prompt and the draft in the same note. This prevents feedback from being detached from the task question.

Task 2 attempt example:

```markdown
---
task: 2
attempt: t2-001-v1
prompt_id: t2-001
version: 1
date: 2026-06-24
---

## Prompt

Some people believe ...

## Draft

Candidate essay text here.
```

Task 1 attempt example:

```markdown
---
task: 1
attempt: t1-001-v1
prompt_id: t1-001
version: 1
date: 2026-06-24
---

## Prompt

The chart below shows ...

## Figure data

| Category | 2000 | 2020 |
|---|---:|---:|
| A | 10 | 20 |

## Draft

Candidate report text here.
```

For Task 1, if the figure's values are available, include them under `## Figure data` as a Markdown table. If the figure data is not available, leave that section out and follow the Task 1 data-accuracy rule below.

## Routing

- An attempt whose frontmatter has `task: 1`, or whose filename begins with `t1-`, uses the `ielts-writing-task1` skill.
- An attempt whose frontmatter has `task: 2`, or whose filename begins with `t2-`, uses the `ielts-writing-task2` skill.

Before assigning a band, consult the relevant IELTS band descriptors. If local skill/reference files exist under `.claude/skills/`, `references/`, or another project-local skills directory, prefer those. Otherwise use the installed IELTS skills from the agent runtime.

If anchor essays are available for the relevant task, read the matching anchor file before assigning any band and locate the draft *relative to the anchors*, not only against the descriptor in the abstract.

Expected shared references, when present:

- `references/ielts-band-descriptors.md` — single source of truth for the band criteria.
- `references/anchor-essays-task1.md` / `references/anchor-essays-task2.md` — real essays at known official bands.

## Default action

When pointed at an attempt file:

1. Read the attempt file in `attempts/`.
2. Identify the task from frontmatter or filename.
3. Read the prompt and draft from the attempt file.
4. Mark the draft against that prompt.
5. Write the mark to `feedback/<same-filename>.md`.
6. **Never overwrite** an existing feedback file — feedback history is the record of progress.

When asked to mark the latest version of a prompt:

1. Find all files in `attempts/` sharing the same task/prompt prefix, e.g. `t2-001-v*.md`.
2. Choose the highest numeric version.
3. Write feedback to the mirrored filename in `feedback/`.

If the target attempt file is missing, do **not** create a feedback file. Report the missing file instead.

Before writing feedback, verify that `feedback/<same-filename>.md` does not already exist. If it exists, stop and report that feedback for this version has already been written.

## Feedback file format

Every file in `feedback/` **opens with YAML frontmatter**, then prose below it. The frontmatter is what the `_dashboard/` Dataview queries read, so the schema is fixed.

For Task 2:

```yaml
---
task: 2
attempt: t2-003-v1
prompt_id: t2-003
version: 1
date: 2026-06-24
band_tr: 6.5
band_cc: 6
band_lr: 6
band_gra: 5.5
band_overall: 6
errors: [article, comma-splice, weak-thesis]
---
```

For Task 1, use `band_ta` instead of `band_tr`:

```yaml
---
task: 1
attempt: t1-003-v1
prompt_id: t1-003
version: 1
date: 2026-06-24
band_ta: 6.5
band_cc: 6
band_lr: 6
band_gra: 5.5
band_overall: 6
errors: [overview-missing, data-accuracy, word-choice]
---
```

Band values may be integers or half-bands only: `5`, `5.5`, `6`, `6.5`, etc. The `errors` field must be a YAML list using only the fixed vocabulary below.

Use error tags only from this fixed vocabulary. Extend this list here before using any new tag; do not invent ad hoc tags in feedback files.

`article`, `comma-splice`, `subject-verb`, `weak-thesis`, `cohesion`, `overview-missing`, `data-accuracy`, `word-choice`, `collocation`, `under-length`, `off-topic`.

## Error-class notes

The `errors/` folder is the study library for recurring weaknesses. Each error note should explain the pattern and collect examples from feedback files.

When marking a draft, link important repeated errors in the prose feedback where helpful, for example:

```markdown
This is an [[errors/article|article]] error: "the education" should be
"education".
```

Do not create a new error tag casually. If a new error category is genuinely needed, first add it to the fixed vocabulary above, then create the matching `errors/<tag>.md` note.

## Prose feedback format

Below the frontmatter, include:

1. Overall band summary.
2. Criterion-by-criterion feedback.
3. Quoted examples from the draft when identifying issues.
4. Corrected or improved versions of problem sentences.
5. Top 3 priorities for the next draft.

For Task 2, criterion feedback should cover:

- Task Response
- Coherence and Cohesion
- Lexical Resource
- Grammatical Range and Accuracy

For Task 1, criterion feedback should cover:

- Task Achievement
- Coherence and Cohesion
- Lexical Resource
- Grammatical Range and Accuracy

## Task 1 data-accuracy rule

Task Achievement requires verifying the candidate's numbers. The agent only sees what is in the attempt file. If the figure's values are present as a table, assess data accuracy normally. If they are **not** present, mark Task Achievement on structure, overview, and selection only, and state explicitly:

> data accuracy not assessed (figure not provided as data).

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

Never fake or infer a number you cannot see.
