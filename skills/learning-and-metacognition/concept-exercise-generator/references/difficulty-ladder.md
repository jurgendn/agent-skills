# Difficulty Ladder

Four tiers, easy → advanced. The ladder mirrors a research-flavored Bloom progression: recall → apply → analyze → create. Pick problems so the set spans tiers; never ship a "self-check" that stops at Tier 2.

## Tier 1 — Recall & Recognize (easy)

**Tests:** vocabulary, definitions, recognizing which method/family/assumption applies.
**Verbs:** define, state, identify, name, match, list, recognize.
**Passes when:** the learner reproduces the term/definition/classification without looking it up.
**Does NOT verify understanding** — only that the words are in place. Necessary floor, not the goal.

Examples of problem shapes:
- "Define X in one sentence."
- "Which method family does X belong to, and what is the one assumption it makes?"
- "Match each term to its definition."

## Tier 2 — Apply & Compute (medium)

**Tests:** running the mechanism on a small, concrete case.
**Verbs:** compute, trace, simulate, predict, plug in, execute, evaluate.
**Passes when:** the learner produces the right output on a toy input by actually carrying out the procedure.
**Verifies mechanism**, not yet meaning.

Examples:
- "Compute the output of X for this 2×2 input by hand."
- "Trace the algorithm on this 4-element list; show each step."
- "Predict what happens to the loss if you double the learning rate here."

## Tier 3 — Analyze & Compare (hard)

**Tests:** *why* the method exists, when it breaks, how it trades off against alternatives.
**Verbs:** contrast, diagnose, justify, choose, explain-why, predict-failure, attribute.
**Passes when:** the learner reasons about pressure and trade-offs, not just procedure.
**This is the first tier that actually verifies understanding.** Always include ≥1.

Examples:
- "Why is attention *scaled* by √d? What goes wrong if you don't?"
- "Method A and B both solve this. Under what data condition does A fail and B win?"
- "Here is a result that looks wrong. Which assumption was violated?"

## Tier 4 — Build, Derive & Break (advanced)

**Tests:** generative mastery — deriving, constructing, critiquing, extending.
**Verbs:** derive, construct a counterexample, critique, design a variant, generalize, propose.
**Passes when:** the learner creates something correct that wasn't handed to them.

Examples:
- "Derive the gradient of this loss from scratch."
- "Construct an input where this method provably fails."
- "Critique the central claim of the paper: what would you need to see to believe it?"
- "Design the smallest modification that fixes failure mode Y; argue why it works."

## Default spreads by budget / depth target

| Budget / target | T1 | T2 | T3 | T4 | Total |
|-----------------|----|----|----|----|-------|
| Quick self-check (~15 min) | 1 | 1 | 1 | 1 | 4 |
| Standard (~45 min) | 2 | 2 | 2 | 1 | 7 |
| Mastery pass (multi-hour) | 2 | 3 | 4 | 3 | 12 |
| "Can read papers" target | 1 | 2 | 3 | 1 | 7 |
| "Can build" target | 1 | 2 | 3 | 3 | 9 |

Center the ladder on the learner's current level but **always reach one tier above it** — that next-tier problem is what tells the learner (and the orchestrator) whether they are ready to move on.

## Mapping to learning-flow stages

When called from `flow-learn-new-topic`, tiers map to the stage whose exit gate they verify:

- Stage 1–2 (orient, map) → Tier 1–2 checkpoint.
- Stage 3 (core intuition) → Tier 3 checkpoint (the "explain *why*" gate).
- Stage 4 (toy cases) → Tier 2 + a Tier 3 checkpoint.
- Stage 5 (bridge to papers) → Tier 4 checkpoint (critique/derive on a real source).
