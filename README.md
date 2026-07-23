# agent-skills

A focused collection of agent skills for research, industrial R&D, paper writing, PhD applications, language learning, presentation and slides, implementation-heavy coding work, and structured project setup.

## Start here

- Never used agent skills before? Follow the
  [five-minute first-skill walkthrough](GUIDE.md#your-first-skill-in-five-minutes).
- Already comfortable with installation? Continue through the
  [beginner guide](GUIDE.md) for design philosophy, role boundaries, and useful
  end-to-end flows.
- Want the rationale behind the skill boundaries? Read
  [DESIGN-PHILOSOPHY.md](DESIGN-PHILOSOPHY.md).
- Looking for one specific skill? Jump to the [skill catalog](#skill-catalog).

## Install

The wrapper scripts in `scripts/` install skills via the official `skills` CLI. Skills are filed one level deep by category — `skills/<category>/<skill>/` — which the CLI discovers by default; installation flattens them to the bare skill name. For example, `skills/learning-and-metacognition/knowledge-debt-audit/` installs as `knowledge-debt-audit`.

**Prerequisite:** Node.js — the scripts call `npx` and exit with an error if it is not found.

Install all skills:

```bash
# Linux/macOS
./scripts/install.sh
```

```powershell
# Windows PowerShell
.\scripts\install.ps1
```

```bat
:: Windows Command Prompt (forwards arguments to install.ps1)
scripts\install.bat
```

Install a single skill (or a glob):

```bash
./scripts/install.sh --skill ielts-writing-task2
```

```powershell
.\scripts\install.ps1 -Skill ielts-writing-task2
```

### Options

| Purpose | `install.sh` | `install.ps1` / `install.bat` |
| --- | --- | --- |
| Skill name or glob to install (default `*`) | `--skill NAME` | `-Skill NAME` |
| Install from a different repository URL | `--repo URL` | `-Repo URL` |
| Show help | `-h`, `--help` | — |

By default the installers call the skills CLI with nested discovery enabled:

```bash
npx skills add https://github.com/jurgendn/agent-skills.git --skill '*'
```

Every skill lives at `skills/<category>/<skill>/`, which the CLI discovers by default — no extra flags needed.

## Skill catalog

### Research discovery

- `research-discovery/cross-domain-analogy-finder` — find a concept's structural twin in a distant field to borrow a portable solution (offense) or check whether the idea already exists under another name (defense), gated by a four-way classifier and an import-a-result test.
- `research-discovery/gap-finder` — surface publishable theoretical gaps in papers and run a weekly lemma autopsy that weakens one hypothesis before consulting the authors' discussion.
- `research-discovery/gap-motivation-builder` — Socratically build the motivation case for filling a found gap (consequence, beneficiary, blocker, timeliness, payoff), deliver a motivation verdict, and derive the desiderata any solution must satisfy — without proposing the method.
- `research-discovery/paper-idea-and-scope-brainstormer` — brainstorm a research idea and scope what a new paper should cover.
- `research-discovery/research-idea-stress-test` — stress-test novelty, assumptions, confounders, and cheap decisive experiments.

### Research evidence

- `research-evidence/citation-auditor` — verify citations are real, claims match what cited papers actually say, and no references are hallucinated or misattributed.
- `research-evidence/literature-triangulation` — build source-grounded maps of a research area.
- `research-evidence/related-work-writer` — turn an existing source map into Related Work prose.
- `research-evidence/survey-paper-writer` — plan, draft, and revise standalone survey, tutorial, review, and perspective papers.

### Research reasoning

- `research-reasoning/argument-audit` — interactively and Socratically check whether stated evidence or premises establish a claim in a proof, essay, research conclusion, or everyday argument; converges to a validity verdict plus the smallest fix or counterexample.
- `research-reasoning/theorem-and-claim-audit` — pressure-test paper claims and mathematical arguments.
- `research-reasoning/theory-assumption-extractor` — surface the assumptions a theorem or method actually relies on.
- `research-reasoning/theory-counterexample-hunter` — hunt for the smallest witness that breaks a claim.
- `research-reasoning/theory-formalism-translator` — translate between formalisms without losing the content of a claim.
- `research-reasoning/theory-paper-to-theorem-distiller` — distill a paper down to its load-bearing theorem statements.
- `research-reasoning/theory-proof-sketcher` — sketch a proof architecture before committing to full details.
- `research-reasoning/theory-to-toy-cases` — turn abstract ideas into minimal examples and sanity checks.

### Research experimentation

- `research-experimentation/benchmark-and-baseline-selector` — recommend the MINIMAL vs SUGGESTED baselines and benchmarks a claim needs to be credible.
- `research-experimentation/experiment-design` — design minimal, decision-relevant experiments, and diagnose runs that already went wrong (symptom classification, data-path audit before model blame, mechanism-wise tuning, scaling-curve fitting via `scripts/fit_scaling_law.py`).
- `research-experimentation/hypothesis-and-ablation-planner` — isolate mechanisms with targeted ablations.
- `research-experimentation/model-eval-error-analysis` — inspect model failures beyond aggregate metrics.
- `research-experimentation/statistical-testing-guide` — choose the right test, compute effect sizes, plan seed counts, and report statistics correctly.

### Research engineering

- `research-engineering/jax-training-recipe` — turn a paper idea into an implementable JAX/Flax/Optax training recipe.
- `research-engineering/paper-to-code` — reproduce a paper with no released code in minimal PyTorch and verify the method works via staged gates.
- `research-engineering/pytorch-training-recipe` — turn a paper idea into an implementable PyTorch training recipe.
- `research-engineering/research-codebase` — structure research code for fast hypothesis testing and command-to-result traceability.

### Research communication

- `research-communication/abstract-and-intro-writer` — draft or revise the abstract and introduction as a matched pair.
- `research-communication/discussion-report-synthesizer` — synthesize fragmented academic conversations into cohesive markdown reports.
- `research-communication/figure-table-planner` — plan figures, tables, captions, and main-vs-appendix evidence.
- `research-communication/method-section-writer` — draft or revise the method section with consistent notation, motivation-first structure, and correct level of detail.
- `research-communication/paper-argument-planner` — plan the central thesis, contribution framing, and claim-to-evidence spine.
- `research-communication/research-proposal-writer` — write or refine a forward-looking research proposal: a multi-year PhD research plan for a prospective supervisor or fellowship, or a next-paper pitch to your advisor.
- `research-communication/research-talk-planner` — structure a conference talk, seminar, or job talk from a paper or set of results.
- `research-communication/results-writeup` — write calibrated Results, Experiments, Discussion, lab notes, and technical reports from verified findings.

### Research publishing

- `research-publishing/artifact-release-packager` — plan code/data/model artifact release packages.
- `research-publishing/peer-review-writer` — write a peer review of someone else's paper: evidenced weaknesses, calibrated scores, constructive questions; also PC-member / area-chair process (bidding, COI, subreviewers, discussion).
- `research-publishing/reproducibility-audit` — test whether results can actually be reproduced from available materials.
- `research-publishing/reviewer-response-strategist` — plan rebuttals, concessions, response structure, and revision priorities.
- `research-publishing/submission-readiness-audit` — run a final pre-submission risk audit.
- `research-publishing/venue-targeting` — select and prioritize publication venues; plan resubmission strategy after rejection.

### Research workflows

- `research-workflows/flow-deep-understanding` — depth-first mastery of one paper, method, or theorem.
- `research-workflows/flow-idea-to-proof` — raw idea → formal claim → defensible proof design.
- `research-workflows/flow-learn-new-topic` — breadth-first onboarding into an unfamiliar research area.
- `research-workflows/flow-paper-lifecycle` — idea → experiments → writing → submission → rebuttal → artifact release.
- `research-workflows/flow-phd-application` — profile → CV → fit → SOP → recommenders → outreach → package audit.

### Learning and metacognition

- `learning-and-metacognition/concept-exercise-generator` — generate a graded easy-to-advanced exercise set with separated solutions to verify understanding, using misconception-coded distractors and intuitive-trap verification items when appropriate.
- `learning-and-metacognition/knowledge-debt-audit` — call toxic AI-assisted knowledge debt before it compounds, then schedule variable-cue re-probes at expanding intervals after repayment.
- `learning-and-metacognition/naive-student` — let the user teach an honest novice whose earned confusion and fallible playback expose underspecified dependencies without silently repairing them.
- `learning-and-metacognition/professor-critic` — critique a finished artifact the way its specific named reader would, returning a verdict-first (ACCEPT/MAJOR REVISION/REJECT) teardown with a FATAL/MAJOR/MINOR severity ladder; requires a named reader and acceptance bar, refuses to grade blind or judge mid-draft work.
- `learning-and-metacognition/professor-mentor-technical-teaching` — explain advanced technical topics with professor-style intuition, rigor, implementation grounding, and critical judgment.
- `learning-and-metacognition/whiteboard-peer` — co-solve unfinished research ideas with one committed partial attempt and mandatory counterpressure per turn, while refusing to take over the full solution.

### Academic career

- `academic-career/apply-cold-email-drafter` — draft, critique, and revise concise cold emails to professors and PIs.
- `academic-career/apply-cv-builder` — build and audit academic CVs for PhD, research master's, fellowship, internship, RA, and lab applications.
- `academic-career/apply-dossier-evaluator` — score a further-education dossier (PhD, master's, scholarship, internship) on a reproducible 11-dimension rubric, with eligibility and scholarship-program (VEF/DAAD/Fulbright/Erasmus/MSCA) fit.
- `academic-career/apply-motivation-keeper` — recover motivation, reframe setbacks, and rebuild momentum through rejection, stagnation, imposter syndrome, and burnout.
- `academic-career/apply-package-auditor` — audit the full application package for coherence, missing evidence, risk, and deadline priorities.
- `academic-career/apply-profile-reader` — read academic-career profile folders/files and extract reusable evidence for SOPs, CVs, fit mapping, emails, and application audits.
- `academic-career/apply-program-fit-mapper` — map applicant interests to programs, faculty, labs, and school-specific fit evidence.
- `academic-career/apply-recommendation-letter-strategist` — choose recommenders, plan letter strategy, draft requests, and prepare recommender packets.
- `academic-career/apply-research-direction-mapper` — define a professor's recent and trending research direction for fit notes, SOPs, and outreach.
- `academic-career/apply-sop-writer` — write, review, and iterate PhD application Statements of Purpose and research-fit essays.

### Industrial R&D

- `industrial-rnd/banking-ai-literature-mapper` — map banking AI publications, cases, benchmarks, methods, and evaluation patterns.
- `industrial-rnd/banking-use-case-discovery` — discover and prioritize banking/fintech AI and R&D use cases.
- `industrial-rnd/industry-problem-framing` — convert vague industry problems into researchable, pilotable R&D problem statements.
- `industrial-rnd/pilot-and-evaluation-design` — design practical pilots, baselines, metrics, guardrails, and go/no-go criteria.
- `industrial-rnd/publication-grounded-solution-design` — design solution directions grounded in prior successful cases, publications, and transfer assumptions.

### Presentation and slides

- `presentation/deck-beamer-academic` — compile-ready LaTeX Beamer decks for academic talks, seminars, conferences, defenses, and lectures.
- `presentation/deck-beamer-proposal-report` — compile-ready LaTeX Beamer decks for research proposals, progress reports, milestone reviews, and final reports.
- `presentation/deck-business-report` — PowerPoint/Canva business report decks for executives, managers, clients, pilots, and stakeholder updates.

### Test preparation

- `test-prep/gre-issue-essay` — draft, score (0–6 rubric), and improve GRE Analytical Writing "Analyze an Issue" essays across all six instruction stems.
- `test-prep/gre-learning-planner` — build personalised GRE study plans with section allocation, a daily vocabulary pipeline, practice-test milestones, and application-deadline scheduling.
- `test-prep/gre-quant-coach` — coach GRE Quantitative Reasoning: quantitative-comparison tactics, careless-error elimination, content-gap triage, pacing.
- `test-prep/gre-reading-comprehension` — coach GRE Reading Comprehension and paragraph-argument questions: passage mapping, wrong-answer taxonomy, line-reference discipline, timed drilling.
- `test-prep/gre-verbal-reasoning` — coach GRE Text Completion and Sentence Equivalence: predict-then-match method, trap taxonomy, practice generation, and miss classification.
- `test-prep/gre-vocabulary-builder` — build and retain GRE vocabulary via meaning clusters, charge, secondary meanings, and spaced cloze drills in TC/SE contexts.
- `test-prep/ielts-grammar-coach` — estimate an IELTS **Grammatical Range & Accuracy** band, then diagnose and durably fix the recurring errors holding it down via coded corrective feedback, Vietnamese-L1 contrastive diagnosis, a persistent error ledger with spaced re-probes, and targeted drills; also a general-English (no-band) mode. Isolates GRA — for a whole-task band across all four criteria use `ielts-writing-task2` / `ielts-speaking-coach`.
- `test-prep/ielts-learning-planner` — build personalised IELTS study plans and progress routines.
- `test-prep/ielts-progress-reporter` — aggregate a practice vault's marked `feedback/*.md` files into periodic progress reports (band trends, recurring errors, revision gains).
- `test-prep/ielts-reading-strategies` — teach and practise IELTS Reading strategies and question types.
- `test-prep/ielts-speaking-coach` — simulate, score, and improve IELTS Speaking Parts 1–3.
- `test-prep/ielts-vocabulary-builder` — build and apply IELTS-relevant vocabulary for Writing, Speaking, and Reading.
- `test-prep/ielts-writing-task1` — draft, analyse, score, and improve IELTS Academic Writing Task 1 reports.
- `test-prep/ielts-writing-task2` — draft, analyse, score, and improve IELTS Writing Task 2 essays.

### Coding support

- `coding-support/prompting-claude-models` — prompt/system-prompt/agent design for Claude-backed features; grounds volatile model-specific behavior in the live Anthropic docs.

### Project setup (entrypoint)

- `init-workspace` — scaffold a non-coding, note-centric Obsidian workspace for learning, ongoing research notes, research writing, academic applications, talks, test preparation, theory, or similar knowledge work. Every result gets a folder tree plus an operating-manual `AGENTS.md`; workspace-local `references/` and a Dataview dashboard are included when the selected template or intake warrants them. One short intake batch includes target-directory confirmation, then the skill uses one of seven ready templates as-is (`ielts`, `paper`, `phd-application`, `research-notebook`, `talk`, `theory`, `learn-a-topic`), adapts the closest one while keeping its contract consistent, or writes a lean bespoke vault. Seeded prose keeps each paragraph or list item on one physical line and relies on Obsidian soft wrapping. The skill never scaffolds software/code projects, writes into the repository templates, or overwrites existing vault files.

## Repository policy

This repository prioritizes skills that support research, paper writing, PhD applications, language learning, reproducibility, and research implementation. Generic or low-priority skills should be removed rather than archived when they dilute that purpose.

Keep skills narrow and activation-oriented. When two skills overlap, their frontmatter descriptions should explain which one should trigger.
