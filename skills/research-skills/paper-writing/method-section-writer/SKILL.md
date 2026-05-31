---
name: method-section-writer
description: Draft or revise the method (approach / model / framework) section of a research paper. Use whenever the user needs to write or improve this section — including phrasings like "write my method section", "how do I describe my model", "my method section is too long / too vague / too dense", "how much detail do I need", "how do I present the algorithm", "write the approach section", or "explain my method clearly". Also use when the notation is inconsistent, the section jumps between abstraction levels, or reviewers complained the method is hard to follow. If the paper's overall argument is not yet stable, use paper-argument-planner first. If the abstract and introduction are not yet written, use abstract-and-intro-writer first.
---

# Method Section Writer

The method section has one job: give the reader enough understanding to evaluate whether the claimed results are plausible and, in principle, to reproduce the work.

It is not a complete implementation guide. It is not a tutorial on all the components the method builds on. It is the minimal formal description needed to understand what is new and why it should work.

---

## The two failure modes

**Too dense**: a wall of notation introduced all at once, multiple sub-components presented at the same abstraction level, equations without motivation. The reader can follow each line but cannot see the idea.

**Too vague**: prose that describes what the method does without saying how. "We encode the input using a contextual representation" is not a method — it's a description of the output. A reader cannot reproduce this or evaluate whether it's novel.

The target: present the key idea with enough precision that a skeptical reviewer can check whether the contribution is real.

---

## Workflow

### 1. Identify the method's core components

Before writing, enumerate:

- What is genuinely new in this method?
- What is standard and can be cited rather than explained?
- What are the sub-components? Which ones are central to the claim and which are engineering choices?

Write a dependency tree: which components must be understood before others? That tree is the section's structure.

**The central component gets the most space.** Everything else is either cited (if standard) or briefly described (if an engineering choice).

---

### 2. Set up notation before equations

Notation errors are among the most common reviewer complaints. Introduce notation in one place, early in the section, before any equations that use it.

For each symbol, state:
- what it represents;
- its type and shape (scalar, vector, matrix, set, function);
- its range or domain if non-obvious.

```
Let G = (V, E) be a graph with node set V (|V| = n) and edge set E ⊆ V × V.
Each node v ∈ V has a feature vector x_v ∈ ℝ^d.
We denote the adjacency matrix as A ∈ {0,1}^{n×n} and the degree matrix as D.
```

Rules:
- Reuse the same symbol for the same concept throughout the paper.
- Use subscripts consistently (time index, layer index, batch index — pick one convention per subscript position).
- Bold for vectors and matrices; italic for scalars — or state your convention explicitly.
- Never introduce a symbol in a figure caption before it appears in the text.

---

### 3. Structure the section

A method section for a deep learning paper typically has this structure:

```
3. Method
  3.1 Problem formulation       ← define input, output, and objective
  3.2 [Core component name]     ← the main novel contribution
  3.3 [Secondary component]     ← only if needed for the claim
  3.4 Training objective        ← loss function, optimization details
  3.5 Complexity (optional)     ← only if runtime is part of the contribution
```

Adjust for the paper type:
- **Theory paper**: Problem → Formulation → Main theorem statement → Proof sketch → Corollaries.
- **System paper**: Problem → Architecture overview → Component design → Implementation details → Analysis.
- **Dataset/benchmark paper**: Task definition → Data collection → Annotation protocol → Quality controls → Statistics.

Avoid sections named "Overview" or "Approach" without a more specific subtitle — these signal that the author hasn't decided what the section is doing.

---

### 4. Present the key idea before the full formulation

State the intuition first, then formalize it. Reviewers who understand the intuition are more likely to follow the math.

Structure per sub-component:

1. **Motivation**: why does this component exist? What problem does it solve that simpler alternatives don't?
2. **Intuition**: what is the idea, in words?
3. **Formalization**: the equation or algorithm.
4. **Interpretation**: what does the formalization say, in words? Point to the key term.

Example:

```
Adaptive walk length. Fixed walk-length methods treat all graphs uniformly,
ignoring that mixing time varies with graph density. We select the walk length
proportional to the inverse spectral gap, which captures how quickly information
spreads across the graph.

Formally, given graph G with normalized Laplacian eigenvalues 0 = λ_1 ≤ λ_2 ≤ ... ≤ λ_n,
we define the adaptive walk length as:

    t* = ⌈1 / λ_2⌉                               (1)

where λ_2 is the Fiedler value. Intuitively, small λ_2 (slow mixing) requires
longer walks to capture community structure; large λ_2 (fast mixing) allows
shorter walks without information loss.
```

