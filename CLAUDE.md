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
- `skills/research-skills/technical-teaching/` contains professor-style technical teaching skills for explaining, deriving, comparing, implementing, and critically analyzing advanced quantitative concepts.
- `skills/research-skills/paper-writing/` contains paper narrative, section writing, discussion-report synthesis, and presentation skills (abstract, intro, method, figures, talk planning).
- `skills/research-skills/review-and-submission/` contains reviewer-response, submission-readiness, and venue-targeting skills.
- `skills/research-skills/artifact-and-reproducibility/` contains reproducibility and artifact release skills.
- `skills/research-skills/applications-and-career/` contains academic-career profile ingestion, PhD application writing, career support, and motivation skills.
- `skills/research-skills/orchestrators/` contains lightweight router/meta-skills that sequence the singleton research skills into a guided workflow with stage gates, delegating the actual work to the singletons rather than duplicating it: `flow-learn-new-topic` (breadth-first onboarding into an unfamiliar area), `flow-deep-understanding` (depth-first mastery of one paper/method/theorem), `flow-idea-to-proof` (raw idea → formal claim → proof design), `flow-paper-lifecycle` (idea → experiments → writing → submission → rebuttal → artifact release), and `flow-phd-application` (profile → CV → fit → SOP → recommenders → outreach → package audit). Orchestrators decide *what next* and which sub-skill to call; they never re-teach what a singleton already does.
- `skills/industrial-rnd/` contains skills for ambiguous industry problem framing, publication-grounded solution design, banking/fintech use-case discovery, and practical pilot/evaluation planning.
- `skills/industrial-rnd/banking/` contains banking and fintech domain-specialized industrial R&D skills.
- `skills/presentation/` contains slide/deck *building* skills that render an approved per-slide spec into an artifact: `deck-design-principles` (shared spec schema + design rules), `deck-beamer-academic` (Beamer for seminar/conference/lecture talks), `deck-beamer-proposal-report` (Beamer for proposals and progress/final reports), and `deck-business-report` (PowerPoint/Canva industrial/executive reports). These are downstream of `research-talk-planner`, which plans a talk's narrative and pacing but does not produce slides.
- `skills/coding-support/` contains coding support skills retained because the user does substantial coding.
- `skills/language-learning/` contains language test preparation skills (IELTS writing, speaking, etc.).
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

## Skill authoring conventions

- Keep one skill focused on one clear capability.
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

## Commands

There is a minimal `package.json` for installing or unlinking skills. There is no build system, linter, or test runner in this repository.

Useful checks for now:

```bash
git status
```

If executable helper scripts are added under `experiments/` or skill-local `scripts/`, document the exact run commands here when they become stable.
