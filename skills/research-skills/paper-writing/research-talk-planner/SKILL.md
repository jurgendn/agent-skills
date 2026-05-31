---
name: research-talk-planner
description: Plan and structure a research talk (conference presentation, seminar, invited talk, or job talk) from a paper, set of results, or research overview. Use whenever the user needs to turn a paper into slides, structure a 15/20/30/45/60-minute talk, decide what to cut for a short slot, plan a job talk narrative, or figure out how to present technical content to a mixed audience. Also use when the user asks "how do I present this paper", "what should my slides cover", "how long should each section be", or "I only have 15 minutes". A talk is not a paper read aloud — the narrative arc, pacing, and depth of detail must be rebuilt from scratch for a listening audience.
---

# Research Talk Planner

A talk is not a paper read aloud and it is not a set of slides with all the paper's content compressed in. It is a live argument designed for a specific audience, a specific time slot, and a specific goal.

The paper can be wrong about what matters. A reviewer reads every section; an audience hears the talk once, cannot rewind, and will remember one thing. The skill is deciding what that one thing should be and building the entire talk around it.

---

## Talk types and their goals

| Talk type | Primary goal | Typical length |
|---|---|---|
| Conference talk | Communicate the core contribution clearly; invite follow-up | 12–20 min + questions |
| Seminar / colloquium | Build understanding of the problem and method; generate discussion | 45–60 min + questions |
| Job talk | Demonstrate research taste, depth, and future potential | 45–60 min + questions |
| Workshop / spotlight | Spark interest; send people to the paper or poster | 5–10 min |
| Thesis defense | Show mastery of a body of work | 30–45 min + committee Q&A |

The goal determines what gets cut and what gets elaborated. A workshop spotlight should end with one memorable result and a pointer to the poster. A job talk must show a research program, not just a paper.

---

## Workflow

### 1. Establish the constraints

Before planning any content:

- **Time slot**: exact minutes available for the talk (not including questions).
- **Audience**: specialists in the subfield / broader ML crowd / mixed academic-industry / undergraduates.
- **Venue context**: single-track conference / workshop / department seminar / job talk.
- **Goal**: what do you want the audience to do or believe after the talk?
- **Available materials**: paper, slides draft, figures, results.

---

### 2. Find the one thing

Every talk has one central takeaway — the single idea an audience member will remember three days later. This is almost never the full contribution list from the paper.

Write it as one sentence before touching any slides:

```
The audience should leave knowing: [one concrete, memorable claim].
```

Good:
```
Adaptive walk length, chosen from the graph's spectral gap, consistently
outperforms fixed-length baselines on dynamic community detection — 
and the reason is surprisingly simple.
```

Bad:
```
We propose a novel method with theoretical guarantees and strong
empirical performance across five benchmarks.
```

The second version is the abstract, not the talk's takeaway. The audience cannot hold five benchmarks in working memory; give them one clear result and the insight behind it.

---

### 3. Build the talk arc

A research talk has four movements, regardless of length. The time budget shifts with slot length, but the movements stay.

**Movement 1 — The problem (why should I care?)**
Open with a concrete scenario, a failure case, or a vivid example. Not "graph neural networks have been widely studied" — something that makes the problem feel real and urgent. The audience grants you 60–90 seconds to earn their attention; use it.

**Movement 2 — Why existing work falls short**
One or two slides. Specific, not dismissive. "Prior work assumes X; that assumption fails when Y." This is the gap that makes the rest of the talk necessary.

**Movement 3 — The idea and method**
The core contribution. Present the key insight before the full method — the intuition should be graspable before the equations. Use one strong visual. If the method has multiple components, present the most important one clearly rather than all of them superficially.

**Movement 4 — Evidence and implication**
The headline result, on one clear slide. Then one or two supporting results. End with what this means — not "future work," but why the result changes something.

---

### 4. Allocate time per movement

Use these as starting points; adjust for the specific content.

| Slot | Problem | Gap | Idea + Method | Evidence | Close |
|---|---|---|---|---|---|
| 10 min | 1 min | 1 min | 4 min | 3 min | 1 min |
| 15 min | 2 min | 1 min | 5 min | 5 min | 2 min |
| 20 min | 2 min | 2 min | 7 min | 7 min | 2 min |
| 30 min | 3 min | 3 min | 10 min | 10 min | 4 min |
| 45 min | 5 min | 5 min | 15 min | 15 min | 5 min |
| 60 min | 7 min | 5 min | 20 min | 20 min | 8 min |

