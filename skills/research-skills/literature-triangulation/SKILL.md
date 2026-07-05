---
name: literature-triangulation
description: Build a source-grounded map of a research topic by comparing papers, benchmarks, code, and genuine disagreements. Use whenever the user wants to understand a research area, not just find papers — including phrasings like "what's the current state of X", "what should I read on Y", "is X still SOTA", "are there good baselines for Z", "what does the field believe about W", "survey this area for me", "what are the key papers on X", "compare these two approaches", or "is this claim actually well-supported". Also use when the user is about to build on a method and should first verify the evidence base is solid. If the user already has a source map and wants polished Related Work prose, use related-work-writer instead. The skill's main job is preventing hallucinated consensus — confidently synthesized positions that aren't grounded in the actual sources.
---

# Literature Triangulation

Produce a skeptical, source-grounded map of the topic. The output should read like something a careful researcher would say after spending a day with the papers — not like a Wikipedia summary.

## The core problem this skill solves

Two failure modes dominate literature synthesis, and both are worse than saying "I'm not sure":

1. **Hallucinated consensus.** Claude fills gaps in coverage with plausible-sounding training-data priors, producing a confident synthesis that nobody with actual paper access would endorse. This is the most dangerous failure because it sounds authoritative.
2. **Surface-level coverage.** Reading abstracts and titles without following citation trails, missing the paper that actually introduced the method everyone else is citing, treating a blog post's characterization as authoritative, or stopping at the first three search results.

The antidote to both is triangulation: a claim earns confidence only when independent sources (ideally with different authors, institutions, and incentives) agree on it, and it holds on benchmarks the original authors didn't control.

## Workflow

### 1. Clarify scope before searching

A topic like "graph neural networks" has too much literature to map usefully. Before searching, get precise about:
- What specific claim, method, or subproblem is in focus?
- What time horizon matters? (all time / last 3 years / last 12 months)
- What does the user need this for? (writing related work / choosing a baseline / understanding a paper / building on a method)

The use case shapes everything: writing related work needs breadth; choosing a baseline needs depth on head-to-head comparisons; building on a method needs to verify the method's actual assumptions and failure modes.

### 2. Search for primary sources, not commentary

Primary sources, in rough order of priority:
- Original research papers (arXiv, venue proceedings)
- Official code repositories and README files
- Benchmark leaderboards and dataset papers
- Technical reports and extended abstracts
- Survey and review papers (useful as *maps*, not *evidence*)

Deprioritize: blog posts, Twitter threads, YouTube talks, review aggregators. These are useful for orientation but never substitute for the original claim. If a blog says "Paper X showed Y", go to Paper X.

**Search strategy.** Run multiple queries, not one — different terms surface different parts of the literature. For a method: search the method name, the problem it solves, the benchmark it's evaluated on, and the names of the most-cited authors. For a claim: search the claim directly plus potential counter-evidence ("X fails when", "limitations of X", "X replication"). Note which queries returned nothing useful — that absence is information.

When the user is **entering a new area** rather than checking a narrow claim, use `references/research-immersion-strategy.md`. It covers exploratory vs. systematic review, disciplinary-bubble escape, survey/recommender/LLM pitfalls, and breadth-depth control for fast fields.

**Following citation trails.** The most important paper in a chain is often not the most recent one. If five papers all cite Paper A as the source of a key result, go to Paper A and verify the result directly. Citation telephone — where Paper E's characterization of Paper A is subtly different from what Paper A actually says — is extremely common.

### 3. Read purposefully, not completely

For each key paper, prioritize sections in this order based on your goal:

- **For a method**: Abstract → Introduction (to understand the claim) → Section 3/4 (the actual method) → Experiments (which baselines, which datasets, which metrics) → Limitations/Conclusion
- **For a result**: Abstract → the specific table/figure → the experimental setup → the footnotes and appendices (where the caveats live)
- **For foundational understanding**: Introduction → Related work → Proofs/derivations (for theory papers) → Conclusion

Don't rely on abstracts alone for any claim you'll stake your own work on. Abstracts are marketing; the method section and experiment tables are evidence.

### 4. Triangulate — treat disagreements as signal

Triangulation means actively looking for where independent sources *diverge*, not just where they agree. For each major claim:

- Does it hold on benchmarks the original authors didn't construct? Check papers from competing groups.
- Has it been replicated? Are there negative results or failed replications in the literature?
- What do critics cite when they argue against this approach? Follow those citations.
- If two papers claim to outperform each other, what explains the discrepancy? (Different train/test splits? Different hyperparameter budgets? Different task formulations? One paper not properly tuning the baseline?)

Genuine consensus means independent researchers with no shared interest in the answer reach the same conclusion. A method being widely *adopted* is not the same as it being widely *validated*.

### 5. Separate what you read from what you infer

Every factual claim in the output should be traceable to a specific source. Maintain this distinction explicitly:

