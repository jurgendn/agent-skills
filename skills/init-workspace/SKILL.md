---
name: init-workspace
description: 'Initialize a structured Obsidian-style workspace for a specific kind of work — scaffolds the folder tree, a heavy operating-manual AGENTS.md, seeded reference material, and a Dataview dashboard. Use whenever the user wants to set up, start, initialize, scaffold, or bootstrap a new project/vault/workspace for one of these work types: learning a new topic, IELTS practice, writing a research paper, a PhD application, a talk/presentation, or a theory/proof project. Triggers on phrasings like "set up a workspace for X", "start a new paper project", "scaffold an IELTS vault", "initialize a folder for learning X", "bootstrap my PhD application folder", "create a project structure for my talk/proof". This skill WRITES files, so it always confirms the project type and target directory before scaffolding. It does not do the downstream work (marking essays, writing sections, proving theorems) — it lays down the structure and an AGENTS.md that routes the agent to the right skills.'
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
| `paper` | One research paper, idea → submission → artifact | `flow-paper-lifecycle` |
| `phd-application` | A full PhD/research application cycle | `flow-phd-application` |
| `talk` | A talk/presentation, narrative → slides | `research-talk-planner` |
| `theory` | A theory/proof project, claim → proof → stress-test | `flow-idea-to-proof` |

The `ielts` template ships **AGENTS.md only** (plus folders + dashboard): the
installed `ielts-*` skills already carry the band descriptors and feedback
aggregation, so the vault doesn't duplicate them. Every other template seeds its
own `references/` so the workspace is self-contained.

### Shared research agents

The four research-pipeline agents — `researcher → reviewer → verifier → writer` —
are identical across templates, so they live once at `templates/_shared/agents/`
(the single source of truth) rather than being duplicated per template. They are
generalized and agent-portable: they describe each stage's job, integrity rules,
and output contract without binding to a particular runtime's tools. At scaffold
time they are copied into the vault at `<vault>/agents/`, so the workspace stays
self-contained and portable.

Only the **full-pipeline** templates get the `agents/` folder: `paper`, `theory`,
and `learn-a-topic`. Their `AGENTS.md` *Operating contract* references the four
stages as the default for any non-trivial research artifact. The `talk`,
`phd-application`, and `ielts` templates use a **lighter grounding-only contract**
(no-code + source-grounded + mark-uncertainty, without the four named stages), so
they do **not** receive the `agents/` folder.

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
   and `_dashboard/` into the target (see *Merge rules*). For the full-pipeline
   templates only (`paper`, `theory`, `learn-a-topic`), also copy
   `templates/_shared/agents/` into `<vault>/agents/` so the research pipeline
   travels with the vault. `talk`, `phd-application`, and `ielts` use the lighter
   grounding-only contract and get no `agents/` folder.
6. **Write the entry-file stub.** Write `<vault>/CLAUDE.md` containing exactly
   one line, `@AGENTS.md`. This makes the operating contract auto-load on Claude
   Code (which reads `CLAUDE.md` and follows `@` imports) while staying inert for
   agents that read `AGENTS.md` natively (Codex, etc.) — so `AGENTS.md` remains
   the single source of truth and the vault behaves the same on every runtime. Do
   this for every template, including `ielts`. (See *Merge rules* — never clobber
   an existing `CLAUDE.md`.)
7. **Fill the one-line title.** Replace the project-title placeholder at the top
   of the copied `AGENTS.md` with the user's project name if they gave one;
   otherwise leave the placeholder.
8. **Report.** List what was created and name the first skill to run (the table
   above), so the user knows the next move.

## Merge rules

Re-running on an existing directory is safe: **merge, never overwrite.**

- Create missing folders; leave existing ones untouched.
- Copy a seeded file only if no file of that name already exists at the
  destination. Never clobber an existing `AGENTS.md`, reference, dashboard,
  `agents/` file, or any content file — those may hold the user's work or edits.
- If `AGENTS.md` already exists, do not replace it; report that the workspace
  already has one and stop touching it.
- If `CLAUDE.md` already exists, do not replace it — the user may have their own
  imports or memory there. If it does not already pull in `AGENTS.md`, report
  that so the user can add `@AGENTS.md` themselves.

## Notes

- Templates assume an **Obsidian vault** (YAML frontmatter, `[[wikilinks]]`,
  `_dashboard/` Dataview). The folders are plain folders, so a code editor works
  too; only the dashboard is Obsidian-specific.
- Templates are intentionally **heavy and zero-config**: they work as-is with no
  customization beyond the project title. Don't interrogate the user for details
  at init time.
- This skill is self-contained: every template lives under `templates/` here.
