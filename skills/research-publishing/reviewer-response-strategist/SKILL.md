---
name: reviewer-response-strategist
description: Plan rebuttals, reviewer responses, and revision strategies for research papers. Use this skill whenever the user shares peer reviews, reviewer concerns, meta-review text, acceptance/rejection feedback, or asks how to respond to Reviewer 2, what experiments to run for rebuttal, what to concede, how to phrase a response, or how to prioritize limited rebuttal space. This skill focuses on strategy and response structure; use results-writeup for writing new result prose after the strategy is decided.
---

# Reviewer Response Strategist

A good rebuttal does not try to win every sentence. It identifies which reviewer beliefs must change, which concerns are valid, and what evidence or wording can change the outcome.

## Use this when

- The user has reviews and needs a response plan.
- The user must decide which requested experiments to run.
- A reviewer misunderstood the paper and the response must be calibrated.
- The user needs to concede a limitation without collapsing the contribution.
- The user is preparing a rebuttal, revision letter, or response-to-reviewers document.

## Do not use this when

- The user only needs a Results section or technical report. Use `results-writeup`.
- The user needs to redesign the whole paper argument. Use `paper-argument-planner`.
- The user needs to verify reproducibility or artifact release readiness.

## Workflow

### 1. Parse the review set

For each reviewer, extract:

- score or recommendation if provided
- main concerns
- minor concerns
- misunderstandings
- requested experiments
- tone and confidence
- likely deal-breakers

Separate what the reviewer explicitly said from your interpretation.

### 2. Classify each concern

Use these categories:

- **Misunderstanding** — paper already answers it, but not clearly enough.
- **Missing evidence** — concern is valid and needs experiment, proof, analysis, or citation.
- **Scope/limitation** — valid boundary that should be acknowledged and framed.
- **Novelty concern** — reviewer doubts the contribution relative to prior work.
- **Evaluation concern** — baselines, metrics, datasets, seeds, statistics, or fairness.
- **Writing/clarity issue** — fixable by reorganization or wording.
- **Potentially fatal flaw** — threatens the central claim if true.

Do not dismiss a concern just because the reviewer is blunt. Extract the decision-relevant issue.

### 3. Prioritize response effort

Rank concerns by outcome impact:

1. Concerns shared by multiple reviewers.
2. Concerns tied to low scores or explicit rejection reasons.
3. Concerns the authors can answer with strong existing evidence.
4. Feasible new experiments or analyses.
5. Minor writing issues.

Do not spend scarce rebuttal space on low-impact defenses.

### 4. Choose a response move

For each concern, choose one:

- **Clarify** — point to existing evidence and say how the paper will be revised.
- **Concede and bound** — acknowledge limitation while preserving the supported claim.
- **Add evidence** — run or report a targeted experiment/analysis.
- **Correct misconception** — explain precisely where the reviewer's premise differs from the paper.
- **Reframe contribution** — narrow or sharpen the claim.
- **Defer** — explicitly mark as future work when not central.

The best response is often a concession plus a narrow defense.

### 5. Draft response skeletons

Use this structure:

```text
We thank the reviewer for [specific concern].
The concern is [valid/misunderstanding/partially valid] because [reason].
Our evidence is [result/citation/analysis], which shows [bounded claim].
We will revise the paper by [specific change].
```

Avoid defensive language, reviewer blame, or vague promises.

## Output format

```markdown
# Reviewer Response Plan

## Overall strategy

## Concern triage
| Reviewer | Concern | Category | Priority | Response move | Evidence/action |
|---|---|---|---|---|---|

## Experiments or analyses to prioritize

## Draft response bullets

## Claims to narrow or concede

## Revision checklist
```

## Quality bar

A good response plan makes it obvious which reviewer beliefs can realistically be changed and which claims should be narrowed before they become liabilities.
