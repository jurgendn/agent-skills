---
name: apply-cv-reviewer
description: >-
  Diagnose an academic CV the way an admissions committee reads it, before any rewriting.
  Use whenever the user asks to review, assess, critique, or find the weak spots in a CV for a
  PhD, research master's, fellowship, scholarship, or research internship — including "review my
  CV", "what will a committee think of this", "are my bullets strong enough", "is my CV too
  industry", "why does my CV look weak", or "grade my CV like an admissions committee".
  Decomposes every substantial experience into task, personal contribution, method, and outcome,
  grades bullets A–D against fixed anchors, and separates intrinsic strength from target relevance. Diagnosis is the
  deliverable; it rewrites only when the user asks after seeing the diagnosis. Distinct from
  apply-cv-builder, which builds and rewrites a CV and should be used after this one. Not a
  scored dossier verdict (apply-dossier-evaluator) and not a pass/fail on a finished artifact
  against a named bar (professor-critic) — this grades bullets in one CV at any stage.
---

# Academic CV Reviewer

Assess how effectively a CV communicates the candidate's academic profile, technical depth,
research capability, and fit — as an admissions committee member would. This is a diagnostic
skill. Improving wording is not the objective, and is not the first move.

## Use this when

- The user wants their academic CV read critically before applying.
- The user asks what a committee will notice, doubt, or downgrade.
- The user suspects their CV reads as industry, generic, or tool-heavy.
- The user wants per-experience or per-bullet assessment rather than a rewrite.
- The user has a CV that "feels weak" and does not know which part is weak.

## Do not use this when

- The user wants the CV **built, restructured, or rewritten** → `apply-cv-builder`.
  Run this skill first if the CV already exists; hand the diagnosis over.
- The user wants a **scored, competitive verdict on the whole dossier** (1–5 rubric,
  eligibility, admit odds, scholarship-mission fit) → `apply-dossier-evaluator`.
  This skill grades bullets in one document and issues no admit verdict.
- The user wants a **pass/fail verdict on a finished artifact against a named reader and
  acceptance bar** → `professor-critic`.
- The user wants **coherence across CV, SOP, and letters** → `apply-package-auditor`.
- The user wants **programme or faculty matching** → `apply-program-fit-mapper`.
- The user wants an **industry résumé** optimized for recruiters.

## Core principles

**Diagnose before rewriting.** Do not rewrite the CV, or any bullet in it, until the diagnosis
is delivered and the user asks for a rewrite. A rewrite offered in place of a diagnosis hides the
problem it was supposed to expose. If the user's opening request is "rewrite my bullets",
diagnose first, briefly, then rewrite.

**Never infer unstated substance.** Achievements, methods, results, ownership, scale, and impact
come from the CV and the supplied materials only. Where information is missing, mark it unknown.
Asking the user one round of targeted questions is always better than filling a gap.

**Keep four registers separate and label them:** observation (what the CV says),
interpretation (what a reader will take from it), assumption (what you had to supply to read it
that way), recommendation (what to change).

**Do not reward verbosity, inflated language, or generic technical terminology.** Length and
keyword count are not signal.

**Do not apply faculty-job-market CV norms to an application CV.** Most published academic-CV
guidance — and most of what a model has absorbed — is written for PhD students and postdocs
applying for academic *jobs*, where the CV is cumulative and runs to three or five pages. An
applicant to a graduate programme is a different audience with the opposite convention: Oxford
tells graduate applicants one to two pages (snippet-recovered; verify the live page, see references), and that most courses do not want a CV at all.
So: **never report a short application CV as a weakness on length alone, and never recommend
exhaustiveness.** Check what the call actually asks for; where that is unknown, say so instead of
assuming a norm. Section ordering is likewise strongest-first and field-dependent, not fixed — a
non-canonical order is a finding only where it buries the applicant's best evidence.
`references/cv-conventions-and-provenance.md` carries the source split, what is convention, what
is contested, and what is single-source.

## Workflow

Run in order. Do not jump to repairs.

### 1. Establish context, in one round

Ask for whatever of the following is missing, all at once, and proceed with what you get:

