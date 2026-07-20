# Beginner Guide to `agent-skills`

An **AI agent** is an AI assistant that can read files, use tools, and follow
multi-step instructions. A **skill** is a small folder of instructions that teaches
the agent how to perform one specialized job consistently. Installing a skill does
not train a new model; it gives your existing agent a reusable operating procedure.

This repository contains those procedures. It is designed for skill-compatible
agents such as Claude Code, Codex, Cursor, and other clients supported by the open
[`skills` CLI](https://github.com/vercel-labs/skills#supported-agents).

## Your first skill in five minutes

This walkthrough installs one skill and uses it once. You do not need to clone this
repository.

### 1. Check the prerequisites

You need:

- a skill-compatible AI agent installed and working;
- [Node.js](https://nodejs.org/en/download), which provides the `npx` command;
- a terminal: Terminal on macOS/Linux or PowerShell on Windows.

If you do not already use an AI coding agent, pause here. First choose one from the
[`skills` CLI supported-agent list](https://github.com/vercel-labs/skills#supported-agents),
install it from its official instructions, and confirm that you can start a normal
chat or coding session. Then return to this guide. This repository installs skills
into an existing agent; it does not create the agent account or client for you.

Open the terminal and run:

```bash
node --version
npx --version
```

If both commands print version numbers, continue. If either command is not found,
install Node.js, close and reopen the terminal, then try again.

### 2. Preview the available skills

Run:

```bash
npx skills add https://github.com/jurgendn/agent-skills.git --list --full-depth
```

This lists the skills without installing them. `--full-depth` is required because
this repository organizes skills into nested categories.

### 3. Install one skill

Start with the guided learning flow:

```bash
npx skills add https://github.com/jurgendn/agent-skills.git \
  --skill flow-learn-new-topic \
  --full-depth \
  --global
```

On Windows PowerShell, enter the same command on one line:

```powershell
npx skills add https://github.com/jurgendn/agent-skills.git --skill flow-learn-new-topic --full-depth --global
```

The installer detects compatible agents and may ask where to install the skill.
Select the AI client you actually use. Global installation makes the skill available
across projects. The installer may also ask whether to use a symlink or copy; choose
the recommended default unless your environment prohibits symlinks.

Verify the result:

```bash
npx skills list --global
```

You should see `flow-learn-new-topic`.

### 4. Open or restart your AI agent

Some clients discover newly installed skills only when a session starts. Restart the
client or open a new session after installation.

Enter this prompt:

```text
Use $flow-learn-new-topic to help me learn graph neural networks.
I know basic linear algebra and Python, but I am new to graph machine learning.
My goal is to understand enough to read an introductory paper.
I can study for three hours this week.
```

The `$flow-learn-new-topic` text names the skill explicitly. If your client does not
recognize `$` invocation, write:

```text
Use the flow-learn-new-topic skill to help me learn graph neural networks.
```

### 5. Check that it worked

A successful first response should not dump a complete course immediately. It should
first locate your starting point by confirming or asking about:

- the exact topic;
- what you already know;
- what you need the knowledge for;
- your available time.

It should then propose the next stage, such as orienting the field or mapping the
literature. Continue answering normally; the flow will route later stages to more
specialized skills.

### Attaching your own material

When a skill needs a paper, draft, codebase, or folder:

- attach the file using your client's file control; or
- give the agent the file path when it can access your local workspace; or
- paste a short excerpt directly into the conversation.

State what the material is and what outcome you want. Do not upload passwords,
private keys, confidential datasets, or material you are not authorized to share.

### Troubleshooting the first run

| Problem | What to do |
|---|---|
| `npx: command not found` | Install Node.js, then reopen the terminal. |
| The repository reports no skills | Include `--full-depth` and use the full repository URL shown above. |
| The skill is not listed after installation | Run `npx skills list --global`; reinstall and select the correct AI client. |
| The agent ignores `$flow-learn-new-topic` | Restart the agent, then say “Use the flow-learn-new-topic skill…” in plain text. |
| Installation reports a permission or symlink error | Retry in a writable directory or choose copy instead of symlink when prompted. |
| You do not know which skill to install | Start with one of the flows in the next section; do not install everything immediately. |

The installer and its supported-client list can change. Check the
[`skills` CLI documentation](https://www.skills.sh/docs/cli) if its prompts differ
from this walkthrough.

## How the ecosystem is organized

This repository is not a collection of interchangeable prompts. It is a system of
small specialist roles connected by explicit hand-offs. After the first successful
run, the main decision is:

> Do I need one focused operation, or a guided multi-stage flow?

Use a **singleton skill** for one well-defined task. Use a **flow** when you know the
goal but do not yet know which specialist should act first.

## Choose your next skill

Choose the row closest to your goal:

| I want to… | Start with |
|---|---|
| Learn an unfamiliar research area | `$flow-learn-new-topic` |
| Master one paper, theorem, or method | `$flow-deep-understanding` |
| Turn a research hunch into a theorem or proof plan | `$flow-idea-to-proof` |
| Develop a paper from idea through submission | `$flow-paper-lifecycle` |
| Build a complete PhD application package | `$flow-phd-application` |
| Find and frame an industry AI/R&D problem | `$industry-problem-framing` |
| Work on one IELTS skill | The corresponding `ielts-*` skill |
| Create a structured workspace | `$init-workspace` |

Example:

```text
Use $flow-deep-understanding to help me master this paper.
I understand the main claim, but the proof becomes unclear at Lemma 3.
My goal is to defend it at an advisor meeting next week.
```

If the task is already precise, invoke the singleton directly:

```text
Use $theorem-and-claim-audit to check this derivation line by line.
```

## The mental model

The ecosystem has four layers.

### 1. Flows decide what happens next

Flows are lightweight orchestrators. They locate the current stage, call the right
singleton, enforce exit gates, and route failures backward.

They do not duplicate the specialist work. For example,
`flow-deep-understanding` may route through technical teaching, assumption
extraction, toy cases, counterexample hunting, and teach-back.

### 2. Singletons perform one job

Each singleton has a narrow contract:

- `literature-triangulation` maps evidence;
- `gap-finder` finds theoretical gaps in an existing paper;
- `experiment-design` designs a decision-relevant experiment;
- `results-writeup` turns verified findings into calibrated prose;
- `reproducibility-audit` checks whether an artifact can actually be reproduced.

Narrow boundaries make outputs easier to audit and prevent a single agreeable
assistant from pretending to be researcher, teacher, reviewer, and grader at once.

### 3. Roles match the maturity of the work

The technical-teaching family is intentionally stage-specific:

| Role | Use it when | It must not become |
|---|---|---|
| `professor-mentor-technical-teaching` | Material is new and needs explanation | A grader |
| `naive-student` | You want to expose gaps by teaching | A hidden expert who repairs your explanation |
| `whiteboard-peer` | The idea is unfinished and needs a co-solver | A full-solution dispenser |
| `concept-exercise-generator` | You need graded verification practice | A first lecture |
| `knowledge-debt-audit` | You are building on AI output you may not own | A trivia quiz |
| `professor-critic` | The artifact is finished and has a real reader | A brainstorming partner |

Choosing the wrong maturity stage is a common failure. A harsh verdict on an
unfinished idea is premature; a friendly brainstorm on a submission-ready proof is
too weak.

### 4. Hand-offs connect the system

A skill should stop when another skill owns the next operation. Typical hand-offs:

- a literature map becomes Related Work through `related-work-writer`;
- a suspected false claim moves to `theory-counterexample-hunter`;
- an unfinished idea moves from `whiteboard-peer` to `flow-idea-to-proof`;
- a finished artifact moves to `professor-critic`;
- an understanding gap moves to teaching, exercises, or teach-back;
- verified results move to `results-writeup`.

Do not invoke five specialists simultaneously unless their jobs are genuinely
independent. Let one produce the evidence or artifact the next one needs.

## Design philosophy

### Small skills over universal experts

Every skill should have a clear firing condition, a clear non-goal, and an explicit
output contract. Overlap is resolved in the skill descriptions rather than left to
guesswork.

### Motivation first, then assumptions, then formalism

Technical explanations begin with why the object exists and what pressure created
it. Formal definitions follow once the learner knows what work they must perform.

### Evidence before synthesis

Literature claims should be traceable to primary sources. The system separates:

- what a source reports;
- what the agent infers;
- what remains unresolved.

Use `literature-triangulation` before building an argument on a remembered
consensus, and `citation-auditor` before trusting a finished bibliography.

### Gates are demonstrated, not declared

Understanding is checked through derivation, prediction, counterexamples,
teach-back, or graded exercises. “This makes sense” is not an exit gate.

### AI output can create knowledge debt

Finishing work and owning the reasoning are different outcomes.
`knowledge-debt-audit` interrupts when an AI-produced step becomes load-bearing,
then schedules variable-cue re-probes after repayment.

### Criticism targets artifacts, not people

Audits and reviews may be strict, but issues must be checkable. The artifact can
overclaim, omit an assumption, or fail a reader's bar; the author is not the defect.

For the longer rationale and references behind these design choices, see
[DESIGN-PHILOSOPHY.md](DESIGN-PHILOSOPHY.md).

## Useful flows

### Flow A — Learn a new research area

Start with `$flow-learn-new-topic`.

```text
Orient
  → map the literature
  → build core intuition
  → work toy cases
  → read primary sources
  → teach the map back
```

Use this when breadth is the bottleneck. Once one paper or theorem becomes the
bottleneck, switch to `$flow-deep-understanding`.

### Flow B — Master one paper or theorem

Start with `$flow-deep-understanding`.

```text
reconstruct the reasoning
  → extract assumptions
  → verify the mechanism
  → stress-test boundaries
  → re-derive and teach it cold
```

This flow is appropriate when you already know the vocabulary but cannot yet
reproduce or criticize the object unaided.

### Flow C — Turn a hunch into a proof plan

Start with `$flow-idea-to-proof`.

```text
whiteboard the hunch
  → stress-test the idea
  → extract required premises
  → state the formal claim
  → sketch the proof
  → attack the claim and derivation
```

Use `$whiteboard-peer` alone when you are still exploring. Enter the full flow once
there is a candidate mechanism or claim.

### Flow D — Develop a research paper

Start with `$flow-paper-lifecycle`.

The flow routes across idea framing, literature, experiments, implementation,
evaluation, paper argument, section writing, submission audit, reviewer response,
and artifact release. Start at the current stage; do not restart completed work.

### Flow E — Build a PhD application

Start with `$flow-phd-application`.

The flow sequences profile extraction, CV, program/faculty fit, SOP, recommenders,
outreach, and package audit. Use `apply-dossier-evaluator` only when reproducible
scoring, formal eligibility, or scholarship-mission fit is needed.

### Flow F — Move from an industry problem to a pilot

Use this sequence:

```text
$industry-problem-framing
  → $publication-grounded-solution-design
  → $pilot-and-evaluation-design
```

For banking and fintech, begin with `$banking-use-case-discovery` when the business
problem itself is still unclear.

### Flow G — Run an IELTS improvement loop

Use the task skill for practice and marking, then use the progress tools:

```text
$ielts-writing-task1 or $ielts-writing-task2
  → revise from feedback
  → $ielts-progress-reporter
  → $ielts-learning-planner
```

The progress reporter brings older errors back on a spaced schedule; it does not
remark new essays.

## How to write a useful request

Provide five pieces of context when available:

1. **Goal:** what outcome you need.
2. **Current state:** novice, partial attempt, finished artifact, or existing data.
3. **Object:** paper, proof, code, dataset, draft, or folder.
4. **Constraints:** deadline, venue, compute, audience, or allowed tools.
5. **Acceptance bar:** what would count as done.

Example:

```text
Use $professor-critic on this finished abstract.
Reader: a skeptical NeurIPS reviewer familiar with the competing method.
Acceptance bar: no claim should justify rejection or demand a new experiment.
Artifact: <abstract>
```

## Common routing mistakes

- Using `professor-critic` on a half-formed idea. Use `whiteboard-peer`.
- Asking `whiteboard-peer` for a complete solution. Leave the peer protocol.
- Using `gap-finder` to write a venue review. Use `peer-review-writer`.
- Using `related-work-writer` before collecting sources. Use
  `literature-triangulation`.
- Using `concept-exercise-generator` to teach unfamiliar material. Use the
  professor-mentor first.
- Treating `submission-readiness-audit` and `professor-critic` as synonyms. The
  former audits a paper package; the latter predicts one named reader's verdict.
- Asking an orchestrator to rerun stages you have already completed. State your
  current stage and provide the existing artifacts.

## Recommended first session

If you are exploring the repository rather than solving an immediate task:

1. Pick one real goal from the start table.
2. Invoke one flow with your current state and acceptance bar.
3. Let it route to a singleton.
4. Inspect the singleton's output contract and “when not to fire” section.
5. Save the resulting artifact or next-step decision.

The full inventory remains in [README.md](README.md). Start with the guide and use
the catalog only when you need a specialist the flow has not already selected.
