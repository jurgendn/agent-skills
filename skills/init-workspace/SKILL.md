---
name: init-workspace
description: Initialize a structured Obsidian-style workspace for a specific kind of work — scaffolds the folder tree, a heavy operating-manual AGENTS.md, seeded reference material, and a Dataview dashboard. Use whenever the user wants to set up, start, initialize, scaffold, or bootstrap a new project/vault/workspace for one of these work types: learning a new topic, IELTS practice, writing a research paper, a PhD application, a talk/presentation, or a theory/proof project. Triggers on phrasings like "set up a workspace for X", "start a new paper project", "scaffold an IELTS vault", "initialize a folder for learning X", "bootstrap my PhD application folder", "create a project structure for my talk/proof". This skill WRITES files, so it always confirms the project type and target directory before scaffolding. It does not do the downstream work (marking essays, writing sections, proving theorems) — it lays down the structure and an AGENTS.md that routes the agent to the right skills.
---

# init-workspace

Scaffold a ready-to-work project from a fixed menu of heavy, self-contained
templates. Each template is a complete operating manual: a folder tree, an
`AGENTS.md` that documents the layout and routes work to the right skills,
workspace-local `references/`, and an Obsidian `_dashboard/` (Dataview).

## When to use

The user wants to **start** a project and have the structure + conventions laid
down for them. Trigger on "set up / start / initialize / scaffold / bootstrap a
workspace/vault/project for …".

## When NOT to use

- The user wants the actual downstream work (mark this essay, write my intro,
  prove this lemma). Route to the domain skill, not here.
- The project already exists and is structured — this skill scaffolds, it does
  not reorganize. (Re-running is safe — see *Merge rules* — but it won't
  restructure an existing layout.)
- For structuring an experiment **codebase** (source layout for fast hypothesis
  testing), use `research-codebase`. The `paper` template here is the *writing*
  vault and defers code structure to that skill.

## Template menu

| Type | Use it for | First skill the AGENTS.md routes to |
|---|---|---|
| `learn-a-topic` | Breadth-first onboarding into an unfamiliar area | `flow-learn-new-topic` |
| `ielts` | IELTS Writing practice loop (attempts → feedback → progress) | `ielts-learning-planner` |
| `paper` | One research paper, idea → submission → artifact | `paper-argument-planner` |
| `phd-application` | A full PhD/research application cycle | `flow-phd-application` |
| `talk` | A talk/presentation, narrative → slides | `research-talk-planner` |
| `theory` | A theory/proof project, claim → proof → stress-test | `flow-idea-to-proof` |

The `ielts` template ships **AGENTS.md only** (plus folders + dashboard): the
installed `ielts-*` skills already carry the band descriptors and feedback
aggregation, so the vault doesn't duplicate them. Every other template seeds its
own `references/` so the workspace is self-contained.

## Procedure

1. **Determine the type.** Match the user's intent to one menu entry. If it's
   ambiguous (or they said "a project" generically), ask which type — do not
   guess.
2. **Confirm the target directory.** Default to the current directory. Because
   this skill writes files, state where you are about to scaffold and confirm
   before writing.
3. **Read the template.** Open `templates/<type>/AGENTS.md` — its *Layout*
   section is the authoritative folder list.
4. **Create the folder tree.** Make every folder in the Layout, adding a
   `.gitkeep` to any that starts empty.
5. **Copy the seeded files.** Copy the template's `AGENTS.md`, `references/`,
   and `_dashboard/` into the target (see *Merge rules*).
6. **Fill the one-line title.** Replace the project-title placeholder at the top
   of the copied `AGENTS.md` with the user's project name if they gave one;
   otherwise leave the placeholder.
7. **Report.** List what was created and name the first skill to run (the table
   above), so the user knows the next move.

## Merge rules

Re-running on an existing directory is safe: **merge, never overwrite.**

- Create missing folders; leave existing ones untouched.
- Copy a seeded file only if no file of that name already exists at the
  destination. Never clobber an existing `AGENTS.md`, reference, dashboard, or
  any content file — those may hold the user's work.
- If `AGENTS.md` already exists, do not replace it; report that the workspace
  already has one and stop touching it.

## Notes

- Templates assume an **Obsidian vault** (YAML frontmatter, `[[wikilinks]]`,
  `_dashboard/` Dataview). The folders are plain folders, so a code editor works
  too; only the dashboard is Obsidian-specific.
- Templates are intentionally **heavy and zero-config**: they work as-is with no
  customization beyond the project title. Don't interrogate the user for details
  at init time.
- This skill is self-contained: every template lives under `templates/` here.
