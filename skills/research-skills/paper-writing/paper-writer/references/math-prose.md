# Mathematical Prose Reference

Use for Phase 3 notation, theorem statements, proof prose, and graph/math/ML formalism. Distills Halmos, "How to Write Mathematics" (1970), and Knuth, Larrabee, and Roberts, "Mathematical Writing" (first three sections).

## Operational Rules

- [EXPERT] Treat notation as part of the prose. A symbol is a word with memory; once assigned, it should not quietly change role.
- [EXPERT] Build a notation table before line-editing mathematical sections: symbol, meaning, type/domain, first definition, and collisions.
- [EXPERT] Define every symbol before use. If a theorem uses $G$, $V$, $E$, $t$, $C$, or $f_\theta$, their roles must be known before the statement depends on them.
- [EXPERT] Avoid dissonant collisions. Do not use $C$ for both a community and a constant, or $d$ for both degree and distance, unless the local context makes the distinction impossible to miss.
- [EXPERT] Replace vague "any" with "each" or "every" when the intended statement is universal. Keep "any" only when the choice really is arbitrary and the ambiguity is harmless.
- [EXPERT] Make theorem statements self-contained. Hypotheses, domains, quantifiers, and parameter ranges belong in the theorem statement rather than only in the paragraph before it.
- [EXPERT] Put a one-sentence proof idea before every nontrivial proof. The reader should know the invariant, construction, induction, coupling, reduction, or contradiction before seeing details.
- [EXPERT] Remove intimidation phrases. Each "clearly", "it is easy to see", or "by a standard argument" must be justified, cited, or deleted.
- [EXPERT] Prefer sentences that carry mathematics over symbol-only fragments. A displayed equation should be introduced by prose that says what role it plays.
- [EXPERT] For graph ML papers, separate mathematical objects from learned objects: graph $G$, node set $V$, adjacency $A$, embedding $h_v$, model parameters $\theta$, and predicted label $\hat{y}$ should not blur.

## Phase 3 Checklist Details

Notation table:

```markdown
| Symbol | Meaning | Type/domain | First defined | Collision risk |
| --- | --- | --- | --- | --- |
| <symbol> | <meaning> | <set/type/range> | <section/paragraph> | none / <conflict> |
```

Theorem audit:

```markdown
| Theorem | Hypotheses inside statement? | Symbols defined before use? | Re-readable alone? | Repair |
| --- | --- | --- | --- | --- |
| <label> | yes/no | yes/no | yes/no | <rewrite needed> |
```

Proof audit:

```markdown
| Proof | Proof idea line? | Hidden lemma? | "clearly/easy/standard" issue? | Repair |
| --- | --- | --- | --- | --- |
| <label> | yes/no | <item> | <quoted text> | <rewrite/cite/remove> |
```

## Rewrite Pattern for Scattered Hypotheses

Problem pattern:

```markdown
Assume $G$ is a connected graph with maximum degree $\Delta$ and let $p > 1/2$.

Theorem. The recovery procedure succeeds with probability at least $1-\epsilon$.
```

Repair:

```markdown
Theorem. Let $G=(V,E)$ be a connected graph with maximum degree $\Delta$, and let $p > 1/2$. Under <named observation model>, the recovery procedure in Algorithm 1 succeeds with probability at least $1-\epsilon$.
```

The repair is [EXPERT] because it follows mathematical-writing craft consensus, not a measured citation effect.