**One slide per minute** is the right default pacing. A 20-minute talk should have roughly 18–22 slides including title and questions slide. Fewer slides with more time per slide is almost always better than more slides with less time.

---

### 5. Slide design principles

**Title slide**: paper title, your name, venue and date. Nothing else.

**Each slide has one job.** If you catch yourself writing "and also..." in the slide notes, that's a second slide.

**Lead with the claim, not the figure.** Put the takeaway in the slide title, not a neutral label.
- Bad title: "Experimental Results"
- Good title: "Adaptive walks outperform fixed-length on all 5 benchmarks"

**Equations need scaffolding.** Introduce notation before showing the equation. Build equations incrementally — show the full form only after the pieces are understood.

**Animations should reveal, not decorate.** Use builds to guide attention: show the baseline first, then overlay the result. Don't animate for visual interest.

**The key figure from the paper is usually your best slide.** If it's designed well, use it. If it needs too much explanation, simplify it for the talk version.

---

### 6. What to cut

For every time pressure, cut in this order:

1. **Related work details**: name the key papers, don't describe them. "Prior work [Smith '20, Jones '21] addressed X but not Y" is enough.
2. **Method components that aren't central to the main claim**: mention them exist, don't explain them.
3. **Secondary results and ablations**: keep only the one ablation that most directly validates the core mechanism.
4. **Proof details**: state the theorem and its implication; defer the proof to the paper.
5. **Dataset preprocessing steps**: unless the dataset itself is a contribution.

Never cut: the problem motivation, the key insight, and the headline result. These are load-bearing.

---

### 7. The close

Do not end with "future work" or "thank you for your attention." End with the one thing — a single sentence that restates the core takeaway, optionally followed by a paper/poster pointer.

```
Take-home: spectral-gap-adaptive walks are not just empirically better —
they expose why the walk length matters and when to trust the community structure.
[Paper: arxiv.org/abs/XXXX | Code: github.com/...]
```

Then leave the title slide or a "Questions?" slide on screen during Q&A — not a summary slide with bullet points.

---

### 8. Job talk additions

A job talk has a different structure because it must demonstrate a research program, not just one paper.

Additional elements:
- **Research vision** (5 min): where is the field going and what role does your work play?
- **Multiple projects** (if applicable): 2–3 papers connected by a coherent theme, not a list of everything you've done.
- **Future directions** (5 min): specific, ambitious, and grounded in your demonstrated capabilities.

Audience is evaluating: depth (do they really understand this?), taste (are they working on the right things?), and potential (what will they do next?). Every slide should contribute to at least one of these.

---

### 9. Q&A preparation

For each major result, anticipate the hardest question and have a one-sentence answer ready. Common question types:

- "Why didn't you compare against X?" → have the reason ready.
- "Does this work when Y?" → know the scope of the claim.
- "How does this relate to Z?" → know the nearest neighbors in the field.
- "What's the main limitation?" → answer honestly and specifically.

It is fine to say "I don't know, but that's a great direction" — but only once per Q&A.

---

## Output format

```markdown
# Talk Plan: [Paper title]

## Constraints
- Slot: [n] minutes
- Audience: [description]
- Goal: [what the audience should believe or do]

## The one thing
[One sentence — the single memorable takeaway]

## Talk arc

### Movement 1 — Problem ([n] min, ~[n] slides)
[What scenario / failure case / example opens the talk]
[How to make the problem feel real and urgent]

### Movement 2 — Gap ([n] min, ~[n] slides)
[Specific claim about what existing work fails to do]
[Key paper(s) to mention (briefly)]

### Movement 3 — Idea and method ([n] min, ~[n] slides)
[Core insight in one sentence]
[Key visual or diagram]
[What to explain vs. what to defer]

### Movement 4 — Evidence ([n] min, ~[n] slides)
[Headline result slide]
[Supporting result(s) to include]
[Ablation to keep (if any)]

### Close ([n] min, 1–2 slides)
[Closing sentence]
[Pointer: paper / code / poster]

## Slide list (working titles)
1. Title
2. [slide title = claim]
...
N. Questions / thank you

## What to cut from the paper
- [item]: [reason]

## Q&A prep
- Q: [anticipated question] → A: [one-sentence answer]
```

---

## Quality bar

A well-planned talk should be reproducible: if two people built slides from this plan, they would produce talks with the same core narrative. The plan should leave no ambiguity about what the one thing is, what gets cut, and what each slide is supposed to prove.
