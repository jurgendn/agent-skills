# AGENTS.md — PhD Application: <CYCLE / YEAR>

Orientation for any agent operating on this PhD/research-application vault. This
file is the map and the rules; the application craft lives in the installed
`apply-*` skills this file routes to. The vault tracks one application cycle
across many schools.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with
your own default behavior, this file wins, so the vault behaves the same across
agents instead of varying with each one's defaults.

- **This is application-writing work, not coding.** Produce profile notes, CV,
  SOPs, fit notes, and emails. Do **not** write code.
- **Every claim is grounded — never fabricate.** Facts about your record (papers,
  grades, roles) come from `profile/`; facts about a professor or program (recent
  work, lab direction) must cite a real, checkable source. Do not invent a
  publication, a professor's interest, or a program detail — a fabricated fit claim
  is worse than a missing one.
- **Mark uncertainty honestly.** If a fit angle or a professor's current focus is
  inferred rather than confirmed, flag it as tentative in `fit-notes/` rather than
  asserting it in an SOP or email.
- **Check inputs before running a skill; ask for what's missing.** Each skill draws
  from specific folders (see *Routing*). `profile/` is the root source and must be
  populated first. Before running a skill, confirm its input folder(s) actually
  contain the needed documents; if a required input is empty or missing, **stop and
  ask the user to add it (or say where it lives) — do not proceed on an empty folder
  or fabricate the input.** (e.g. `apply-dossier-evaluator` needs a populated
  `profile/` plus the drafted `cv/` and `sop/` it is scoring.)

## What this vault is

A workspace for assembling and tracking a research-application package: a
reusable profile, an academic CV, per-school fit notes and SOPs, outreach
emails, recommender coordination, and a deadline tracker. It optimises for
*reusing one strong profile across many schools* without losing track of
per-school deadlines and tailoring.

## Layout

```text
profile/          # raw inputs: CV/resume, transcripts, research statements,
                  # project writeups, publication list, GitHub summary
cv/               # academic CV drafts (the polished artifact)
sop/              # per-school SOP drafts
fit-notes/        # per-school / per-professor fit evidence
emails/           # cold emails and follow-ups to professors
recommenders/     # recommender list, request emails, packets
references/       # application-components-checklist, sop-structure
_dashboard/       # schools-tracker (deadlines + per-school status)
```

## Filename conventions

```text
sop/          sop-{school}.md            # sop-mit.md
fit-notes/    fit-{school}.md            # fit-mit.md
emails/       email-{prof}-{school}.md   # email-jordan-mit.md
recommenders/ rec-{name}.md             # rec-smith.md
```

Use a short stable slug per school (`mit`, `cmu`, `ethz`) and reuse it across all
folders so a school's materials sort together.

## Routing

| Folder | Skill to use |
|---|---|
| `profile/` | `apply-profile-reader` — run this **first** to build the reusable structured profile |
| `cv/` | `apply-cv-builder` |
| `fit-notes/` | `apply-program-fit-mapper`, `apply-research-direction-mapper` |
| `sop/` | `apply-sop-writer` |
| `emails/` | `apply-cold-email-drafter` |
| `recommenders/` | `apply-recommendation-letter-strategist` |
| pre-submission (coherence) | `apply-package-auditor` |
| scoring / scholarship / eligibility | `apply-dossier-evaluator` |
| feeling stuck | `apply-motivation-keeper` |

Use `flow-phd-application` to orchestrate the whole sequence (profile → CV → fit
→ SOP → recommenders → outreach → audit) when unsure what comes next.

## Default actions

- **Starting the cycle:** run `apply-profile-reader` over `profile/` to produce
  the reusable profile; everything else draws from it.
- **Adding a school:** create its row in `_dashboard/schools-tracker.md`, then
  `fit-notes/fit-{school}.md` (`apply-program-fit-mapper`), then
  `sop/sop-{school}.md` (`apply-sop-writer`) tailored to that fit.
- **Before any submission:** run `apply-package-auditor` across the school's
  materials for coherence and missing evidence; only then mark it ready.
- **Scoring or scholarships:** when you want a graded scorecard, an eligibility
  verdict (e.g. a 4-year BSc against a master's-required EU PhD), or scholarship
  mission fit (VEF/DAAD/Fulbright/Erasmus/MSCA), run `apply-dossier-evaluator`.
  Verify every cutoff, length limit, and deadline against the live official call.

## Rules

- **One profile, many tailorings.** Don't rewrite your story per school; reuse
  the profile and adjust the *fit* and emphasis. Inconsistent claims across SOPs
  are a red flag — `apply-package-auditor` checks for this.
- **Every fit claim is evidenced.** A "fit" with a professor must cite specific
  recent work/lab direction (`apply-research-direction-mapper`), not a vague
  topic match.
- **Deadlines are the master clock.** Keep `_dashboard/schools-tracker.md`
  current; prioritise by deadline, not by enthusiasm.
- **Recommenders need lead time.** Track ask/sent/received per recommender in
  `recommenders/`; chase early, not the week before.

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
