---
name: industry-problem-framing
description: Convert vague industry, banking, fintech, enterprise, or operational problems into precise R&D problem statements, stakeholder maps, hypotheses, constraints, and solution search directions. Use whenever the user says a problem is vague, ambiguous, unclear, broad, political, business-driven, or not yet researchable. This skill should usually run before publication-grounded-solution-design when the problem is not specific enough to search literature or draft methods.
---

# Industry Problem Framing

Turn an ambiguous business problem into a researchable and pilotable R&D problem.

The goal is to prevent premature solutioning. A vague request like "use AI to improve operations" must become a concrete decision, workflow, metric, and evidence need before methods are proposed.

## When to use this skill

Use this skill when:
- the user has an unclear business or industry problem;
- stakeholders disagree on what the problem means;
- the user needs to brainstorm but avoid shallow idea lists;
- the next step is literature search, solution design, or pilot planning;
- the user needs an internal R&D framing memo.

If the user already has a precise problem and wants paper-backed methods, use `publication-grounded-solution-design` instead.

## Workflow

### 1. Capture the raw problem statement

Write the user's problem exactly, then extract:
- domain and business unit;
- current workflow;
- users and decision-makers;
- pain points;
- constraints;
- known data sources;
- proposed solution, if any;
- why the problem matters now.

Do not improve the wording yet. First preserve the ambiguity.

### 2. Identify the actual decision or workflow

Most industry R&D problems are about changing a decision or workflow.

Ask:
- Who makes the decision today?
- What information do they use?
- What action follows the decision?
- What failure is costly?
- What would happen if the model/system is wrong?
- Is the goal automation, prioritization, explanation, recommendation, monitoring, or insight generation?

Classify the problem as one or more:
- prediction;
- ranking or prioritization;
- anomaly detection;
- segmentation;
- recommendation or next-best-action;
- information extraction;
- decision support;
- process mining;
- causal measurement;
- forecasting;
- optimization;
- knowledge management;
- human productivity support.

### 3. Map stakeholders and incentives

For each stakeholder, capture:

| Stakeholder | Pain | Desired outcome | Constraint | Possible conflict |
|---|---|---|---|---|

Include operational, risk, compliance, legal, data, product, engineering, and frontline users when relevant.

### 4. Turn pain points into hypotheses

Create falsifiable hypotheses:

```text
If we [intervention], then [target metric] improves for [population/process] because [mechanism], compared with [baseline].
```

Examples:
- If we prioritize high-risk cases for manual review, then investigators process more true positives per hour because low-value cases are filtered earlier.
- If we retrieve similar resolved cases during complaint handling, then average handling time decreases because agents reuse verified resolution patterns.

### 5. Separate business metrics from technical metrics

Business metrics answer whether the work matters. Technical metrics answer whether the system works.

Examples:
- Business: cost per reviewed case, time-to-resolution, approval rate at fixed risk, fraud loss, customer churn, NPS, SLA compliance.
- Technical: precision@k, recall at fixed workload, calibration, AUC, latency, extraction F1, hallucination rate, human acceptance rate.

Tie every technical metric to a business decision. Remove metrics that do not affect action.

### 6. Identify data and evidence requirements

List:
- available tables/documents/logs;
- labels or proxies;
- observation window;
- leakage risks;
- privacy or compliance constraints;
- unit of analysis;
- population coverage;
- data refresh frequency;
- integration path.

Flag whether the problem is blocked by:
- missing labels;
- weak ground truth;
- no action logs;
- unclear ownership;
- unmeasurable success;
- compliance constraints;
- insufficient sample size;
- non-stationary behavior.

### 7. Produce search directions

Convert the framed problem into literature search handles:
- domain terms;
- method terms;
- benchmark terms;
- adjacent domains with similar problem shape;
- negative-result or limitation queries.

This prepares handoff to `publication-grounded-solution-design` or `literature-triangulation`.

## Output format

```markdown
# Industry problem framing: [short title]

## Raw problem

## Clarified problem statement
For [stakeholder/process], improve [decision/workflow/outcome] by using [available signals/interventions], subject to [constraints], measured by [business and technical metrics].

## Stakeholder map
| Stakeholder | Pain | Desired outcome | Constraint | Possible conflict |
|---|---|---|---|---|

## Decision/workflow analysis
- Current workflow:
- Decision point:
- Failure modes:
- Cost of errors:
- Human-in-the-loop needs:

## Candidate hypotheses
1. If ..., then ..., because ..., compared with ...

## Metrics
- Business metrics:
- Technical metrics:
- Guardrail metrics:

## Data and feasibility
- Available data:
- Labels/proxies:
- Leakage risks:
- Compliance/privacy constraints:
- Blockers:

## Literature and precedent search directions
- Domain queries:
- Method queries:
- Adjacent-domain analogues:
- Limitation queries:

## Recommended next step
```

## Quality bar

A good framing should make it obvious what to search, what to measure, and what must be clarified before proposing methods.
