# Drafting Reference

Use for Phase 2 section drafting, ordering, and revision loops. Distills Whitesides (outline-first), Kallestinova (methods-first and draft/revision separation), and Halmos's spiral rewriting.

## Operational Rules

- [EXPERT] Draft from an outline before writing prose. The outline should contain claims, figures/tables/theorems, and paragraph jobs, not just section names.
- [EXPERT] Draft the technical core first: method, theorem/proof, construction, algorithm, or experimental setup. This is where hidden weaknesses surface.
- [EXPERT] Draft results/experiments after the technical core, because results prose must state what was actually tested rather than what the method hoped to show.
- [EXPERT] Draft the introduction late enough that it can honestly advertise the paper, but keep the Phase 1 skeleton visible so the story does not drift.
- [EXPERT] Draft the abstract last. It should compress the final story, not forecast a story that later sections fail to support.
- [EXPERT] Do not edit while drafting. Use placeholders such as `[define conductance here]`, `[insert ablation table]`, or `[citation needed: dynamic community detection survey]`.
- [EXPERT] Use Halmos's spiral revision: after drafting a new section, revisit earlier sections and adjust definitions, notation, motivation, or promises that the new section made obsolete.
- [EXPERT] Stop drafting when a missing proof, missing experiment, or unsupported claim blocks the current section. Record it as a blocking placeholder rather than writing around it.

## Section Order

Default order for theorem-proof papers:

```markdown
1. Definitions and setup
2. Main theorem statements
3. Proof ideas
4. Proof details
5. Examples, tightness, or limitations
6. Related work positioning
7. Introduction
8. Abstract
```

Default order for ML papers:

```markdown
1. Problem setup and method
2. Experimental setup
3. Main results
4. Ablations and analysis
5. Limitations
6. Related work positioning
7. Introduction
8. Abstract
```

Default order for graph ML hybrids:

```markdown
1. Formal setup and assumptions
2. Method or algorithm
3. Theoretical result and proof sketch
4. Experimental setup
5. Main results and ablations
6. Limitations and assumption checks
7. Related work positioning
8. Introduction
9. Abstract
```

## Per-Section Gate Details

- [EXPERT] The first paragraph must state the section's job: define objects, prove a claim, describe an algorithm, report an experiment, position literature, or explain limitations.
- [EXPERT] A forward dependency is acceptable only as a visible placeholder, for example: `[forward pointer: define evaluation metric after Table 1 exists]`.
- [EXPERT] Every section must resolve at least one row in the claims-to-evidence map.

## Drafting Output Pattern

For each section, produce:

```markdown
## <Section>

Purpose:
Claims supported:
Required artifacts:
Known placeholders:

Draft:
<prose>

Gate:
- [ ] Purpose in first paragraph
- [ ] No unmarked forward dependency
- [ ] Claims mapped to evidence
```
