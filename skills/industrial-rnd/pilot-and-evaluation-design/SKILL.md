---
name: pilot-and-evaluation-design
description: Design practical pilots and evaluation protocols for industry R&D, AI, ML, analytics, LLM, banking, fintech, or enterprise solutions. Use when the user has a proposed method or solution direction and needs to validate it with offline tests, backtests, human evaluation, A/B tests, baselines, metrics, ablations, guardrails, and a go/no-go decision. Especially use after publication-grounded-solution-design or industry-problem-framing.
---

# Pilot and Evaluation Design

Design the smallest credible pilot that can decide whether an industry R&D solution should move forward.

The goal is not to prove the solution is perfect. The goal is to reduce uncertainty enough to make a responsible build, stop, or iterate decision.

## When to use this skill

Use this skill when:
- a solution candidate exists and needs validation;
- the user needs a PoC, MVP, pilot, or experiment plan;
- the work must connect technical metrics to business value;
- offline evaluation, backtesting, human review, or A/B testing is needed;
- risks such as compliance, fairness, explainability, latency, or adoption must be measured.

For purely academic experiments, use `experiment-design`. For unclear business problems, use `industry-problem-framing` first.

## Workflow

### 1. State the pilot decision

Define the decision the pilot must support:

```text
After this pilot, we will decide whether to [scale / redesign / stop / collect more data] based on [criteria].
```

Avoid pilots that only produce a demo. A useful pilot changes a decision.

### 2. Define scope and deployment boundary

Specify:
- user group or process included;
- data window;
- product or workflow touchpoint;
- whether the pilot is offline, shadow-mode, assisted-human, or live;
- who reviews outputs;
- what actions are allowed;
- what is explicitly out of scope.

Prefer the least risky design that still tests the core mechanism.

Common pilot modes:

| Mode | Use when | Main limitation |
|---|---|---|
| Offline replay | Historical decisions and outcomes exist | Cannot measure behavior change |
| Backtest | Time-dependent decisions matter | Sensitive to leakage and policy changes |
| Shadow mode | Need production-like inputs without affecting users | No direct business impact |
| Human-assisted pilot | Need adoption and judgment signals | Human behavior adds variance |
| A/B test | Safe live intervention is possible | Requires traffic, governance, and monitoring |

### 3. Define baselines

Always compare against:
- current process;
- simple heuristic;
- simple statistical or ML baseline when relevant;
- published or standard method if feasible;
- human-only or human-with-tool condition when decision support is involved.

If a baseline cannot be implemented, explain why and how this weakens conclusions.

### 4. Choose metrics by decision role

Use four metric groups:

1. **Primary success metric**: the metric that decides go/no-go.
2. **Diagnostic metrics**: explain why the system works or fails.
3. **Business metrics**: connect to cost, revenue, risk, time, satisfaction, or compliance.
4. **Guardrail metrics**: ensure the pilot does not create unacceptable harm.

Examples:
- fraud/risk: precision@review-capacity, recall at fixed false-positive rate, loss captured, investigator workload;
- document AI: extraction F1, field-level accuracy, human correction time, hallucination rate;
- recommendation: uplift, conversion, churn, opt-out, fairness by segment;
- LLM support: answer groundedness, escalation rate, handling time, human acceptance, policy violation rate.

When the pilot pairs a metric with qualitative signals (interviews, adoption feedback, human review), design that combination *intentionally* rather than running two strands and stapling them together. `references/mixed-methods-integration.md` covers when mixing is worth it (methodological rationale, novel integrated insight), which design type fits (exploratory/explanatory sequential, convergent parallel, embedded), and the antipatterns to avoid (sample contamination, lost opportunity, integration failure) — grounded in Storey et al. (2025), arXiv:2404.06011.

### 5. Prevent invalid conclusions

Check for:
- target leakage;
- future information in features;
- biased labels from existing policy;
- selection bias in reviewed cases;
- seasonality and campaign effects;
- changed business rules;
- non-random pilot assignment;
- metric gaming;
- human review inconsistency;
- data drift.

If any risk is material, add a control or caveat.

### 6. Add ablations and stress tests

Use ablations only when they answer a decision-relevant question.

Examples:
- remove graph features to test whether network structure matters;
- compare retrieval-only vs generation-with-retrieval for LLM systems;
- compare model score vs model score plus explanation for human adoption;
- test performance by customer segment, branch, channel, or time period;
- stress test out-of-distribution months or rare cases.

### 7. Set go/no-go criteria

Define thresholds before seeing results.

```text
Go: improves primary metric by X while guardrails remain within Y.
Iterate: improves diagnostics but misses business threshold.
Stop: does not beat current process or violates guardrails.
Collect data: uncertainty dominated by label/data gaps.
```

Use confidence intervals or repeated time splits when sample size allows.

## Output format

```markdown
# Pilot and evaluation design: [solution]

## Pilot decision

## Pilot scope
- Mode:
- Users/process:
- Data window:
- Deployment boundary:
- Out of scope:

## Hypothesis
If we ..., then ..., because ..., compared with ...

## Baselines

## Metrics
| Metric | Type | Why it matters | Decision threshold |
|---|---|---|---|

## Evaluation protocol
- Data split/replay design:
- Human evaluation design:
- Statistical analysis:
- Leakage controls:
- Monitoring:

## Ablations and stress tests

## Risks and guardrails

## Go/no-go criteria

## Pilot deliverables
```

## Quality bar

A good pilot design should be small, safe, decision-relevant, and honest about what it cannot prove.
