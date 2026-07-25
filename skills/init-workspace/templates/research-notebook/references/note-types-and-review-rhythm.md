# Note types and review rhythm

Use the lightest note that preserves a research decision or makes later synthesis possible. The notebook is an instrument for research judgment, not a second project that competes with the research.

## Capture and promotion

`agents/note-method.md` holds the general loop — capture → expand → store → query. This section is how it applies to this notebook's note types.

- Write the fragment straight into the durable note it belongs to. There is no staging folder: if the type is plainly a question, source, evidence item, or decision, create that note now.
- Capture rough. Fragments, abbreviations, and keywords beat full sentences during the session; expansion is a separate pass afterwards.
- Give a fragment its own durable note once it will affect a future choice, needs evidence, or should remain findable after the current session. Until then it can live inside a note it relates to.
- **Preserve the raw capture inside the durable note** under a `## Raw capture` heading, rather than deleting it once the prose reads well. It is the better input to any later expansion, the fallback when an expansion turns out wrong, and the record of what you actually thought before it got cleaned up.
- Do not duplicate the same prose across several folders. If the type is genuinely unclear, start it in `questions/` and reclassify once you know.

## Durable note types

- **Question:** one uncertainty that evidence or argument could resolve. State why it matters, current evidence, and what would count as an answer.
- **Idea:** a proposed hypothesis, mechanism, method direction, explanation, or proof route. State its weak point and a falsifying observation.
- **Reading:** what a source actually says, where it says it, relevant caveats, and why it enters this notebook. Do not summarize an unread source from its title or abstract alone.
- **Evidence:** an observed result, negative result, qualitative observation, or pointer to a checkable external artifact. Separate observation from reading.
- **Decision:** a consequential choice plus alternatives, rationale, accepted tradeoff, and a condition for revisiting it.
- **Meeting:** context, discussion, decisions, unresolved questions, owners, and dates. Do not turn tentative discussion into a committed decision.
- **Synthesis:** a cross-note position or map that a reader may rely on. Run the shared four-pass pipeline for substantial syntheses.

## Status discipline

- `open`: captured but not actively investigated.
- `active`: currently being investigated or used.
- `supported`: evidence currently favors the idea; not the same as proved.
- `refuted`: evidence contradicts the stated idea under its recorded scope.
- `answered`: the question has a linked answer and supporting evidence.
- `parked`: intentionally deferred, with the reason recorded.

Status changes require a short explanation and a link to the note or artifact that caused the change. Confidence records support strength, not enthusiasm.

## Weekly review

Keep the review short enough to sustain:

1. Surface durable notes not yet linked to a question or idea; link, park, or remove them.
2. Inspect active questions and ideas: identify stale items and the next decision-relevant check.
3. Link new reading and evidence to the questions or ideas they bear on.
4. Review recent decisions for triggered revisit conditions.
5. Write one `log/{YYYY}-W{NN}.md` note: what changed, what did not, what is blocked, and the next one to three priorities.

Do not report intended work as progress. A week with a refuted idea, clarified question, or documented blocker can still be a productive research week.

## Monthly synthesis

Run a longer review only when the accumulated notes justify it:

- Which questions changed status, and why?
- Which ideas gained or lost support?
- Which decisions still hold under current evidence?
- What repeated theme deserves a synthesis note?
- Which notes are merely collected and have not influenced understanding or a decision?

Create or update a file in `syntheses/` only when it connects several durable notes. Use `agents/pipeline.md` when the result is substantial enough that another reader may rely on it.
