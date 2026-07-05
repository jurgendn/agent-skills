---
name: venue-targeting
description: Select and prioritize publication venues (conferences, workshops, journals) for a research paper. Use whenever the user asks where to submit, which conference fits best, whether a paper is ready for a top venue, how to resubmit after rejection, or when comparing venues like NeurIPS vs. ICLR vs. ICML vs. ACL vs. EMNLP vs. CVPR vs. AAAI vs. ICDM vs. journals. Also use when the user has a contribution in hand and needs to decide between tier levels, theory vs. empirical tracks, workshop vs. main track, or short vs. long paper format. If the paper isn't ready for any venue yet, use submission-readiness-audit first.
---

# Venue Targeting

Choosing the wrong venue is one of the most expensive mistakes in academic publishing — a misfit paper gets desk-rejected or triaged by reviewers who don't understand the contribution.

The goal is not to aim for the most prestigious venue. The goal is to find the venue where your contribution is most legible to the reviewers who will read it.

---

## Workflow

### 1. Characterize the contribution

Before matching to venues, classify the paper across these dimensions:

**Contribution type**
- New method (architecture, algorithm, loss, training procedure)
- New analysis or theory (bounds, complexity, expressiveness, generalization)
- New dataset or benchmark
- Empirical study or survey (what works, what doesn't, at what scale)
- Application or system (deployed system, real-world impact)
- Negative result or replication study

**Domain**
- ML theory / optimization
- Deep learning (supervised, self-supervised, generative)
- NLP / language models
- Computer vision
- Reinforcement learning
- Graph learning
- Multimodal / audio / speech
- Robotics / embodied AI
- Data mining / knowledge discovery
- AI systems / efficiency / inference

**Evaluation style**
- Synthetic + real benchmarks with ablations
- Single large-scale benchmark (leaderboard)
- Theoretical proof + small empirical illustration
- Large-scale human evaluation
- Deployment metrics (latency, cost, real users)

**Paper length and scope**
- Full paper (8–12 pages)
- Short / findings paper (4 pages)
- Workshop paper (4–6 pages)
- Journal (no page limit)

---

### 2. Match to venue families

Use this as a rough guide. Venue norms shift — always check the current CFP and recent accepted papers before submitting.

#### Top-tier ML conferences (theory + methods + empirical)

| Venue | Strongest fit | Notes |
|---|---|---|
| NeurIPS | Novel methods, theory, analysis, large-scale empirical | Very broad; high volume; strong theoretical bar |
| ICLR | Deep learning methods, representation learning, LLMs | Community-driven reviews; OpenReview transparency |
| ICML | Methods with strong theoretical grounding or empirical rigor | Strong optimization and theory community |
| AISTATS | Probabilistic models, statistical ML, Bayesian methods | Smaller; faster reviews; theory-friendly |
| COLT | Pure ML theory, PAC learning, online learning | Theory only; no empirical-only papers |
| UAI | Probabilistic graphical models, causal inference, uncertainty | Smaller; strong probabilistic reasoning community |

#### NLP / language

| Venue | Strongest fit |
|---|---|
| ACL / EMNLP / NAACL | Core NLP tasks, language model analysis, datasets, applications |
| EACL | Same scope; European community; sometimes less competitive |
| CoNLL | Structured prediction, linguistic NLP |
| Findings of ACL/EMNLP | Good work that didn't make the main track; broad acceptance |

#### Computer vision

| Venue | Strongest fit |
|---|---|
| CVPR | Vision methods, large-scale empirical, applications |
| ICCV / ECCV | Similar scope; biennial; sometimes more theory-friendly |
| WACV | Lower tier; good for solid applied work |

#### AI / data mining / applied

| Venue | Strongest fit |
|---|---|
| AAAI | Broad AI, applied work, planning, knowledge representation |
| IJCAI | Similar to AAAI; more international scope |
| KDD | Data mining, large-scale systems, industry applications |
| WWW | Web-scale systems, graph learning, recommendation |
| WSDM | Information retrieval, recommendation, search |
| ICDM | Data mining, pattern recognition |

#### Journals (when to use)

- **JMLR**: Long-form theoretical or empirical ML work; no page limit; slower but respected.
- **TMLR**: Fast-turnaround ML journal; accepts solid contributions rejected from conferences; no venue prestige bias.
- **TACL**: NLP journal; fast-turnaround; proceedings published at ACL/EMNLP.
- **AIJ**: AI research; broad scope; slower.

Use journals when: the paper is too long for a conference, it's a negative result or replication study, it needs more pages to do the contribution justice, or it was rejected multiple times and the community hasn't found a home for it.

---

### 3. Assess fit and tier realism

For the top 2–3 candidate venues, assess:

**Contribution fit**
- Do the top papers at this venue look like this contribution?
- Would reviewers in this community understand and value the core claim?
- Is the evaluation protocol what this community expects?

**Tier realism**
- What is the acceptance rate? (NeurIPS ~25%, ICLR ~30%, ICML ~27%, ACL ~25%, CVPR ~25%)
- What is the weakest accepted paper at this venue in recent years?
- What is the strongest objection a reviewer at this venue will have, and can the paper answer it?

**Deadline fit**
- What is the next submission deadline?
- How much revision is needed before the paper is ready?
- Is there a workshop option for an earlier feedback cycle?

---

### 4. Workshop vs. main track

Workshops are appropriate when:
- The paper has a core idea but insufficient experiments for a main paper.
- The contribution is interdisciplinary and may get confused at a single-domain venue.
- The paper targets a niche community that has a dedicated workshop.
- You want feedback before polishing for a main submission.

Workshops are not appropriate when:
- The paper is already main-track quality — workshop acceptance adds nothing.
- The paper will be rejected from the workshop too if the idea isn't solid.

Workshop proceedings are generally non-archival; you can still submit to a main venue after.

---

### 5. Resubmission strategy after rejection

After a rejection, before resubmitting:

1. **Read the reviews.** Identify the strongest objection — not the harshest, the most substantive.
2. **Decide: fix or reframe.** Some papers need more experiments; others need a different framing for a different community.
3. **Consider venue change.** If three reviewers at NeurIPS thought the paper "lacks theoretical depth," consider ICML with a stronger theory framing, or JMLR for a long-form treatment.
4. **Reframe deliberately when the community changes** — don't just fix the technical objections. Writing norms (framing, jargon, quantitative-evidence density, canonical citations, structure) vary by community, and a paper that reads as an outsider's gets discounted for "fit" reasons no reviewer states outright. When redirecting to a different community, work through `references/cross-community-writing-norms.md`: rewrite the **introduction first** (it carries the framing and is what interdisciplinary authors nearly always rewrite), then retune jargon, evidence density, and canonical citations to the target. Don't trust a one-shot LLM "reframe for venue X" pass — LLMs homogenize writing across communities rather than adapting to the target; steer with the checklist and do a human fit pass.
5. **Never bare-resubmit.** A paper that goes in unchanged will fail for the same reasons.

Common resubmission paths:
- Rejected from NeurIPS → revise → ICLR (same cycle if timing allows)
- Rejected from ICML → add experiments → NeurIPS
- Rejected from ACL → revise framing → EMNLP
- Rejected from main track → shorten → Findings
- Rejected from Findings → journal (TMLR or TACL for NLP)

---

## Output format

```markdown
# Venue Targeting: [Paper title / one-line description]

## Contribution profile
- Type: [method / theory / dataset / empirical study / system / negative result]
- Domain: [field]
- Evaluation: [benchmark types]
- Length: [full paper / short / journal-length]

## Recommended venues (ranked)

### 1. [Venue]
- Fit: [why this community will understand and value the contribution]
- Risks: [what reviewers will push back on]
- Next deadline: [approximate]
- Tier realism: [honest assessment]

### 2. [Venue]
...

### 3. [Venue]
...

## Workshop options (if applicable)
- [Workshop] at [Venue]: [why]

## If rejected from #1
[Concrete resubmission path and what to fix]

## Open questions
[What the user needs to clarify before a final venue decision]
```

---

## Quality bar

A good venue recommendation should prevent a mismatch that wastes 3–6 months of revision cycles. It should be honest about tier realism, specific about reviewer expectations, and give a concrete plan for what happens if the first choice rejects.
