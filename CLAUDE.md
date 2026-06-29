# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This repository is for authoring and collecting agent skills focused on research workflows, industrial R&D, paper writing, PhD applications, language test preparation, presentation/deck building, and implementation-heavy coding work. Skills should help agents support research ideation, literature grounding, industry problem framing, solution design, pilot evaluation, implementation, reproducibility, paper writing, reviewer response, artifact release, research-oriented applications, IELTS preparation, slide/deck production, and coding support.

Generic coding-support skills are allowed when they materially support research implementation. Generic README, architecture, slide, or meta-discovery skills should not be added unless they directly support research, industrial R&D, paper production, PhD applications, language test preparation, presentation/deck building, or coding-heavy research work.

## Structure

- `skills/` contains individual skills. Each skill should live in its own directory and include a `SKILL.md` file.
- `skills/research-skills/` contains research lifecycle, paper-writing, application, and artifact skills.
- `skills/research-skills/idea-and-positioning/` contains early-stage research framing skills.
- `skills/research-skills/literature-and-related-work/` contains literature mapping, Related Work writing, and citation verification skills.
- `skills/research-skills/experiment-design-and-analysis/` contains experiment design, benchmark/baseline selection, statistical testing, evaluation, and deep-learning experimentation skills.
- `skills/research-skills/implementation-support/` contains implementation recipes for research experiments (PyTorch, JAX, etc.).
- `skills/research-skills/theory-and-claims/` contains theorem, claim, proof, theory-heavy, and paper-gap-finding skills.
- `skills/research-skills/technical-teaching/` contains professor-style technical teaching skills for explaining, deriving, comparing, implementing, and critically analyzing advanced quantitative concepts. It also contains `concept-exercise-generator`, which produces a graded easy-to-advanced exercise set (emitted as a separate `exercises.md` plus `solutions.md` with self-check rubrics) to *verify* understanding rather than teach it; the learning orchestrators (e.g. `flow-learn-new-topic`) hand off to it at each stage's exit gate.
- `skills/research-skills/paper-writing/` contains paper narrative, section writing, discussion-report synthesis, and presentation skills (abstract, intro, method, figures, talk planning).
- `skills/research-skills/review-and-submission/` contains reviewer-response, submission-readiness, and venue-targeting skills.
- `skills/research-skills/artifact-and-reproducibility/` contains reproducibility and artifact release skills.
- `skills/research-skills/applications-and-career/` contains academic-career profile ingestion, PhD application writing, dossier scoring/eligibility evaluation, career support, and motivation skills. Note the deliberate split between `apply-package-auditor` (qualitative coherence/readiness audit, no scores) and `apply-dossier-evaluator` (reproducible 1–5 rubric across 11 dimensions, eligibility gate, and scholarship-program fit for VEF/DAAD/Fulbright/Erasmus/MSCA); each disambiguates against the other in its `description`. `apply-dossier-evaluator` bakes in a strict volatility split — stable structural logic only, with deadlines/cutoffs/score-minimums/word-limits/funding routed to a "verify against the live official call" instruction rather than committed as authoritative, and faculty/lab fit fetched live per run (no cached professor file).
- `skills/research-skills/orchestrators/` contains lightweight router/meta-skills that sequence the singleton research skills into a guided workflow with stage gates, delegating the actual work to the singletons rather than duplicating it: `flow-learn-new-topic` (breadth-first onboarding into an unfamiliar area), `flow-deep-understanding` (depth-first mastery of one paper/method/theorem), `flow-idea-to-proof` (raw idea → formal claim → proof design), `flow-paper-lifecycle` (idea → experiments → writing → submission → rebuttal → artifact release), and `flow-phd-application` (profile → CV → fit → SOP → recommenders → outreach → package audit, plus a *conditional* route to `apply-dossier-evaluator` for graded scoring, cross-border eligibility, or scholarship-mission fit — situational, not a linear stage). Orchestrators decide *what next* and which sub-skill to call; they never re-teach what a singleton already does.
- `skills/industrial-rnd/` contains skills for ambiguous industry problem framing, publication-grounded solution design, banking/fintech use-case discovery, and practical pilot/evaluation planning.
- `skills/industrial-rnd/banking/` contains banking and fintech domain-specialized industrial R&D skills.
- `skills/presentation/` contains slide/deck *building* skills that render an approved per-slide spec into an artifact: `deck-design-principles` (shared spec schema + design rules), `deck-beamer-academic` (Beamer for seminar/conference/lecture talks), `deck-beamer-proposal-report` (Beamer for proposals and progress/final reports), and `deck-business-report` (PowerPoint/Canva industrial/executive reports). These are downstream of `research-talk-planner`, which plans a talk's narrative and pacing but does not produce slides.
- `skills/coding-support/` contains coding support skills retained because the user does substantial coding.
- `skills/language-learning/` contains language test preparation skills (IELTS writing, speaking, etc.), including `ielts-progress-reporter`, which aggregates a practice vault's marked `feedback/*.md` files into periodic progress reports (band trends, recurring errors, revision gains) rather than marking individual drafts. The IELTS scoring skills each carry their own `references/ielts-band-descriptors.md` scoped to that skill (`ielts-writing-task1`, `ielts-writing-task2`, `ielts-speaking-coach`, and `ielts-learning-planner`); there is no shared band-descriptor file.
- `skills/init-workspace/` is a top-level project-setup skill that scaffolds a structured Obsidian-style workspace for a chosen work type. It ships one heavy, self-contained template per type under `templates/<type>/` (each = a folder tree + an operating-manual `AGENTS.md` that routes work to the relevant skills + workspace-local `references/` + a Dataview `_dashboard/`). Templates: `ielts`, `paper`, `phd-application`, `talk`, `theory`, `learn-a-topic`. The `ielts` template ships AGENTS.md + dashboard only because the installed `ielts-*` skills already carry the band descriptors and feedback aggregation; the other five seed their own references. The skill writes files, so it confirms type + target directory first and merges (never overwrites) on re-run. Each template's AGENTS.md opens with an `## Operating contract` (read-this-first block whose rules override the agent's own defaults) that makes the vault behave the same across agents (Claude Code, Codex, Feynman) rather than varying with each one's biases: research-not-coding, source-grounded synthesis, explicitly marked uncertainty, and a check-inputs-before-running rule (confirm a skill's input folder is actually populated; if a required input is missing, stop and ask the user rather than proceeding on an empty folder or fabricating it). The five skill-routing templates (`paper`, `theory`, `learn-a-topic`, `talk`, `phd-application`) all carry this input-precondition rule, each adapted to its own root-input folder; `ielts` (marking-only) does not — keep the rule present across those five when editing it. The four research-pipeline agents (`researcher → reviewer → verifier → writer`) live once, generalized and agent-portable, at `templates/_shared/agents/` (single source of truth, no per-template duplication); at scaffold time they are copied into `<vault>/agents/` for the **full-pipeline** templates only (`paper`, `theory`, `learn-a-topic`), whose Operating contract runs work through the four stages. `talk`, `phd-application`, and `ielts` use the lighter grounding-only contract and get no `agents/` folder. The skill also writes a one-line `<vault>/CLAUDE.md` containing `@AGENTS.md` so Claude Code auto-loads the contract via import while `AGENTS.md` stays the single source of truth (inert for agents that read AGENTS.md natively). Every template's AGENTS.md ends with an `## Obsidian formatting rules` section (frontmatter must be valid YAML starting on line 1, wikilinks in frontmatter must be a quoted list, no raw `|` in table cells) so the notes the agent later authors don't render corrupted; keep that block in sync across all six templates when editing it.
- `skills/research-codebase/` and similar top-level skills are allowed when they support the whole research codebase rather than one paper stage.
- `templates/skill-template/` is for reusable starter material when creating new skills.
- `experiments/` is for shell scripts or prompt variants used to test skill behavior.
- `results/` is for saved evaluations or notes about which skill behavior worked.

