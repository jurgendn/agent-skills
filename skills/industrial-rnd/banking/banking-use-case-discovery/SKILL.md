---
name: banking-use-case-discovery
description: Discover and prioritize banking, fintech, and financial-services AI/ML/R&D use cases from vague business goals, stakeholder pain points, data assets, or operational bottlenecks. Use whenever the user works on banking problems such as credit risk, fraud, AML, collections, customer intelligence, personalization, document AI, compliance, branch/contact-center operations, treasury, or productivity and needs a structured map of feasible, high-impact, research-grounded opportunities.
---

# Banking Use Case Discovery

Turn broad banking R&D goals into a prioritized use-case portfolio.

The goal is not to list every possible AI use case in banking. The goal is to identify opportunities where business value, data feasibility, risk controls, and literature precedent can align.

## When to use this skill

Use this skill when the user asks:
- what AI/ML/R&D problems to explore in a bank;
- how to turn banking pain points into use cases;
- which banking use cases are feasible with available data;
- how to prioritize ideas for R&D, PoC, or pilot;
- how to brainstorm within credit, fraud, AML, customer, operations, documents, compliance, or productivity.

For paper-backed solution details after a use case is selected, use `publication-grounded-solution-design` or `banking-ai-literature-mapper`.

## Banking opportunity map

Consider these domains:

| Domain | Example decisions/workflows | Common methods | Key risks |
|---|---|---|---|
| Credit risk | approval, limit, early warning, affordability | scoring, survival models, graph ML, explainable ML | fairness, explainability, regulation, leakage |
| Fraud and scams | transaction monitoring, mule detection, scam prevention | anomaly detection, graph learning, sequence models, rules + ML | adversarial behavior, false positives, latency |
| AML | suspicious activity detection, case prioritization | graph analytics, weak supervision, entity resolution, typology mining | label bias, auditability, regulatory defensibility |
| Collections | contact prioritization, hardship detection, treatment strategy | uplift modeling, reinforcement learning, segmentation | customer harm, policy constraints |
| Customer intelligence | churn, next-best-action, personalization | recommender systems, uplift modeling, representation learning | consent, fairness, over-targeting |
| Contact center | routing, summarization, QA, agent assist | retrieval, LLMs, speech/text analytics | hallucination, privacy, human adoption |
| Document AI | KYC, loan docs, contracts, forms | OCR, layout models, information extraction, RAG | extraction errors, audit trail, document drift |
| Compliance and risk ops | policy checking, control testing, reporting | NLP, retrieval, workflow mining, anomaly detection | legal interpretation, accountability |
| Productivity | analyst copilots, knowledge search, code/data assistants | RAG, agents, tool use, summarization | data leakage, answer grounding, evaluation |

## Workflow

### 1. Start from pain, not technology

For each candidate area, capture:
- current process;
- user pain;
- cost of failure;
- decision frequency;
- manual effort;
- available data;
- known constraints;
- owner and adoption path.

Avoid starting with "use LLM" or "use graph neural networks" unless the problem shape justifies it.

### 2. Convert areas into use-case cards

Use this template:

```markdown
### Use case: [name]
- Business problem:
- Decision/workflow:
- Target users:
- Data needed:
- Candidate method families:
- Prior precedent to search:
- Business value hypothesis:
- Risk/compliance concerns:
- Pilot shape:
```

### 3. Score each use case

Score 1–5 for:
- business impact;
- data readiness;
- technical feasibility;
- literature/industry precedent;
- evaluation clarity;
- operational adoption;
- risk/manageability.

Then classify:
- **Quick pilot**: high feasibility, clear data, manageable risk;
- **R&D candidate**: promising but requires method/data exploration;
- **Strategic bet**: high impact but hard integration or governance;
- **Defer**: unclear value, weak data, or unacceptable risk.

### 4. Identify research grounding needs

For each promising use case, list search directions:
- canonical banking/finance terms;
- adjacent domains with similar problem shape;
- evaluation benchmarks;
- regulatory or explainability literature;
- known failure modes.

Examples:
- mule account detection → graph anomaly detection, fraud rings, financial transaction networks;
- complaint summarization → grounded summarization, customer support QA, RAG evaluation;
- credit early warning → survival analysis, temporal tabular modeling, macroeconomic stress features.

### 5. Prioritize a portfolio

Recommend a balanced set:
- one quick pilot;
- one medium-term R&D project;
- one strategic learning bet;
- one data-foundation project if many use cases are blocked by the same missing data.

## Output format

```markdown
# Banking use-case discovery

## Context and constraints

## Use-case portfolio
| Use case | Domain | Impact | Data readiness | Feasibility | Precedent | Evaluation clarity | Risk | Priority |
|---|---|---:|---:|---:|---:|---:|---:|---|

## Top use-case cards
### 1. [Use case]
- Business problem:
- Decision/workflow:
- Target users:
- Data needed:
- Candidate methods:
- Prior precedent to search:
- Pilot shape:
- Main risks:

## Recommended portfolio
- Quick pilot:
- R&D candidate:
- Strategic bet:
- Data foundation need:

## Next literature searches
```

## Quality bar

A good use-case map should help the user choose what to investigate next, not merely show that many banking tasks could use AI.
