---
name: paper-idea-and-scope-brainstormer
description: Brainstorm a research idea and decide what a new paper should cover — generate candidate framings, pick the central contribution, and draw the in-scope vs. deferred boundary. Use whenever the user has a rough interest, preliminary results, or a problem and asks "what should this paper be about", "help me brainstorm an idea", "what should I include / cover", "is this one paper or two", "help me scope this", "what's the contribution here", or "I have an idea but don't know how to frame it". Default to running this upstream of research-idea-stress-test (which vets one chosen idea) and paper-argument-planner (which structures a paper once the contribution is fixed). Always check first whether the input is sufficient (a seed, the field, the motivation); if not, request the missing context before brainstorming rather than inventing a direction. Hands off per-claim evidence to benchmark-and-baseline-selector, novelty grounding to literature-triangulation, and section logic to paper-argument-planner.
---

# Paper Idea and Scope Brainstormer

When the user has a rough idea, some results, or a problem, help them **diverge** into candidate paper framings and then **converge** on what this one paper should actually cover.

The deliverable is a **Paper Scoping Brief**: the central contribution, the in-scope vs. deferred boundary, and the coverage checklist needed to be complete and credible — *not* polished prose, not the argument spine, not the experiments themselves. Those come from downstream skills.

This skill is upstream. Brainstorm and scope here first, then hand off.

---

# Procedure

## 0. Context intake — gate before brainstorming

**Do not invent a research direction from a thin prompt.** First check whether the conversation supplies the context below. Pull what is present; for anything **required** that is missing, *ask the user* in one concise batch — do not guess. Brainstorming on top of a misread seed wastes the whole session, so it is always cheaper to ask first.

**Required — ask if absent:**
- **The seed** — the rough interest, problem, observation, or preliminary result that started this. If it is one vague phrase, ask what specifically sparked it.
- **Field / subfield** — so candidate framings and "what's already done" are grounded.
- **Motivation** — why this matters to the user (curiosity, a gap they hit, a result they got, a deadline).

**Helpful — pull if available, otherwise state an assumption:**
- Target venue / audience (shapes how big a contribution needs to be).
- Timeline / resources (a 6-week workshop paper scopes very differently from a year-long study).
- What's already done or available (preliminary results, code, data, prior papers by the user).
- Adjacent prior work the user already knows.

Surface any assumption you had to make in the final brief — never bury it.

## 1. Diverge — generate distinct framings

Produce several *genuinely different* answers to "this could be a paper about X." Force variety by rotating lenses, not by rewording one idea:

- **Problem reframing** — same observation, different question being asked.
- **Mechanism variation** — a different underlying cause or method to foreground.
- **Application / domain shift** — the same idea aimed at a different task or field.
- **Empirical vs. theoretical framing** — a measurement/benchmark paper vs. an analysis/proof paper.
- **Unit of contribution** — is the paper a *method*, a *hypothesis tested*, an *artifact* (dataset/benchmark/tool), or an *analysis/finding*?

Aim for 3–5 candidates that a reviewer would see as *different papers*, not paraphrases.

## 2. Name the contribution per candidate

For each candidate, write one line: the would-be contribution + its claim type (accuracy / efficiency / generalization / robustness / mechanism / new-resource / new-finding). This makes candidates comparable and exposes which ones are actually the same paper in disguise.

## 3. Converge on the spine

Pick **one central contribution** plus a small set of genuinely supporting contributions. Watch the two failure modes:

- **Salami-slicing / too thin** — the contribution is a single delta that won't carry a paper ("is this one paper or two" usually means *this half is too thin alone*). Merge or enrich.
- **Overstuffing** — two or three independent contributions crammed together. Split; name which one is *this* paper and which is the follow-up.

State plainly: this is one paper, or this should be two (and which is first).

## 4. Scope — in vs. out

The core "what to cover" deliverable. Write two explicit lists:

- **In scope** — the claims, methods, datasets/domains, and analyses this paper will cover.
- **Deferred / out of scope** — what belongs in a follow-up or a different paper, and one phrase on why it's cut (keeps the contribution sharp, avoids reviewer "why didn't you also…" by pre-empting it as future work).

## 5. Coverage checklist

What the paper must cover to be complete and credible. Delegate the depth, don't duplicate it:

- **Claims → evidence** — list each in-scope claim and the *kind* of evidence it needs. Hand the actual baseline/benchmark selection to `benchmark-and-baseline-selector`.
- **Related-work coverage** — the bodies of work that must be positioned against; hand grounding to `literature-triangulation`.
- **Theory coverage** — any guarantee/derivation the claims imply (if applicable).
- **High-level section needs** — which sections this paper requires; hand the argument spine and section logic to `paper-argument-planner`.

## 6. Risks and handoffs

Name the 2–3 biggest threats to the idea (likely-strong baseline already exists, novelty is thin vs. known work, the claim may not be falsifiable cheaply). Then route to the right next skill (see below). Recommend `research-idea-stress-test` as the immediate next step for the chosen spine.

---

# Output format

```
Working title: <tentative>
Thesis (one sentence): <what this paper claims>

Candidate angles considered:
  1. <framing> — contribution: <…> [claim type]
  2. <framing> — contribution: <…> [claim type]
  ... (3–5)
Chosen: #<n> — because <why this one>

Contributions:
  Central:    <the one>
  Supporting: <small set>
One paper or two: <verdict + which is first if split>

Scope:
  In scope:  <claims / methods / datasets / analyses>
  Deferred:  <what's cut> — because <why>

Coverage checklist:
  - <claim> → evidence needed: <kind>   (→ benchmark-and-baseline-selector)
  - Related work to position against: <bodies of work>  (→ literature-triangulation)
  - Theory to cover: <…/none>
  - Sections required: <high level>      (→ paper-argument-planner)

Key risks: <2–3>
Next step: research-idea-stress-test on the chosen spine
Assumptions made: <inferred context — omit if none>
```

Lead with the chosen spine and the in/out-of-scope split — that is the answer to "what should this paper cover." Keep the candidate list short and the brief scannable.

---

# When not to use this skill

- The idea is already chosen and you want to vet whether it's worth pursuing / novel / falsifiable → `research-idea-stress-test`.
- The contribution is fixed and you want the argument spine and section logic → `paper-argument-planner`.
- You need the actual baselines/benchmarks for a claim → `benchmark-and-baseline-selector`.
- You need a grounded literature map or novelty check → `literature-triangulation`.
- You need to plan figures/tables → `figure-table-planner`.

This skill is **upstream** of all of these: brainstorm and scope here, then hand off.