---

### 5. Algorithm boxes

Use an algorithm box when:
- The method is procedural with a clear sequence of steps.
- The paper is about a training procedure or inference algorithm.
- Reviewers need to verify pseudocode to evaluate correctness.

Do not use an algorithm box when:
- The method is a single equation.
- The procedure is a standard training loop with minor modifications.

Algorithm box conventions:
- Name the algorithm.
- List inputs and outputs explicitly.
- Number lines.
- Match variable names in the box to variable names in the text.
- Keep it to 10–15 lines; move sub-routines to appendix if longer.

---

### 6. Figures in the method section

The method figure (architecture diagram, pipeline visualization) is usually the most-viewed figure in the paper. It should:

- Show the data flow end-to-end.
- Use the same variable names as the text.
- Be readable at the column width where it will appear.
- Not require reading the caption to understand the structure.

One method figure is almost always better than two. If multiple figures are needed, each should show a different component — not two views of the same thing.

---

### 7. What belongs in appendix

Move to appendix:
- Full proofs (state the theorem in main text, defer proof).
- Hyperparameter tables.
- Implementation details that don't affect the core method (framework version, GPU type).
- Extended derivations.
- Failure cases and sensitivity analysis beyond the main ablation.
- Dataset details beyond what's needed to understand the experiment.

Never move to appendix:
- The definition of the loss function.
- The notation table (if long, put in appendix but reference it early in main text).
- Any component that the main results depend on.

---

### 8. Level of detail calibration

Ask for each component: "Could a reader implement this from the main text alone?"

If the answer is no for the core contribution, add detail.
If the answer is yes for a standard component (e.g., multi-head attention), you have too much detail — cite the original paper instead.

A good test: cover the equations and read only the prose. Does the reader still understand what the method does and why? If yes, the prose is doing its job. If no, the prose is just a caption for the equations.

---

### 9. Training objective

The loss function and optimization setup need at minimum:
- The loss function with full notation (not "cross-entropy loss" — write it out or cite the formulation).
- Whether the objective is end-to-end or has separate training stages.
- Any regularization terms and their hyperparameter names (even if values go in the experiments section).
- Optimizer name and key hyperparameters (learning rate schedule, weight decay).

If the loss function is non-standard or is itself a contribution, it gets its own subsection.

---

## Common reviewer complaints and how to prevent them

| Complaint | Root cause | Fix |
|---|---|---|
| "Notation is inconsistent" | Symbol reuse or undefined symbols | Notation table at start of section |
| "I can't tell what's new vs. prior work" | No explicit novelty markers | Add "Unlike [X], our method..." or "The key difference is..." |
| "The method is underspecified" | Prose without equations for non-trivial steps | Add formal definition for each novel component |
| "The method is over-specified" | Step-by-step implementation details for standard components | Cite and refer; don't re-derive |
| "I don't understand why this works" | Intuition missing | Add one sentence of motivation before each equation |
| "The figure doesn't match the text" | Variables diverge between text and diagram | Audit every symbol in both |

---

## Output format

```markdown
# Method Section Draft

## [Section number]. Method / Approach / [Custom name]

### [N.1] Problem formulation

[Input, output, objective — with full notation setup]

### [N.2] [Core component]

[Motivation → Intuition → Formalization → Interpretation]

[Equation / Algorithm box if applicable]

### [N.3] [Secondary component — if needed]

...

### [N.4] Training

[Loss function, optimizer, training procedure]

---

## Notes

**Notation defined:** [list of all symbols introduced]
**Moved to appendix:** [list with reason]
**What to cite rather than explain:** [list]
**Figures needed:** [description of each, with what it should show]
**Reviewer risks:** [anything likely to draw pushback, with mitigation]
```

When revising an existing draft, also include:
```markdown
## Diagnosis
[Which failure mode(s) the current draft has]

## Changes made and why
```

---

## Quality bar

After reading the method section, a reviewer should be able to: (1) state the core idea in one sentence, (2) identify what is new vs. prior work, (3) sketch the forward pass or algorithm, and (4) know which components are novel and which are standard. If any of these fail, the section needs revision.