- **Observed in source**: "Paper X reports 84.2 F1 on benchmark Y (Table 3)."
- **Inferred from sources**: "This suggests the gain is largely dataset-specific, since the method underperforms on Z."
- **Open / unresolved**: "No paper we found directly compares X and Y under matched conditions."

Never collapse the third category into a synthetic "the field believes" statement when the field actually disagrees or hasn't answered the question.

### 6. Distinguish consensus from hype

Fast-moving fields (LLMs, RL, diffusion models) generate a lot of claimed results that don't survive contact with independent replication. Signals that a result is more likely solid:

- Replicated by groups with no co-authorship and no shared industry affiliation
- Holds on benchmarks the original authors didn't create
- Performance gap is large enough to survive realistic hyperparameter variation
- Method is simple enough that the explanation is the mechanism (not "it works because transformers")
- Has been around for 12+ months without a successful challenge appearing

Signals that a result might be hype:
- Only tested on benchmarks introduced in the same paper
- Baseline is not tuned competitively (very common; check if baselines match reported numbers from the baseline's own paper)
- Result is on a leaderboard but not in a peer-reviewed comparison
- All positive citations are from the original authors' lab
- Claim involves emergent/scaling phenomena with no mechanistic account

For mathematical and theoretical results, the hype/consensus distinction works differently: a proved theorem is proved (check the proof, not the venue). What to watch for instead is whether the *conditions* of the theorem are met in the applications people are using it for.

### 7. Flag staleness risk explicitly

Research moves at very different speeds by subfield. Roughly:
- **Fast** (results can be superseded in weeks–months): LLM pretraining, RLHF/alignment techniques, multimodal models, diffusion, retrieval-augmented generation
- **Medium** (months to 1–2 years): GNNs, efficiency methods (quantization, distillation), specific benchmark competitions
- **Slow** (years to decades): most mathematical theory, foundational algorithmic results, established empirical benchmarks like ImageNet

When covering a fast-moving area, say so explicitly in the output and note the search date. If a key result is older than 12 months in a fast-moving subfield, note that it may have been superseded and name what to search for to check.

## Output shape

Adapt to what the user needs, but these sections cover most cases:

- **Scope and framing** — what specific question this map answers, and what it deliberately excludes
- **Landscape** — the major approaches, their relationships, and which papers introduced them (with citations)
- **Strongest evidence** — the most robustly supported claims, with provenance and replication status
- **Genuine disagreements** — where the field actually conflicts, stated as a disagreement (not a false synthesis)
- **Known weaknesses and blind spots** — failure modes, underexplored settings, missing ablations, benchmarks that are known to be gamed
- **Open questions** — things the literature hasn't resolved, framed specifically enough to be researchable
- **Recommended next reads** — 3–7 papers with a one-sentence rationale for each; prioritize papers that are load-bearing (many subsequent works depend on them) or that contain the most reliable empirical evidence
- **Sources** — for every claim that isn't obvious, include: paper title, authors, year, venue (or arXiv ID), and URL. For code, link the repo directly.

For a **related-work section**: compress the Landscape + Strongest evidence into 2–4 paragraphs organized by thematic cluster, positioning the user's own work relative to each. Don't list every paper; cite the most representative.

For **choosing a baseline**: go deep on the Strongest evidence and Known weaknesses sections. The point is to understand what the best honest comparison looks like, including why some "standard" baselines are weak.

For **mathematical literature**: the Landscape section should map the theorem/conjecture space, not just paper titles. Note which results are conditional (assuming X, then Y), which are tight (matching upper and lower bounds), and where the boundary of current knowledge actually lies.

## What to do when sources conflict

Two papers reporting different numbers on "the same" benchmark is the default, not an exception. Before synthesizing:

1. Check if they're actually using the same splits, preprocessing, and evaluation protocol.
2. Check if the baseline in one paper is properly tuned — compare against the numbers the baseline's own paper reports.
3. Check if one paper's result supersedes the other's (same authors + more data, better implementation).
4. If none of the above resolves it, report the conflict explicitly: "Paper A reports X; Paper B, under what it describes as matched conditions, reports Y. The discrepancy is not explained in either paper."

False synthesis ("results are mixed") is worse than reporting the conflict, because it hides the specific question the user might need to resolve.

## Epistemic honesty in the output

The output should accurately represent your confidence:
- Claims backed by multiple independent sources: state directly
- Claims from a single paper not yet replicated: flag as such
- Claims you inferred rather than read: say "this suggests" or "one interpretation is"
- Areas where you couldn't find primary sources: say so explicitly — "we didn't find a direct comparison of X and Y in the literature" is useful information
- Areas where your search coverage is likely incomplete (e.g., non-English literature, workshop papers, technical reports): note the limitation

Never use "the field believes" or "it is generally accepted that" without being able to point to at least 3 independent sources that support the claim.