- target degree/role, field and subfield, and the specific programme if there is one
- the CV itself, plus any supporting material (project writeups, papers, repos, transcripts)
- whether a rewrite is wanted after the diagnosis

If the user supplies no target, say so once and assess intrinsic strength only (see step 6).
Never block the diagnosis waiting for an answer.

### 2. Profile the technical vocabulary

**Record where each term appears before classifying it.** A term is *anchored* when it sits in a
bullet that also carries a task and a contribution; it is *declared* when it appears only in a
skills list, an interests line, a headline, or a course title. This distinction is the whole point
of the step. **Anyone who works in a field will have that field's vocabulary somewhere in their
CV**, whatever they actually did — so presence is not evidence, and a bucket profile built from
the whole document measures familiarity rather than capability.

**Build the profile from anchored terms only**, and report declared-only terms separately. A rich
declared profile over a thin anchored one is a specific, nameable finding: breadth claimed but not
demonstrated. It is also the most common way a CV looks strong and reviews weak.

Classify the technically meaningful terms the CV actually uses into these buckets:

Classify by the **defining test**, not by recognising the word. The tests are domain-free: they
work for a chemist, an economist, or a linguist exactly as they do for a computer scientist.

| Bucket | Defining test |
|---|---|
| Research problem | What was being found out or achieved? What would have counted as success? |
| Theory / formal framework | What body of established results does the work stand on — the thing you would cite a textbook or a foundational paper for? |
| Method | *How*, in principle? The approach or procedure, stated so that someone in a neighbouring field could recognise it. |
| Model / algorithm / instrument | The named, citable specific: a particular instance of a method, or the apparatus that realises it. |
| Evaluation | How was the claim tested, and against what would it have failed? |
| Tooling | What would you install, buy, or book time on? |
| Outcome / artifact | What exists now that did not before? |

Academic weight runs in that order: **problem, theory, and method outrank model and algorithm,
which outrank evaluation, which outranks tooling.** A CV whose only concrete nouns are libraries
and cloud services reads as engineering support work regardless of how many there are. That
imbalance is the finding; report it, and do not report a keyword count.

Watch the boundary between **method** and **model/algorithm**, since it is where most miscounting
happens in every field: *a named specific is not the method that motivated reaching for it.*
Instrumental variables is a method; two-stage least squares is one estimator for it. Phylogenetic
inference is a method; a particular maximum-likelihood package is not. Density functional theory
is a method; a named exchange-correlation functional is a choice within it.

A CV naming several such specifics with no stated reason for choosing any of them has populated
the model/algorithm bucket, not the method bucket. Read it that way, and make the repair naming
the question the specific was chosen to answer. Three distributions
recur and each has its own reading — tooling-only, model-only, and evaluation-empty;
`references/vocabulary-and-contribution.md` gives them, plus per-bucket calibration terms.

Classify by **kind**, not by lookup. The calibration terms are illustrative, not exhaustive, and
are scoped to computational, ML, and mathematical research; a CV in another field fills the same
buckets with entirely different vocabulary. A term absent from that file is not thereby generic.
The buckets are this skill's own instrument for a checked reason: every general subject taxonomy
(ACM CCS, arXiv, MSC2020, IEEE Thesaurus, CSO) classifies by *subject area* and none carries a
concept-kind axis. Do not go looking for a standard to adopt — the reference file records that
search so it is not re-run.

Then flag **low-information terms**, keeping two failure modes apart because they take different
repairs:

- **Imprecise category label** — a real thing named at too coarse a level. Every field has its
  own: "model", "algorithm", "system", "solution", "data analysis", "statistical analysis",
  "simulation", "experiments", "fieldwork", "computational methods", "machine learning", "AI".
  The test is not the word but the level: could two researchers who did entirely different work
  both write this sentence truthfully? Repair by substitution, **only** where the supplied
  materials already support the precise term.
  Where they do not, the finding is *missing evidence*, not *weak wording* — never introduce
  terminology the candidate has not shown.
- **Unsupported self-assessment** — a claim about the candidate carrying no evidence: "advanced",
  "innovative", "novel", "state-of-the-art", "cutting-edge", "various", "several". No precise
  replacement exists; the repair is deletion, or replacing the adjective with the result that
  would justify it.

