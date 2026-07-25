# AGENTS.md — Study Notes: <PROJECT TITLE>

Orientation for any agent operating on this study vault. This file is the map and the rules; the actual teaching, explanation, and exercise-writing knowledge lives in the installed skills this file routes to. The vault holds per-session study notes and the exercises that verify them. It does not hold source code, raw data, or a paper draft.

This is the leanest template in the set: **two folders, one level deep, no subfolders.** Depth is not free — every extra folder is a filing decision paid at capture time, when the cost is highest. Resist adding a third.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with your own default behavior, this file wins, so the vault behaves the same across agents instead of varying with each one's defaults.

- **This is study note-taking, not coding.** Produce notes, key terms, review questions, and exercises. Do **not** write or store code, scripts, or computational notebooks here. If the user asks for implementation work, route it to a separate code repository.
- **The user captures; you expand.** Never write the raw capture for the user — the encoding benefit of putting it in their own words is the point, and an agent that captures destroys it. You take their fragments and expand; you do not attend the lecture for them.
- **The user reviews every expansion before it is saved.** Present the expanded note for approval rather than writing it to `notes/` and announcing it as done. An unreviewed expansion is a transcript, not a note.
- **The user solves the exercises.** Generate the problems; never fill in `# Solutions`. If asked to check work, check what they wrote — do not replace it with your own solution and call it correct.
- **Ground expansions in the capture and the named source.** Expand what the fragments actually say. Where a fragment is too thin to expand safely, write `TODO: unclear from capture` and ask — never invent plausible lecture content, a definition the source did not give, or a citation.
- **Mark uncertainty explicitly.** Distinguish what the source stated, what you inferred while expanding, and what remains unresolved. Tag inferences `(inference)` and unverified claims `#unverified`.
- **Report what you actually did.** Before saying a note is expanded or an exercise set is generated, point to the file. If a step was skipped, say so plainly.
- **Check inputs before running a skill; ask for what's missing.** Expansion needs a raw capture; exercise generation needs an expanded note. If the input is empty, stop and ask — do not proceed on an empty file or fabricate the input.

## What this vault is

A per-session study loop. You attend a lecture, read a chapter, or work through a paper; you capture rough fragments; an agent expands them into a structured note; the agent generates a matching exercise file; you solve it. One session produces exactly one note and one exercise file, paired by filename. The vault optimises for *turning attendance into verified understanding* without becoming a filing system.

## The session loop

```text
capture (you)  →  expand (agent, you review)  →  store  →  drill (you solve)
```

1. **Capture — you, during the session.** Fragments, abbreviations, arrows, keywords. Not full sentences; speed and honesty beat completeness. Paste them under `# Raw Capture`.
2. **Expand — agent, after the session.** Turn fragments into structured prose, pull out `# Key Terms`, and write 3–5 review questions. Ground every expansion in the capture plus the named source.
3. **Store — after the user approves.** Write to `notes/{YYYY-MM-DD}-{topic}.md`.
4. **Drill — agent generates, you solve.** Create `exercises/{YYYY-MM-DD}-{topic}-ex.md` with 5 problems derived from that note, and link the pair.

**Never delete the raw capture.** It stays in the note permanently. It is the better input to any later re-expansion, the fallback when an expansion turns out wrong, and the record of what *you* actually thought before clean prose overwrote it.

## Layout

```text
notes/            # one note per session: raw capture + expansion + key terms + questions
exercises/        # one exercise file per note, same date and topic, suffixed -ex
```

No subfolders. No `references/`, no `_dashboard/`, no `agents/` — this file carries the whole method.

## Filename conventions

```text
notes/      {YYYY-MM-DD}-{topic}.md        # 2026-07-25-backprop.md
exercises/  {YYYY-MM-DD}-{topic}-ex.md     # 2026-07-25-backprop-ex.md
```

**Metadata lives in frontmatter, not in the folder path** — tags, source, and status are what gets queried, so never encode them as directories. The filename is the one exception, and it carries exactly two things: the **date** (so files sort chronologically) and the **`-ex` suffix** (so a note and its exercise pair unambiguously). Do not drop the date prefix as redundant; it is the vault's only ordering.

## Note file format

```markdown
---
tags: [tag1, tag2]
source: "lecture / textbook / paper"
date: 2026-07-25
status: draft          # draft → reviewed → mastered
---

# Raw Capture

(your micronotes, exactly as written — never edited away)

# Notes

(expanded prose, structured with sub-headings)

# Key Terms

(definitions extracted from the notes)

# Questions

(3-5 review questions generated from the notes)

→ [[2026-07-25-backprop-ex]]
```

`status` is honest, not aspirational: `draft` until the user has read the expansion, `reviewed` once they have corrected it, `mastered` only once the paired exercises are solved and checked.

## Exercise file format

```markdown
---
tags: [tag1, tag2]
source: "lecture / textbook / paper"
date: 2026-07-25
type: exercise
status: unsolved       # unsolved → solved → checked
---

# Problems

(5 problems generated from the note, hardest last)

# Solutions

(the user writes these — an agent must leave this section empty)
```

## Section headers are a retrieval contract

