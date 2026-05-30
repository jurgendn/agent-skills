---
name: banking-ai-literature-mapper
description: Map publications, prior successful cases, datasets, benchmarks, and method families for banking and fintech AI problems. Use when the user needs publication-grounded evidence for credit risk, fraud, AML, collections, customer intelligence, personalization, banking document AI, compliance, contact-center automation, or financial-services R&D proposals. This skill specializes literature-triangulation for banking domain transfer and should feed publication-grounded-solution-design.
---

# Banking AI Literature Mapper

Build a source-grounded map of banking and fintech AI methods, successful cases, datasets, benchmarks, and evaluation practices.

The goal is to help an industry R&D team justify solution directions with credible precedent while staying honest about transfer risk, regulatory constraints, and data differences.

## When to use this skill

Use this skill when the user asks for:
- prior successful AI/ML cases in banking or fintech;
- papers supporting a banking solution proposal;
- method options for credit, fraud, AML, customer, document, compliance, or operations problems;
- evaluation benchmarks or datasets for banking-like tasks;
- a literature-backed internal R&D proposal.

If the user asks for a broad non-banking research survey, use `literature-triangulation`. If the user needs a final solution design, use `publication-grounded-solution-design` after mapping sources.

## Workflow

### 1. Define the banking problem shape

Classify the problem by both domain and technical shape.

Domain examples:
- credit risk;
- fraud/scam detection;
- AML and suspicious activity monitoring;
- collections and recovery;
- customer churn and personalization;
- contact-center and branch operations;
- document understanding and KYC;
- compliance, risk controls, and audit;
- employee productivity and knowledge retrieval.

Technical shapes:
- tabular prediction;
- temporal forecasting;
- ranking or triage;
- graph detection;
- anomaly detection;
- causal uplift;
- recommender systems;
- information extraction;
- retrieval and grounded generation;
- workflow/process mining;
- optimization.

Search using both labels. Banking labels alone may miss transferable methods from insurance, telecom, e-commerce risk, healthcare operations, cybersecurity, or public-sector fraud.

### 2. Separate source types

Build separate buckets:

1. **Banking/finance papers**: closest domain match.
2. **Adjacent-domain papers**: similar problem shape with stronger methods or benchmarks.
3. **System/case papers**: production or near-production deployments.
4. **Datasets/benchmarks**: public tasks useful for baselines or proxies.
5. **Surveys**: maps of the area, not direct evidence.
6. **Regulatory/explainability sources**: constraints that affect adoption.

Do not mix these as equal evidence.

### 3. Evaluate evidence quality

For each source, assess:
- publication venue or credibility;
- dataset realism;
- sample size and time span;
- evaluation protocol;
- baselines;
- leakage controls;
- explainability and fairness treatment;
- operational relevance;
- whether the result is reproducible or only claimed.

Flag weak evidence explicitly.

### 4. Map methods to banking transfer assumptions

For every method family, state what must be true in the bank:
- data fields exist and are reliable;
- labels are not too biased by old policies;
- decisions and outcomes are timestamped;
- entities can be linked consistently;
- model outputs can be explained to users or auditors;
- latency and integration constraints are feasible;
- compliance approves the intervention.

### 5. Extract evaluation patterns

Identify how the literature evaluates similar work:
- temporal train/test split;
- out-of-time validation;
- precision@k under review capacity;
- cost-sensitive metrics;
- calibration;
- fairness by segment;
- human-in-the-loop evaluation;
- backtesting;
- ablations;
- robustness to drift or adversarial change.

Recommend the evaluation style that best matches the user's problem.

### 6. Produce a reading and action map

Prioritize sources into:
- must-read;
- useful for methods;
- useful for evaluation;
- useful for risk/compliance;
- weak or only background.

Then recommend how to use the literature:
- justify a pilot;
- select baselines;
- avoid known failure modes;
- define data requirements;
- draft the method section.

## Output format

```markdown
# Banking AI literature map: [problem]

## Problem classification
- Banking domain:
- Technical shape:
- Decision/workflow:
- Key constraints:

## Source map
| Source | Type | Problem match | Method | Evidence quality | Evaluation pattern | Transfer assumptions | Caveats |
|---|---|---|---|---|---|---|---|

## Method families
### [Method family]
- Core idea:
- Best supporting sources:
- When it fits:
- When it fails:
- Banking transfer assumptions:
- Evaluation implications:

## Prior successful cases

## Datasets and benchmarks

## Evaluation patterns to reuse

## Gaps and risks in the literature

## Recommended reading order

## How this should feed solution design
```

## Quality bar

A good banking literature map should make it clear which sources are strong enough to support an R&D proposal, which only provide inspiration, and which assumptions must be tested before deployment.
