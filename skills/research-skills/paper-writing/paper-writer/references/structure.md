# Structure Reference

Use for Phase 1 story, paper skeleton, claims-to-evidence mapping, and introduction planning. Distills Simon Peyton Jones, "How to Write a Great Research Paper", and Mensh & Kording, "Ten Simple Rules for Structuring Papers" (PLOS Computational Biology, 2017).

## Operational Rules

- [EXPERT] Build the paper around one central contribution. If the author needs three unrelated contribution sentences, the project is probably several papers or the story is not yet understood.
- [EXPERT] The introduction is a contract with the reader: problem, why it matters, why it is hard, what this paper does, and where the evidence appears.
- [EXPERT] Make contributions explicit and falsifiable. Prefer "We prove/show/introduce X under Y conditions" over "We study X".
- [EXPERT] Map every contribution to a later section. A contribution without a section is an orphan claim; a section without a mapped claim is likely baggage.
- [EXPERT] Let the paper structure follow the argument, not the project chronology. Failed attempts, implementation history, or discovery order belong only when they help the reader trust the final claim.
- [EXPERT] Give readers a navigation layer early: after the contribution list, state which section proves, implements, evaluates, or contextualizes each contribution.
- [EXPERT] For mathematics venues, make the skeleton theorem-forward: definitions/preliminaries, main theorem(s), proof strategy, proof details, examples/counterexamples, comparison with known results.
- [EXPERT] For ML venues, make the skeleton claim-and-evidence-forward: task/problem, method, experimental setup, baselines, main results, ablations, limitations, reproducibility.
- [EXPERT] For graph ML hybrids, separate theorem claims from empirical claims in the map. Do not let a theorem imply empirical performance unless the experiment actually tests that bridge.

## Phase 1 Templates

One-sentence contribution:

```markdown
This paper <proves/proposes/introduces/shows> <new claim or method> for <specific setting>, by <core idea>, supported by <proof/experiment/artifact>.
```

Claims-to-evidence map:

```markdown
| Claim | Evidence type | Supporting section | Status |
| --- | --- | --- | --- |
| <claim> | theorem / experiment / ablation / example / citation | Section <n> | planned / drafted / verified |
```

Introduction skeleton:

```markdown
1. Problem:
2. Why it matters:
3. Why it is hard:
4. Existing approaches and gap:
5. What we do:
6. Contributions:
   - Contribution 1 -> Section <n>
   - Contribution 2 -> Section <n>
7. Reader roadmap:
```

## Gate Failure Patterns

- [EXPERT] "We study..." without a concrete new result usually fails the one-contribution gate.
- [EXPERT] "Our contributions are threefold..." fails if one item is only a paper-writing activity, such as "we provide background".
- [EXPERT] A contribution like "we show strong performance" fails unless the map names the benchmark, metric, baseline family, and results section.
