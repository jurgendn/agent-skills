---
name: discussion-report-synthesizer
description: 'Synthesize a fragmented academic conversation into a cohesive, structured markdown report. Use this skill whenever the user has asked many disconnected questions about a topic in one session and now wants a unified write-up that captures what was discussed. Trigger phrases: write a report on our conversation, summarize this discussion into a document, turn this into a readable report, capture everything we talked about, make a note of this whole conversation, write up what we covered. The skill scans the full conversation, groups ideas into themes, identifies gaps, asks 2–4 targeted clarifying questions to fill them, then drafts the report. It does NOT write experimental results sections (use results-writeup), Related Work prose (use related-work-writer), or paper section drafts (use method-section-writer or abstract-and-intro-writer).'
---

# Discussion Report Synthesizer

Turn a fragmented academic conversation into a single, readable document that a person who wasn't present could understand and use.

## Use this when

- The user has explored a topic through many back-and-forth questions in one session and now wants a consolidated write-up.
- The conversation covers several related sub-topics that have never been stitched together.
- The user asks to "capture", "report", "document", or "summarize" the discussion.
- The output is a standalone markdown file, not a paper section or literature review.

## Do not use this when

- The user wants to write a section of a research paper — use `method-section-writer`, `abstract-and-intro-writer`, or `results-writeup` instead.
- The user wants a grounded literature survey — use `literature-triangulation` or `related-work-writer`.
- The conversation is about experimental logs or run results — use `results-writeup` or `experiment-trace-summarizer`.
- The conversation has only one question and one answer — a short direct reply is better than a full report.

## Workflow

### Step 1: Extract all distinct ideas from the conversation

Read the full conversation and list every distinct idea, question, claim, definition, example, and sub-topic that appeared — as a flat inventory. Do not group or synthesize yet. Flag anything stated with uncertainty or left unresolved.

What counts as distinct:
- A definition or explanation the user asked for
- A comparison or contrast drawn between concepts
- A claim asserted (by the user or by the assistant)
- An example or analogy introduced
- A question raised but not fully answered
- A tangent that led somewhere useful

### Step 2: Group into themes and identify the unifying topic

Cluster the inventory into 3–6 coherent themes. Name each theme with a short descriptive title. Then identify the overarching topic: the single sentence that explains what the whole conversation was about.

If no clear grouping emerges, structure by: (1) foundations/definitions, (2) mechanisms/how it works, (3) applications/implications, (4) open questions.

### Step 3: Surface gaps

Before drafting, identify:

- **Unresolved questions** — raised in the conversation but not settled
- **Missing context** — implied but never stated (scope, audience, domain, motivation)
- **Thin coverage** — themes that came up briefly but may deserve more depth in the report
- **Contradictions or tensions** — places where the conversation said two things that don't fully align

### Step 4: Ask clarifying questions

Ask 2–4 targeted questions to resolve the most important gaps. Wait for the user's answers before drafting.

**What to ask:**
- Intended audience for the report (expert, student, general reader, future-self)
- Whether any theme should be expanded or cut
- Missing context that would change how a section is framed (e.g., a specific domain, application, or constraint that was implied but not stated)
- Any key point the user wants emphasized that the conversation may have underweighted

**What NOT to ask:**
- "Should I write the report?" — the user already asked; just write it
- Vague preference questions ("how long should it be?") — default to a length that fits the content
- Questions whose answers you can reasonably infer from the conversation

**Format for asking:** Present the gaps as a short numbered list, not as open-ended prompts. Make it easy for the user to answer or skip.

Example:
> Before drafting, I want to clarify a few things:
> 1. Who is the intended reader — someone already familiar with [topic], or a newcomer?
> 2. The discussion touched on [X] briefly — should I expand it or treat it as a side note?
> 3. Is there a specific context (e.g., [domain]) framing this, or should the report stay general?

### Step 5: Draft the report

Once you have answers (or have made reasonable defaults), write the report using the output format below. Draw only from what was actually discussed — do not add claims, examples, or citations that did not appear in the conversation. If something is uncertain or contested, flag it explicitly.

## Output format

```markdown
# [Topic Title]

## Overview
[2–4 sentences: what this conversation explored, why it matters, and what the report covers]

## [Theme 1 Title]
[Synthesized prose covering the ideas from this theme. Each paragraph should make one clear point. Use inline emphasis for key terms the first time they appear.]

## [Theme 2 Title]
...

## [Theme N Title]
...

## Open Questions
[Bulleted list of questions raised but not resolved. Phrase each as a genuine question, not a hedge.]

## Key Takeaways
[3–5 bullet points: the most important, transferable insights from the discussion]
```

**Formatting rules:**
- Use H2 (`##`) for theme sections; avoid H3 unless a theme has genuinely distinct sub-parts.
- Keep the Overview section factual, not evaluative — describe what was discussed, not whether it was good.
- Limit Key Takeaways to what the conversation actually established, not aspirational conclusions.
- If the conversation included a worked example or comparison, preserve it in the relevant section rather than abstracting it away.

## Clarifying question guidance

The goal of clarifying questions is to resolve gaps that would force you to invent content or make a significant framing choice you cannot infer. Good questions are:

- **Specific**: "Should section 2 cover X or leave it for future work?" not "What should I include?"
- **Answerable with one sentence**: not questions that require the user to think for ten minutes
- **Consequential**: if the answer doesn't change the draft, don't ask it

If the user doesn't respond to a clarifying question or says "just write it", apply sensible defaults: general-reader audience, balanced coverage of all themes, report length proportional to conversation depth.

## Quality bar

A good report should let someone who was NOT in the original conversation:

1. Understand what topic was explored and why it matters
2. Follow each theme without needing to read the original conversation
3. Know which questions remain open and why
4. Walk away with 3–5 actionable or memorable insights

If the report requires reading the original conversation to make sense of a section, that section needs more context or should be cut.

## Failure modes to avoid

- **Transcript mimicry**: Do not restate the conversation as Q&A. Synthesize into prose that reads as a document, not a chat log.
- **Over-hedging**: "The conversation seemed to suggest that perhaps X might be the case" — if the conversation said X, say X. If it was tentative, say "tentatively" once and move on.
- **Invented content**: Do not add facts, citations, or examples that did not appear in the conversation, even if they are accurate. Mark any inference explicitly ("this implies..." or "one natural extension is...").
- **Flat structure**: A list of bullet points for every section is not a report. Aim for synthesized paragraphs with clear logical flow.
- **Missing open questions**: Unresolved questions are often the most valuable part. Do not bury or skip them.