Recommended skill layout:

```text
skills/<category>/<skill-name>/
├── SKILL.md
├── examples/    # optional calibration examples
├── evals/       # optional test prompts or evaluation metadata
└── scripts/     # optional helpers the skill actually uses
```

## Skill taxonomy

Use this taxonomy when adding or reorganizing skills:

1. Idea and positioning
2. Literature and related work
3. Experiment design and analysis
4. Implementation support
5. Theory and claims
6. Technical teaching
7. Paper writing
8. Review and submission
9. Artifact and reproducibility
10. Applications and career
11. Industrial R&D
12. Coding support
13. Language learning
14. Presentation and slides
15. Project setup (workspace scaffolding)

## Skill authoring conventions

- Keep one skill focused on one clear capability.
- Keep each skill self-contained: a skill must not depend on resources outside its own directory, and skills must not share files or link into each other (e.g. no `../references/…` cross-references). When several skills need the same reference material, give each its own copy scoped to that skill rather than pointing them at a shared directory.
- Put activation guidance in the frontmatter `description`; agents use this to decide when to load the skill. Do not use a separate `when_to_use` frontmatter key — it is not read by agents. Merge all triggering guidance into `description`.
- Make descriptions specific and slightly pushy about when to use the skill, including common user phrasings.
- Group tight "pick-one" skill families with a short, domain-derived name prefix so siblings sort together and read as one suite: `apply-*` (PhD/career applications), `flow-*` (orchestrators/routers), `deck-*` (slide/deck builders), `theory-*` (theory-heavy math/ML tools), plus the existing `ielts-*`, `python-*`, and `banking-*`. Do not prefix the broad research singletons — their directory already conveys the category, and prefixing all of them adds churn without aiding triggering (agents match on `description`, not name).
- Prefer procedural guidance: when to use the skill, when not to use it, the process to follow, and the expected output format.
- When two skills overlap, disambiguate in the frontmatter description and body. For example, field mapping belongs to `literature-triangulation`, while polished Related Work prose belongs to `related-work-writer`.
- Add `examples/` only when examples materially improve calibration.
- Add `scripts/` only when repeated manual work justifies a helper script.
- Add `evals/evals.json` for new skills when realistic test prompts will help evaluate triggering or output quality.
- Avoid broad scaffolding until there is real content for it.
- Remove low-priority or redundant skills instead of archiving them, unless they support the user's research, PhD application, or coding workflows.
- Do not vendor a `skill-creator` skill into this repo. Creating, editing, and evaluating skills uses Claude Code's built-in skill-creator, which ships the full eval/benchmark tooling; a repo-local clone only duplicates the `name`, shadows the built-in, and goes stale (a prior clone carried only `SKILL.md` while referencing scripts/agents/references it did not include).

## Commands

There is a minimal `package.json` for installing or unlinking skills. There is no build system, linter, or test runner in this repository.

Useful checks for now:

```bash
git status
```

If executable helper scripts are added under `experiments/` or skill-local `scripts/`, document the exact run commands here when they become stable.
