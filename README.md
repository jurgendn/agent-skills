# agent-skills

A focused collection of agent skills for research, industrial R&D, paper writing, PhD applications, language learning, presentation and slides, implementation-heavy coding work, and structured project setup.

## Install

This repository keeps skills nested by topic, but installation unnests them into flat skill directories. For example, `skills/research-skills/technical-teaching/knowledge-debt-audit/` installs as `knowledge-debt-audit`.

Linux/macOS:

```bash
./scripts/install.sh
```

Windows PowerShell:

```powershell
.\scripts\install.ps1
```

Windows Command Prompt:

```bat
scripts\install.bat
```

Install one skill:

```bash
./scripts/install.sh --skill ielts-writing-task2
```

The installers call the official skills CLI with nested discovery enabled:

```bash
npx skills add https://github.com/jurgendn/agent-skills.git --skill '*' --full-depth
```

Use `--no-full-depth` only if you intentionally do not want nested skill discovery.

## Skill catalog

### Idea and positioning

- `research-skills/idea-and-positioning/research-idea-stress-test` — stress-test novelty, assumptions, confounders, and cheap decisive experiments.
- `research-skills/idea-and-positioning/paper-idea-and-scope-brainstormer` — brainstorm a research idea and scope what a new paper should cover.
- `research-skills/idea-and-positioning/cross-domain-analogy-finder` — find a concept's structural twin in a distant field to borrow a portable solution (offense) or check whether the idea already exists under another name (defense), gated by a four-way classifier and an import-a-result test.

### Literature and related work

- `research-skills/literature-triangulation` — build source-grounded maps of a research area.
- `research-skills/literature-and-related-work/related-work-writer` — turn an existing source map into Related Work prose.
- `research-skills/literature-and-related-work/citation-auditor` — verify citations are real, claims match what cited papers actually say, and no references are hallucinated or misattributed.

### Experiment design and analysis

- `research-skills/experiment-design-and-analysis/experiment-design` — design minimal, decision-relevant experiments.
- `research-skills/experiment-design-and-analysis/hypothesis-and-ablation-planner` — isolate mechanisms with targeted ablations.
- `research-skills/experiment-design-and-analysis/model-eval-error-analysis` — inspect model failures beyond aggregate metrics.
- `research-skills/experiment-design-and-analysis/statistical-testing-guide` — choose the right test, compute effect sizes, plan seed counts, and report statistics correctly.
- `research-skills/experiment-design-and-analysis/deep-learning-experimentation/*` — specialist diagnostics for data pipelines, training runs, scaling, probes, hyperparameters, and experiment traces.

### Implementation support

- `research-codebase` — structure research code for fast hypothesis testing and command-to-result traceability.
- `research-skills/implementation-support/pytorch-training-recipe` — turn a paper idea into an implementable PyTorch training recipe.
- `research-skills/implementation-support/jax-training-recipe` — turn a paper idea into an implementable JAX/Flax/Optax training recipe.

### Theory and claims

- `research-skills/theory-and-claims/gap-finder` — surface publishable theoretical gaps in papers, including hidden assumptions, loose bounds, missing guarantees, and uncovered settings.
- `research-skills/theory-and-claims/theorem-and-claim-audit` — pressure-test paper claims and mathematical arguments.
- `research-skills/theory-and-claims/theory-to-toy-cases` — turn abstract ideas into minimal examples and sanity checks.
- `research-skills/theory-and-claims/theory-heavy-math-ml/*` — specialist support for assumptions, counterexamples, derivations, formalism translation, theorem distillation, and proof sketches.

### Technical teaching

- `research-skills/technical-teaching/professor-mentor-technical-teaching` — explain advanced technical topics with professor-style intuition, rigor, implementation grounding, and critical judgment.
- `research-skills/technical-teaching/concept-exercise-generator` — generate a graded easy-to-advanced exercise set with separated solutions to verify understanding.
- `research-skills/technical-teaching/knowledge-debt-audit` — at the moment of building on an AI-produced result, probe whether the user actually understands the load-bearing step, and call toxic knowledge debt before it compounds.

### Paper writing

- `research-skills/paper-writing/paper-argument-planner` — plan the central thesis, contribution framing, and claim-to-evidence spine.
- `research-skills/paper-writing/abstract-and-intro-writer` — draft or revise the abstract and introduction as a matched pair.
- `research-skills/paper-writing/method-section-writer` — draft or revise the method section with consistent notation, motivation-first structure, and correct level of detail.
- `research-skills/paper-writing/discussion-report-synthesizer` — synthesize fragmented academic conversations into cohesive markdown reports.
- `research-skills/results-writeup` — write calibrated Results, Experiments, Discussion, lab notes, and technical reports from verified findings.
- `research-skills/paper-writing/figure-table-planner` — plan figures, tables, captions, and main-vs-appendix evidence.
- `research-skills/paper-writing/research-talk-planner` — structure a conference talk, seminar, or job talk from a paper or set of results.

### Review and submission

- `research-skills/review-and-submission/reviewer-response-strategist` — plan rebuttals, concessions, response structure, and revision priorities.
- `research-skills/review-and-submission/submission-readiness-audit` — run a final pre-submission risk audit.
- `research-skills/review-and-submission/venue-targeting` — select and prioritize publication venues; plan resubmission strategy after rejection.

### Artifact and reproducibility

- `research-skills/artifact-and-reproducibility/reproducibility-audit` — test whether results can actually be reproduced from available materials.
- `research-skills/artifact-and-reproducibility/artifact-release-packager` — plan code/data/model artifact release packages.

