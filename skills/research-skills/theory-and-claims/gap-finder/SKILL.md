---
name: gap-finder
description: Read a research paper and surface publishable theoretical gaps — unstated assumptions, loose bounds, missing guarantees, unjustified heuristics, and settings the theory doesn't cover. Trigger whenever the user shares a paper and wants to find weaknesses, gaps, or open problems. Trigger phrases include "find gaps in this paper", "what's weak about this", "where could I improve on this", "what assumptions are they hiding", "poke holes in this", "what's not proven here", "where's the theoretical gap", "analyze this for weaknesses", or any request to critically read a paper to identify research opportunities. Also trigger on "I want to extend X" or "is there room to improve this" about a method or paper. Do NOT use for literature surveys (literature-triangulation), stress-testing own conjectures (counterexample-hunter), or finding papers (applied-paper-search).
---

# Gap Finder

Read a paper. Find where the theory is thin.

The goal is not to "critique" the paper in a reviewer sense. The goal is to find **publishable theoretical gaps** — places where a mathematician could contribute something new. A gap is valuable when: (1) the method works empirically but lacks theoretical justification, (2) the theory exists but under assumptions that don't match practice, or (3) a natural generalization is left open.

## The two failure modes

1. **Fake gaps.** Pointing out something the paper already addresses (in the appendix, in a cited companion paper, or implicitly via a well-known result). Always check before reporting.
2. **Trivial gaps.** "They don't prove convergence in infinite dimensions" when the method is for finite graphs. A gap must be *relevant* — someone would care about closing it.

---

## Step 1: Extract the paper's theoretical skeleton

Read the paper and produce a structured summary of exactly these items:

**Claims.** Every theorem, proposition, lemma, and corollary — stated precisely, with all quantifiers and domains. Also include any informal claims the authors make in prose ("our method converges", "this is optimal", "the complexity is O(n log n)") that aren't backed by a formal statement.

**Assumptions.** For each claim, list:
- Explicit assumptions (stated in the theorem)
- Implicit assumptions (used in the proof but not stated, or inherited from a cited result)
- Modeling assumptions (what the problem formulation assumes about the data/graph/distribution)

**Guarantees.** What exactly does each result promise? Distinguish:
- Existence vs. uniqueness vs. both
- Exact vs. approximate (and if approximate: what metric, what bound)
- Worst-case vs. average-case vs. high-probability
- Finite-sample vs. asymptotic

**What the method actually does vs. what the theory covers.** Many papers have a gap between the algorithm (which does X, Y, Z) and the theory (which only analyzes X under idealized conditions). Map this gap explicitly.

---

## Step 2: Probe each assumption

For each assumption in the skeleton, ask:

1. **Is it necessary?** Would the result fail without it, or is it a convenience assumption the proof uses but the result doesn't need? (If you suspect it's unnecessary, that's a gap: proving the result under weaker assumptions.)

2. **Is it realistic?** Does the assumption hold in the settings where people actually use the method? Common offenders:
   - i.i.d. data when the application is temporal/spatial
   - Connected graphs when real networks have isolates
   - Bounded degree when real graphs are heavy-tailed
   - Smoothness/Lipschitz when the function is learned by a neural net
   - Known number of communities when it's unknown in practice
   - Stationarity when the process is evolving

3. **Is it tight?** Could the result be strengthened by replacing the assumption with something weaker? Is there a known hierarchy of assumptions in this area, and where does this paper sit in it?

---

## Step 3: Probe each guarantee

For each guarantee, ask:

1. **Is the bound tight?** Is there a matching lower bound? If not, is the gap between upper and lower bounds large? A loose bound is a gap.

2. **Is the rate optimal?** For convergence results: is this the best achievable rate, or could it be improved? For complexity results: is there a lower bound that matches?

3. **Does the guarantee match the loss function / metric people actually care about?** Theory often proves something in L2 when practitioners care about L∞, or proves expected risk when high-probability bounds are needed.

4. **Is the asymptotic regime realistic?** A result that kicks in at n > 10^8 when datasets have n = 10^4 is technically correct but practically useless. Check if the paper's experiments are in the regime where the theory applies.

---

## Step 4: Identify the structural gaps

These are the most publishable kind — not a weakness in a specific theorem, but a missing piece in the paper's overall theoretical architecture:

**Theory-practice gap.** The method includes a component (a heuristic, a hyperparameter choice, an initialization scheme) that has no theoretical justification. The experiments show it matters, but there's no theorem explaining why or when.

**Missing generalization.** The result is proved for a special case (e.g., undirected graphs, homogeneous networks, static settings) but the method is applied more broadly. The generalization to the broader setting is open.

**Missing connection.** The paper's technique resembles or could be connected to a known framework (optimal transport, spectral theory, information geometry, etc.) but the connection isn't made. Formalizing it could yield a cleaner proof or stronger results.

**Computational-statistical tradeoff.** The paper proves a statistical guarantee and separately proves a computational guarantee, but doesn't analyze whether achieving the statistical optimum is computationally feasible, or vice versa.

**Robustness.** The method is analyzed under clean conditions but not under noise, adversarial perturbation, or model misspecification. How do the guarantees degrade?

---

## Step 5: Rank and report

Not all gaps are worth pursuing. Rank each gap by:

- **Publishability.** Would closing this gap be a paper? A section of a paper? A footnote?
- **Tractability.** Is there a plausible proof strategy, or is this a known hard open problem?
- **Relevance to the user's research.** (If context is available — e.g., the user works on random walks, GNNs, spectral methods — flag gaps that connect to their tools.)

Output format:

### Paper skeleton
The structured summary from Step 1, kept concise.

### Gaps found
For each gap, state:
- **What's missing:** one sentence
- **Why it matters:** one sentence
- **How hard it looks:** easy extension / moderate / hard open problem / unclear
- **Proof strategy hint:** if one exists — what tool or technique might work
- **Connects to:** related work or frameworks the user could leverage

Order gaps by estimated publishability × tractability, best first.

### What's solid
Briefly note what the paper *does* prove well — both for fairness and so the user knows which parts to build on rather than attack.

---

## Principles

- A gap you construct a counterexample for is worth ten gaps you merely suspect. If you can build a small example (a graph, a distribution, a function) where the paper's theory doesn't apply but its method is used, say so.
- Distinguish "the authors didn't prove X" from "X is false." The former is a gap; the latter is a flaw. Both are useful, but they lead to different research programs.
- Check the appendix and supplementary material before reporting a gap. Many papers address limitations there.
- If the paper cites a companion paper or technical report for proofs, note that the gap might be closed there — but flag it as "unverified" unless you can check.
- Be concrete. "The assumptions are strong" is not a gap. "Assumption 3 requires bounded spectral gap, but Barabási-Albert graphs have unbounded spectral gap, so the theory doesn't cover the most common synthetic benchmark" is a gap.
