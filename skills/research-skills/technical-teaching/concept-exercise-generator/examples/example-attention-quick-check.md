# Example — Quick self-check on scaled dot-product attention

Calibration example for a `~15 min` self-check (4-problem spread: T1, T2, T3, T4). Source material assumed: the learner has read the "Attention" section of a transformers tutorial. Note the two files are emitted separately.

---

## `exercises.md`

```text
# Exercises — Scaled dot-product attention
Attempt every problem before opening solutions.md. Write your answer down; a vague
mental "yeah I know this" is the thing these problems exist to catch. Then score
yourself against the rubric in solutions.md.

1. [Tier 1 · definition] In one sentence, what does the attention operation
   softmax(QKᵀ/√d)V compute, in plain terms?

2. [Tier 2 · mechanism] Given query q = [1, 0], keys k₁ = [1, 0], k₂ = [0, 1],
   and d = 2, compute the two attention weights (the softmax over the scaled
   dot products). Show the scaled scores before softmax.

3. [Tier 3 · why] Why is the dot product divided by √d before the softmax?
   What specifically goes wrong as d grows if you remove the scaling?

4. [Tier 4 · break] Construct a small set of keys and a query for which attention
   behaves almost like a hard lookup (nearly all weight on one key), and explain
   what property of the inputs causes it.
```

## `solutions.md`

```text
# Solutions — Scaled dot-product attention
Gate rule: you've verified understanding only if Problems 3 and 4 pass unaided.
Clearing 1–2 alone means re-study, not progress.

1. [Tier 1 · definition]
   Answer: A weighted average of the value vectors, where each value's weight is
   how well its key matches the query.
   Why: softmax(QKᵀ/√d) turns query–key similarities into weights that sum to 1;
   multiplying by V averages the values under those weights.
   ✅ You've got it if: you said "weighted average of values, weights from
   query–key similarity" in any phrasing.
   ⚠️ Common wrong turn: describing the matrix shapes but not that the output is
   a convex combination of values.
   ↩ Revisit if missed: the definition of the attention operation.

2. [Tier 2 · mechanism]
   Answer: scaled scores = [1/√2, 0] ≈ [0.707, 0]; weights ≈ [0.670, 0.330].
   Why: q·k₁ = 1, q·k₂ = 0; divide by √d = √2 → [0.707, 0]; softmax([0.707, 0])
   = [e^0.707, e^0]/(e^0.707 + e^0) ≈ [2.028, 1]/3.028 ≈ [0.670, 0.330].
   ✅ You've got it if: scores divided by √2 and softmax applied correctly.
   ⚠️ Common wrong turn: forgetting to scale (softmax([1,0]) ≈ [0.731, 0.269]).
   ↩ Revisit if missed: the toy computation of attention weights (Tier 2).

3. [Tier 3 · why]
   Answer: Without scaling, dot products grow with d, pushing softmax into a
   saturated regime where one weight ≈ 1 and gradients vanish; dividing by √d
   keeps the score variance ~constant in d.
   Why:
     - For unit-variance independent q, k entries, q·k has variance d.
     - Large-magnitude logits make softmax near one-hot → tiny gradients → slow
       or stalled learning.
     - √d normalizes the std back to ~1, keeping softmax in a usable range.
   ✅ You've got it if: you named BOTH the variance-grows-with-d cause AND the
   saturated-softmax/vanishing-gradient consequence.
   ⚠️ Common wrong turn: "it normalizes things" with no mention of variance or
   gradient saturation — right verdict, missing why.
   ↩ Revisit if missed: the scaling motivation; redo with the variance argument.

4. [Tier 4 · break]
   Answer (one valid construction): q = [10, 0], k₁ = [10, 0], k₂ = [0, 10].
   Scaled scores = [100/√2, 0] ≈ [70.7, 0]; softmax ≈ [~1, ~0]. Nearly all weight
   on k₁ → near-hard lookup of value 1.
   Why: large key/query magnitudes make one scaled score dominate, so softmax
   saturates toward one-hot. The driver is the *magnitude/separation* of the
   matching key, not just its direction.
   ✅ You've got it if: your construction makes one scaled score dominate (large
   magnitude or wide separation) AND you attribute the hardness to that, not to
   the number of keys.
   ⚠️ Common wrong turn: building a case with similar-magnitude keys and expecting
   hard selection — softmax stays soft. Magnitude is the lever.
   ↩ Revisit if missed: the link between logit magnitude and softmax sharpness
   (connects back to Problem 3).
```