### Applications and career

- `research-skills/applications-and-career/apply-profile-reader` — read academic-career profile folders/files and extract reusable evidence for SOPs, CVs, fit mapping, emails, and application audits.
- `research-skills/applications-and-career/apply-sop-writer` — write, review, and iterate PhD application Statements of Purpose and research-fit essays.
- `research-skills/applications-and-career/apply-cv-builder` — build and audit academic CVs for PhD, research master's, fellowship, internship, RA, and lab applications.
- `research-skills/applications-and-career/apply-program-fit-mapper` — map applicant interests to programs, faculty, labs, and school-specific fit evidence.
- `research-skills/applications-and-career/apply-research-direction-mapper` — define a professor's recent and trending research direction for fit notes, SOPs, and outreach.
- `research-skills/applications-and-career/apply-cold-email-drafter` — draft, critique, and revise concise cold emails to professors and PIs.
- `research-skills/applications-and-career/apply-recommendation-letter-strategist` — choose recommenders, plan letter strategy, draft requests, and prepare recommender packets.
- `research-skills/applications-and-career/apply-package-auditor` — audit the full application package for coherence, missing evidence, risk, and deadline priorities.
- `research-skills/applications-and-career/apply-dossier-evaluator` — score a further-education dossier (PhD, master's, scholarship, internship) on a reproducible 11-dimension rubric, with eligibility and scholarship-program (VEF/DAAD/Fulbright/Erasmus/MSCA) fit.
- `research-skills/applications-and-career/apply-motivation-keeper` — recover motivation, reframe setbacks, and rebuild momentum through rejection, stagnation, imposter syndrome, and burnout.

### Orchestrators

Lightweight routers that sequence the singleton research skills into a guided workflow with stage gates; they decide *what next* and delegate the work to the singletons.

- `research-skills/orchestrators/flow-learn-new-topic` — breadth-first onboarding into an unfamiliar research area.
- `research-skills/orchestrators/flow-deep-understanding` — depth-first mastery of one paper, method, or theorem.
- `research-skills/orchestrators/flow-idea-to-proof` — raw idea → formal claim → defensible proof design.
- `research-skills/orchestrators/flow-paper-lifecycle` — idea → experiments → writing → submission → rebuttal → artifact release.
- `research-skills/orchestrators/flow-phd-application` — profile → CV → fit → SOP → recommenders → outreach → package audit.

### Industrial R&D

- `industrial-rnd/industry-problem-framing` — convert vague industry problems into researchable, pilotable R&D problem statements.
- `industrial-rnd/publication-grounded-solution-design` — design solution directions grounded in prior successful cases, publications, and transfer assumptions.
- `industrial-rnd/pilot-and-evaluation-design` — design practical pilots, baselines, metrics, guardrails, and go/no-go criteria.
- `industrial-rnd/banking/banking-use-case-discovery` — discover and prioritize banking/fintech AI and R&D use cases.
- `industrial-rnd/banking/banking-ai-literature-mapper` — map banking AI publications, cases, benchmarks, methods, and evaluation patterns.

### Coding support

- `coding-support/debugging-strategies` — systematic debugging support.
- `coding-support/python-code-style` — Python style and linting guidance.
- `coding-support/python-design-patterns` — Python design/refactoring guidance.
- `coding-support/python-performance-optimization` — Python profiling and performance guidance.
- `coding-support/python-testing-patterns` — Python testing guidance.

### Language learning

- `language-learning/ielts-writing-task1` — draft, analyse, score, and improve IELTS Academic Writing Task 1 reports.
- `language-learning/ielts-writing-task2` — draft, analyse, score, and improve IELTS Writing Task 2 essays.
- `language-learning/ielts-speaking-coach` — simulate, score, and improve IELTS Speaking Parts 1–3.
- `language-learning/ielts-reading-strategies` — teach and practise IELTS Reading strategies and question types.
- `language-learning/ielts-vocabulary-builder` — build and apply IELTS-relevant vocabulary for Writing, Speaking, and Reading.
- `language-learning/ielts-learning-planner` — build personalised IELTS study plans and progress routines.
- `language-learning/ielts-progress-reporter` — aggregate a practice vault's marked `feedback/*.md` files into periodic progress reports (band trends, recurring errors, revision gains).

### Presentation and slides

- `presentation/deck-design-principles` — shared slide-spec schema and design rules (one-signal-per-slide, claim-titles, hierarchy, density) reused by the format-specific builders.
- `presentation/deck-beamer-academic` — compile-ready LaTeX Beamer decks for academic talks, seminars, conferences, defenses, and lectures.
- `presentation/deck-beamer-proposal-report` — compile-ready LaTeX Beamer decks for research proposals, progress reports, milestone reviews, and final reports.
- `presentation/deck-business-report` — PowerPoint/Canva business report decks for executives, managers, clients, pilots, and stakeholder updates.

### Project setup

- `init-workspace` — scaffold a structured Obsidian-style workspace for a chosen work type (`ielts`, `paper`, `phd-application`, `talk`, `theory`, `learn-a-topic`): folder tree + an operating-manual `AGENTS.md` that routes work to the relevant skills + workspace-local `references/` + a Dataview dashboard. Confirms type and target directory first; merges (never overwrites) on re-run.

## Repository policy

This repository prioritizes skills that support research, paper writing, PhD applications, language learning, reproducibility, and research implementation. Generic or low-priority skills should be removed rather than archived when they dilute that purpose.

Keep skills narrow and activation-oriented. When two skills overlap, their frontmatter descriptions should explain which one should trigger.
