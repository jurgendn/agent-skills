---
name: publication-grounded-solution-design
description: Design industry R&D solution directions grounded in prior successful cases, academic papers, technical reports, and credible industry publications. Use whenever the user has a vague business, banking, fintech, enterprise, or operational problem and wants to brainstorm methods, draft a theoretically motivated solution, compare solution families, or justify a proposal with publications instead of unsupported intuition. Also use when the user asks for "prior successful cases", "paper-backed solutions", "method draft", "research-backed proposal", or "what has worked before" for an applied industry problem.
---

# Publication-Grounded Solution Design

Turn an ambiguous industry problem into a set of defensible solution directions backed by literature, prior deployments, and an evaluation plan.

The goal is not to produce a generic AI idea list. The goal is to identify methods that have credible precedent, explain why they might transfer, and expose what still needs to be validated in the user's setting.

## When to use this skill

Use this skill when the user wants to:
- brainstorm solutions for a vague industry or R&D problem;
- draft a method section for an internal proposal;
- ground a proposed solution in papers, case studies, or technical reports;
- compare ML, optimization, LLM, rules-based, workflow, or data-product approaches;
- identify what evidence is strong enough to justify a pilot.

If the user only wants a broad research map, use `literature-triangulation` first. If the user already has a specific method and needs an experiment, use `experiment-design` or `pilot-and-evaluation-design`.

## Workflow

### 1. Frame the industry problem precisely

Extract or ask for:
- business process or decision being improved;
- target users and stakeholders;
- current pain point;
- available data or expected signals;
- operational constraints such as latency, explainability, compliance, cost, human review, and integration;
- what success would change in practice.

Write the problem in this form:

```text
For [stakeholder/process], improve [decision/workflow/outcome] by using [available signals/interventions], subject to [constraints], measured by [business and technical metrics].
```

If the problem remains vague, state the missing information rather than inventing it.

### 2. Search for precedent by problem shape

Search by underlying problem type, not only by domain labels.

Examples:
- "reduce manual review burden" → triage, human-in-the-loop prioritization, active learning, decision support;
- "detect suspicious behavior" → anomaly detection, graph fraud detection, weak supervision, sequential pattern mining;
- "understand customer intent" → representation learning, retrieval, segmentation, next-best-action, causal uplift;
- "automate document work" → document AI, information extraction, retrieval-augmented generation, verification workflows.

Prioritize:
1. peer-reviewed papers and arXiv papers with experiments;
2. benchmark or dataset papers;
3. official system papers and technical reports;
4. credible industry case studies with concrete metrics;
5. surveys only as maps, not final evidence.

### 3. Build a precedent table

For each relevant source, capture:

| Source | Problem matched | Method | Evidence | Setting | Transferability | Caveats |
|---|---|---|---|---|---|---|

Transferability should mention what must be true for the result to apply to the user's environment.

Examples:
- similar data granularity;
- similar label quality;
- similar regulatory constraints;
- comparable transaction/customer/document distribution;
- feasible human feedback loop.

### 4. Generate solution candidates

For each candidate, include:
- method family;
- core mechanism;
- supporting sources;
- required data;
- expected benefit;
- operational risks;
- evaluation strategy;
- simplest pilot version.

Prefer 3–5 candidates. Avoid long lists of shallow ideas.

Separate candidates into:
- **near-term pilot**: can be tested with current data and low integration burden;
- **strategic R&D bet**: promising but needs data, infra, governance, or research work;
- **not recommended yet**: attractive but unsupported, infeasible, or too risky.

### 5. Draft the method concept

For the strongest candidate, draft a concise method section:

```text
Method concept:
We propose [approach] for [problem]. The method uses [inputs] to produce [outputs/interventions]. It is motivated by [paper/case evidence], where similar mechanisms improved [metric/outcome]. In our setting, the key adaptation is [domain-specific change].
```

Then specify:
- model or algorithm components;
- training or fitting procedure;
- decision thresholding or human-in-the-loop workflow;
- explainability or audit layer;
- deployment boundary for the pilot.

### 6. Define evaluation before implementation

Every proposed solution needs a validation route:
- offline evaluation with historical data;
- backtesting or replay if decisions are temporal;
- baseline comparison against current process;
- human evaluation if outputs affect judgment or writing;
- ablations for claimed mechanisms;
- fairness, robustness, privacy, and compliance checks when relevant.

For each metric, state what decision it supports. Do not include decorative metrics.

### 7. Calibrate confidence

Use explicit confidence levels:

- **High**: multiple independent sources, similar setting, clear evaluation path, feasible data.
- **Medium**: good method precedent, but transfer depends on unverified assumptions.
- **Low**: plausible idea, but limited evidence or serious feasibility uncertainty.

Never present a literature-backed idea as proven in the user's setting. The literature justifies a pilot; the pilot validates transfer.

## Output format

Use this structure:

```markdown
# Publication-grounded solution design: [problem]

## Problem framing
- Stakeholders:
- Current pain:
- Decision/workflow:
- Constraints:
- Success criteria:
- Missing information:

## Prior successful cases and literature
| Source | Problem matched | Method | Evidence | Transferability | Caveats |
|---|---|---|---|---|---|

## Solution candidates
### Candidate 1: [name]
- Method family:
- Core idea:
- Supporting publications/cases:
- Required data:
- Expected benefit:
- Risks:
- Evaluation:
- Pilot version:
- Confidence:

## Recommended direction

## Draft method concept

## Evaluation plan

## Open questions before pilot

## Sources to read next
```

## Quality bar

A good answer should:
- cite concrete sources or clearly say sources still need to be searched;
- distinguish proven precedent from transfer assumptions;
- connect each method to the user's operational constraints;
- include baselines and evaluation criteria;
- avoid pretending a model is the solution when the bottleneck is data, workflow, incentives, or governance.