The headers above are fixed. Retrieval chunks on headings, so renaming `# Key Terms` to `# Glossary` in one file silently breaks every query that targets it. Add a new heading if you need one; do not rename an existing one.

## Routing

| Task | Skill to use |
|---|---|
| a concept in the capture the user did not follow | `professor-mentor-technical-teaching` |
| generating or grading the exercise set | `concept-exercise-generator` |
| the user wants to verify understanding by teaching it back | `naive-student` |
| checking whether an expansion is understood or merely borrowed | `knowledge-debt-audit` |
| the sessions have become a whole unfamiliar field to map | `flow-learn-new-topic` |
| one paper or theorem now deserves depth-first mastery | `flow-deep-understanding` |
| experiment or implementation code | `research-codebase` in a separate repository |

## Rules

- **Two folders, permanently.** `notes/` and `exercises/`. A third folder needs a real retrieval problem, not a tidiness impulse.
- **One session, one note, one exercise file.** Do not split a session across files or merge two sessions into one.
- **Querying the vault is not retrieval practice.** Asking an agent to search and synthesize your notes delegates the retrieval and the learning benefit with it. Query to locate what to re-derive, then close the answer and reconstruct it yourself.
- **An agent needs file-write access scoped to this vault root** to save notes and exercises directly. Which server or integration provides that is environment-specific and changes often — check the current setup rather than assuming a particular one. Without it, the agent presents the note and the user saves it; the loop still works.
- **Version the vault.** Git or Obsidian Sync, so a bad expansion is one revert away.

## What the evidence actually supports

Stated at the strength the sources carry. Do not promote these.

- **Structured beats unstructured — supported.** Structured note formats scored higher overall than unstructured linear notes (Yıldırım 2026, n=134; Cornell-vs-linear was the only pairwise comparison to survive correction), and meta-analytic work agrees that what you do with notes dominates the recording medium (Voyer et al. 2022; Flanigan et al. 2024). **This is an overall achievement difference, not a retention mechanism** — the same trial found no differential forgetting between methods (time×group interaction non-significant, F(3,129) = 1.82, p = 0.146). A structured note is better from the moment it is written; it does not decay more slowly.
- **Review is what earns the advantage — supported.** Flanigan et al.'s meta-analysis found the achievement advantage small (Hedges' g = 0.248) and *conditional on the notes being reviewed*; without review it vanishes, even though more volume gets recorded. This is why step 2 ends in the user's review rather than at the agent's output.
- **Expansion buys effort, not proven learning — efficiency-only.** Micronote capture with LLM expansion cut text written ~47% and time ~44% at 93.2% factual correctness (NoTeeline, IUI 2025), but n=12 and the authors state they did **not** measure retention. Treat it as a time saver whose learning cost is unmeasured.
- **Motivation predicted retention; cognitive load did not — supported.** In the same trial, motivation was the strongest predictor (β = 0.50–0.60) while cognitive load showed no significant association. A vault the user abandons teaches nothing, which is why this template stays at two folders.

## Obsidian formatting rules

A few silent failures: the file saves fine but renders broken in Obsidian. Follow these whenever you write a note here.

- **Use soft wrapping, not hard wrapping.** Keep each prose paragraph or list item on one physical line and let Obsidian wrap it visually. Do not insert manual line breaks merely to satisfy a column width. Start a new physical line only for a new paragraph or Markdown structure such as a heading, list item, block quote/callout, table row, or code fence.
- **Frontmatter must be valid YAML and start on line 1** — nothing before the opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid YAML and makes Obsidian render the whole block as raw text. Use a quoted list on one line: `related: ["[[other-note]]", "[[a-summary]]"]`. (The `→ [[…-ex]]` pair link lives in the body, where a bare wikilink is fine.)
- **Quote any frontmatter value that contains a colon** (and values starting with `[`, `{`, `#`, `@`, `` ` ``, `!`, `&`, `*`, `>`, `|`, or a quote). A colon-space inside an unquoted value — most often a lecture title with a subtitle, `source: Lecture 4: Backpropagation` — makes YAML read it as a nested key, so the whole block fails to parse and renders as raw text. Wrap the value in double quotes: `source: "Lecture 4: Backpropagation"`.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table (stray `label]]` leaks into a phantom column). In a table use an unaliased link `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just never inside a table.
- **Inline math in a table must not contain a bare `|` either, and `\|` does not fix it.** The table parser splits the cell on `|` first, so `$d \ll |V|$` fragments into phantom columns. And `\|` is the wrong repair: inside `$...$` it renders as the norm symbol `‖`, silently changing the meaning. Use the LaTeX command for the bar you mean — cardinality / absolute value `|V|` → `$\lvert V\rvert$`, norm `\|x\|` → `$\lVert x\rVert$`, conditional `P(u|v)` → `$P(u \mid v)$`.
- **A bare `$` in prose can open math mode.** A second `$` later on the same line — a price like `$30k … $45k`, "raise $5M" — makes everything between the two render as italicised math. Escape literal dollar signs: `\$30k`.
- **`#` without a trailing space is a tag, not a heading.** `#Results`, `#1`, or a mid-line `#` (e.g. `C#`) silently becomes a tag. Write `# Heading` with a space, or escape it as `\#`.
