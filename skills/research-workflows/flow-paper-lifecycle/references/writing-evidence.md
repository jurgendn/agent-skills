# Evidence Reference

Use whenever giving writing advice that sounds empirical: citations, readability, title length, abstract length, or discipline-specific style. The main rule is epistemic discipline: do not turn craft advice into fake data.

## Flag Meanings in Practice

- [EXPERT] Writing-guide consensus or senior-practitioner advice; often useful, but not established by controlled evidence.
- [SUPPORTED] Empirical backing exists, usually correlational rather than causal.
- [CONTESTED] Studies disagree, definitions differ, or the effect is field-specific.
- [REFUTED] A common claim is contradicted by the cited empirical evidence.

## Empirical Layer

- [SUPPORTED] Readability is associated with citation outcomes in large-scale bibliometric studies, including Weinberger, Evans, and Allesina (PLOS Computational Biology, 2015) and work finding that highly cited NeurIPS papers score as more readable. Treat this as correlational: readable papers may be cited more, but quality, venue, topic, author network, and timing also confound citations.
- [SUPPORTED] For mathematics and physics, Weinberger, Evans, and Allesina (2015) report that shorter sentences are associated with more citations. For math/graph ML authors, the actionable rule is concise sentences and reduced syntactic load, not reduced technical content.
- [REFUTED] "Make the abstract ultra-short to get cited more" is not supported. Weinberger, Evans, and Allesina (2015) found shorter abstracts received fewer citations across all eight tested disciplines.
- [CONTESTED] Title length advice is unstable. Letchford et al. (2015) and Didegah & Thelwall (2013) point in different directions depending on corpus, field, and modeling choices. Do not promise that short titles increase citations.
- [EXPERT] Outline-first, methods-first, no-editing-while-drafting, theorem self-containment, proof-idea lines, and spiral rewriting are craft rules from writing guides. Use them as practical heuristics, not as measured citation levers.

## How to Answer Common Evidence Questions

Question: "Should I keep the abstract really short to get cited more?"

Answer pattern:

```markdown
[REFUTED] No. The empirical result you want does not support ultra-short abstracts: Weinberger, Evans, and Allesina (2015) found shorter abstracts got fewer citations across all eight disciplines they tested.

[SUPPORTED] For mathematics and physics, the more relevant finding is about shorter sentences, not shorter abstracts. For a math/graph ML paper, write a complete abstract with concise sentences: problem, gap, method/theorem, evidence, and implication.
```

Question: "Should the title be short?"

Answer pattern:

```markdown
[CONTESTED] Maybe, but do not optimize title length as a citation hack. Evidence conflicts across Letchford et al. (2015) and Didegah & Thelwall (2013). Use the shortest title that accurately names the object, method, and contribution without becoming cryptic.
```

Question: "Can I use clearly or easy to see?"

Answer pattern:

```markdown
[EXPERT] Avoid it unless you immediately justify the step or cite the standard result. This is a mathematical-prose hygiene rule from Halmos/Knuth-style craft consensus, not an empirical citation result.
```

## Citation Details to Preserve

- Weinberger, Evans, and Allesina, PLOS Computational Biology, 2015: large-scale abstract/readability/citation study; use for readability, sentence length, and abstract-length claims.
- Letchford et al., 2015: title length/citation study; use only as one side of a contested title-length claim.
- Didegah & Thelwall, 2013: title length/citation-impact study; use only as one side of a contested title-length claim.
- Mensh & Kording, 2017: paper-structure craft guide; flag as [EXPERT] unless the specific claim is separately empirical.