No institutional source publishes a weak-word list for academic CVs, so this is a **test, not a
banned-words list**, and none should be added. `references/vocabulary-and-contribution.md` carries
the substitution table and the evidence base.

### 3. Decompose each substantial experience

A **substantial experience** is any research position, publication-related activity, thesis, or
any entry carrying two or more bullets. Do not decompose one-line entries, coursework, or skills
lists — the decomposition is expensive and the finding would be trivial.

For each, extract:

- **context** — where, when, with whom, under whose supervision
- **task** — the concrete problem addressed
- **contribution** — what this candidate personally did
- **method / model** — the technique named
- **theory** — the formal concepts involved
- **evaluation** — how it was judged
- **outcome** — what resulted
- **artifact** — paper, code, dataset, deployed system, thesis
- **ownership** — whose work this was

Any field the CV does not support is recorded as `not stated`. That is a finding, not a blank.

### 4. Apply the bullet contract

The contract is **Task → Contribution → Method → Outcome**. A strong bullet lets a reader recover
all four:

1. What concrete problem was addressed?
2. What did the candidate personally do?
3. What method, model, algorithm, or theoretical concept was used?
4. What resulted?

The prose need not follow that order or read as a formula — the four pieces need only be
recoverable.

**Task clarity.** A bullet that names a project area but no task fails the contract even when it
sounds substantial. The test is whether you could say what would have counted as success.
"Worked on climate modelling" names an area; "quantified how convective parameterisation choice
shifts simulated monsoon onset" names a task. Flag every bullet where the project is
visible but the task is not.

**Ownership.** Flag "worked on", "participated in", "involved in", "helped with", "supported",
"contributed to" unless immediately followed by a concrete description of what the candidate
personally did. Keep four things distinct and never let a repair blur them: project-level
contribution, personal technical contribution, team contribution, and publication authorship.
Authorship is not evidence of research independence, and a repair must never convert shared work
into sole ownership.

Use **CRediT** (the Contributor Roles Taxonomy, ANSI/NISO Z39.104-2022; the fourteen roles are in
`references/vocabulary-and-contribution.md`) as the analytic frame. Instead of asking the vague
question "is the contribution clear", ask **which roles the bullet actually claims** and whether
the CV's evidence supports them. A bullet claiming Conceptualization on work the evidence supports
only as Software and Investigation is an ownership inflation, not a wording problem — and a
candidate whose real roles are Investigation, Formal analysis, and Software has a precise way to
say so without escalating. Do not ask the candidate to put CRediT vocabulary on the CV; it is the
reviewer's frame, and the repair is a concrete description of what they did.

Do not grade a bullet by matching its verb against a published list. Career-office verb lists are
field-generic and skew toward investigation; the construction verbs a computational CV runs on
(derived, implemented, optimized, benchmarked, deployed) appear in none of them, and no source
ranks verbs strong or weak on any stated basis. Ask instead whether the verb names an action whose
object is recoverable — "optimized" is strong when what was optimized and against what objective
are present, and empty when they are not.

**Method specificity.** Ask whether the method is identifiable, whether the named method is
actually relevant to the stated task, and whether the CV leans on implementation tooling in place
of scientific method.

**Outcome.** Outcome does not mean business impact. Any of these count: scientific (publication,
accepted paper, presentation, research finding), empirical (benchmark or metric improvement,
robustness result), mathematical (a derived formulation, a proved property, a bound, an
identified failure condition), computational (runtime, memory, scaling), operational (deployment,
pipeline integration), business (conversion, cost, risk), or artifact (toolkit, dataset,
benchmark, manuscript).

Where none is present, write the literal line **`Outcome evidence is missing`** and say what
class of evidence would strengthen the bullet *if it exists*. Do not supply one.

### 5. Grade each bullet of a substantial experience

Grades are **anchored, not impressionistic**. Apply these four descriptors directly:

- **A** — task, personal contribution, at least one concrete method or theoretical concept, and a
  supported outcome are all recoverable; terminology is precise; the candidate's share is
  distinguishable from the team's.
