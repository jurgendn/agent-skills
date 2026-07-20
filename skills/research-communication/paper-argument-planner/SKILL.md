---
name: paper-argument-planner
description: Plan the argument of a research paper from an idea, partial draft, experiment results, notes, or reviewer-facing story. Use this skill whenever the user asks how to structure a paper, clarify the contribution, build a paper outline, connect claims to evidence, decide what belongs in each section, turn results into a coherent narrative, or diagnose why a paper feels unfocused. This skill should trigger before drafting full prose when the paper's thesis, claim hierarchy, or section logic is not yet stable.
---

# Paper Argument Planner

A paper is not a list of experiments. It is an argument that a reader can follow, object to, and eventually believe. This skill helps turn research material into that argument before drafting prose.

## Use this when

- The user has an idea, result set, outline, abstract, or rough draft and asks how to make it into a paper.
- The contribution is unclear or too broad.
- Experiments exist but the story does not.
- The user needs to decide what each section should prove.
- The paper has too many claims, disconnected tables, or weak motivation.

## Do not use this for

- Polishing finished prose sentence by sentence. Use a writing/editing skill instead.
- Writing a source-grounded literature survey. Use `literature-triangulation` or `related-work-writer`.
- Checking whether results are reproducible. Use `reproducibility-audit`.
- Strategic rebuttal to reviewers. Use `reviewer-response-strategist`.

## Workflow

### 1. Extract the raw material

Identify, without embellishing:

- Problem: what is hard, missing, or misunderstood?
- Proposed idea or method: what did the authors do?
- Evidence: what results, proofs, ablations, or analyses exist?
- Audience: which community must be convinced?
- Constraint: venue, page limit, deadline, available experiments.

If these are missing, ask targeted questions instead of inventing them.

### 2. State the argument spine

Write the paper's argument in this form:

```text
Because [problem/gap], we need [capability or understanding].
Existing work fails because [specific limitation].
This paper contributes [method/claim/analysis].
The key evidence is [main result + supporting result + stress test].
Therefore readers should believe [bounded conclusion].
```

The spine should be narrow enough that one paper can actually support it.

### 3. Separate claims by strength

Classify each claim:

- **Main claim** — the paper lives or dies on this.
- **Supporting claim** — needed to make the main claim believable.
- **Mechanism claim** — explains why the method works.
- **Scope claim** — where it works and where it does not.
- **Speculative claim** — interesting but not established; move to discussion or remove.

For each claim, require evidence. If evidence is missing, mark it explicitly.

### 4. Build the section logic

Create a section plan where every section has a job:

- **Abstract** — compressed problem, contribution, evidence, implication.
- **Introduction** — why the problem matters, what gap exists, what this paper proves.
- **Related Work** — how prior work creates the gap or contrast.
- **Method / Theory** — what is new enough to understand the contribution.
- **Experiments / Results** — evidence for each claim, in order of importance.
- **Analysis / Ablations** — why the result happens and what alternatives fail.
- **Limitations** — bounded honesty, not self-sabotage.
- **Conclusion** — what changed after reading the paper.

Do not include a section just because papers usually have one. Include it because it performs a necessary role in the argument.

### 5. Plan figures and tables as evidence

For each proposed figure or table, specify:

- claim it supports
- expected reader takeaway
- required comparison or control
- whether it belongs in main paper or appendix

Decorative figures are liabilities. If a figure does not support a claim, cut it or move it to appendix.

### 6. Stress-test reader objections

List the strongest likely objections:

- novelty objection
- baseline fairness objection
- generality/scope objection
- mechanism objection
- missing ablation objection
- reproducibility objection

For each, say whether the current paper answers it with evidence, prose, or neither.

## Output format

Use this structure:

```markdown
# Paper Argument Plan

## One-sentence thesis

## Argument spine

## Claim hierarchy
| Claim | Type | Evidence | Status |
|---|---|---|---|

## Section plan

## Figure/table plan
| Artifact | Claim supported | Takeaway | Main/appendix |
|---|---|---|---|

## Weak spots

## Next actions
```

## Quality bar

A good plan should make the paper easier to reject or accept. If the argument is vague enough that no experiment could falsify it, sharpen it before writing prose.