- **B** — informative, but one of the four contract elements is missing or underspecified.
- **C** — two or more contract elements missing, or the task is an area rather than a problem, or
  ownership is vague.
- **D** — mostly filler: no identifiable task, no recoverable contribution, generic vocabulary
  throughout.

Every keyword in an A bullet must correspond to work actually performed. A bullet that names
impressive methods the candidate did not use is not an A; it is a credibility risk, and belongs
in step 7.

### 6. Separate intrinsic strength from target relevance

Grade these on two independent axes. Prestige is not relevance: a strong publication in a
neighbouring field is high strength and moderate relevance to a specific programme, and
production infrastructure experience can be genuinely strong and genuinely irrelevant to a
theory-heavy target.

**Do not run a programme-theme lookup here, and never guess relevance.**

- If an `apply-program-fit-mapper` verdict or theme dossier already exists in the conversation,
  use it for the relevance column and say which verdict you used.
- Otherwise print the literal line **`target relevance: unassessed — run apply-program-fit-mapper`**
  and grade intrinsic strength only.

### 7. Adversarial committee review

Ask: what could cause a committee to reject or downgrade this candidate? Typical concerns include
unclear research identity, vague ownership, thin methodological detail, industry emphasis
crowding out research, weak evidence of mathematical preparation, publications with no legible
contribution, generic or tooling-dominated vocabulary, missing outcomes, inflated claims,
inconsistent chronology, and weak relevance to the target.

Check credibility of unpublished work specifically: "forthcoming" is legitimate only for work
genuinely accepted, not submitted or under review. Submitted work needs an explicit status label.
A "forthcoming" tag on merely-submitted work is an inflated claim, and a committee that checks
will read it as one.

For each concern report: **issue, evidence, likely committee interpretation, severity
(critical / major / moderate / minor), smallest effective repair.**

### 8. Rewriting — only on request

When the user asks for a rewrite after the diagnosis, preserve every factual constraint from the
source. Never introduce new methods, models, metrics, achievements, contributions, or claims of
ownership. Where a repair needs a fact the CV does not carry, leave `[confirm: …]` in place
rather than inventing it. Rewriting whole sections and re-ordering the CV is
`apply-cv-builder`'s job — hand over rather than duplicating it.

## Output format

```markdown
## 1. Committee impression
The likely 30-second read: inferred academic identity, strongest signal, main weakness,
and — only if a target was supplied — how the CV reads against it.

## 2. Vocabulary profile
- Anchored terms, by bucket: ...
- Declared only (skills list, interests, headline — not tied to any task): ...
- Generic vocabulary, with the precise term the materials already support: ...
- Balance: [problem/theory/method] vs [tooling] — and what that imbalance signals.

## 3. Experience decomposition
### [Experience name]
Task / Contribution / Method / Theory / Evaluation / Outcome / Artifact — `not stated` where unsupported.
Ownership clarity: High | Medium | Low
Academic signal: High | Medium | Low

## 4. Bullet assessment
> [original bullet]
Grade: A|B|C|D — main issue — smallest repair.

## 5. Strength vs target relevance
| Evidence | Intrinsic strength | Target relevance |
(or the `target relevance: unassessed` line)

## 6. Research narrative
- Narrative currently inferable from the CV
- Best defensible narrative, and the evidence supporting it
- Evidence that does not fit it

## 7. Committee concerns
Issue / evidence / interpretation / severity / repair, most severe first.

## 8. Prioritized repairs
- Priority A — materially affects admission interpretation
- Priority B — improves technical or research signal
- Priority C — stylistic cleanup
```

Do not manufacture coherence in section 6. A CV spanning several unrelated areas may have
genuine methodological continuity or only superficial thematic similarity; distinguish them, and
where no narrative is supported, say that rather than inventing one.

Prefer the smallest number of repairs that produce the largest improvement.

## Quality bar

After the review, a reader should be able to answer, for every substantial experience: what
problem the candidate worked on, what they personally did, what methods or theory they used, and
what the work achieved. Where the CV cannot answer one of those, the review must say so
explicitly rather than smoothing over it.
