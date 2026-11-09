# Teaching philosophy

How every study book is written, in any mode and for any subject. `SKILL.md` implements it; this file is the reason behind that structure. Read it before writing the first Part.

## The goal

The reader must be able to **explain and rebuild**, not recite. A second question ("why?", "what if the assumption fails?", "how does this connect to X?") breaks a memorised formula but not an understood one, whether the question comes from an examiner, a colleague, or a bug. So a note is judged by one test: *could the reader reconstruct this from the story if they forgot the formula, and say it aloud in a minute?* Understanding is shown, not felt: the reader can predict a fresh small case, tell the idea apart from its nearest alternative, and say where it stops applying.

## Principles

1. **Motivation before mechanics.** Every idea enters as the answer to a limitation of the previous idea. State the problem, the obvious approach, where it fails, and only then the new idea. A definition that appears without its reason is a fact to memorise; one that appears as the fix for a visible failure is something the reader can rediscover.

2. **Story, statement, example, connection, in that order.**
   - *Story*: why the topic exists and how its pieces fit together (intuition, plain words).
   - *Statement*: the exact definition, theorem, or interface (rigour second).
   - *Example*: small numbers, doable by hand, checked.
   - *Connection*: the same idea in another Part, in the reader's own work, or in something the reader already knows.
   The order is also the order of a good spoken answer.

3. **One idea per Part, one turn per story.** Each Part has a single principle everything grows from ("find the basis where the map is simple", "study the rules once and apply them to every object", "let every token decide what to read"). Each story has one *turn*: the limit, and the idea it forces. If the reader can name the turn, the rest can be derived.

4. **Connections are the content.** The same few ideas return under different names (fixed points, eigenvalues, orthogonality, conditioning, averaging, random walks). Name the recurrence every time it happens. Seeing it is the sign of maturity, and it gives the reader a bridge whenever a question lands on a weak area.

5. **Intuition and rigour are both required, never one instead of the other.** Intuition tells the reader what to say first; the precise statement is what survives a follow-up. Skipping either produces a blog post or an equation dump. Every equation earns its place by answering a named question (what is optimised, bounded, approximated, or traded off), and every central idea is shown where it breaks: its failure modes and the trade-off it cannot avoid.

6. **Show the decision, not only the knowledge.** For each Part, say *which question to ask* and *which tool it selects* (framework tables). Knowing a method is less useful than knowing when to use it and when it fails.

7. **Retrieval over rereading.** Notes are built to be practised: cover the right-hand column and retell the seven stages; redraw the concept graph from memory; say the core idea in 60 seconds; explain one example aloud. A Part is done when the reader can do this *without help*, not when the pages have been read.

8. **Honesty about gaps.** Never present a thin understanding as a strong one. In exam mode, weak grades get more worked examples and likely questions, and missing topics are listed as gaps with why the programme expects them and how to say truthfully where the reader met them: one honest sentence of context, then demonstrate the knowledge now. In every mode, content not backed by a source is marked as such.

9. **Depth where it will be probed.** In exam mode, strong grades are asked for depth (proof ideas, edge cases, failure modes) and weak grades for fluency (basics done correctly and fast). In learning modes, depth goes to the load-bearing ideas the reader will build on, fluency to the rest. Spend the page budget accordingly.

10. **Every claim checked.** Recompute each worked example. Take facts about the reader's own work only from their documents, and facts about a framework or model only from its paper, official docs, or source at a named version. A wrong example in a study note is worse than none, because the reader will trust it.

## Voice

- A mentor talking to one graduate student: direct ("your thesis", "say this aloud"), calm, no hype.
- Plain English, short sentences, no filler. Prefer the concrete word to the abstract one.
- Explain *why* before *what*. Avoid rules stated without reasons.
- Use analogies only when they are accurate (a clock forgets the full hours and keeps the time of day; a quotient forgets what the map cannot tell apart).
- Mathematics in full, in proper notation, after the intuition has been given.

## Checklist before a Part is finished

- [ ] Does each topic open with *why it exists*, before any definition?
- [ ] Is the turn (limit → idea) stated in one sentence for each story, with the extra assumption named if the limit only motivates the idea?
- [ ] Does each central idea say where it breaks and what trade-off it cannot avoid?
- [ ] Is there a worked example with small numbers, and was it recomputed?
- [ ] Does at least one link point to another Part, the reader's own work, or their prior knowledge?
- [ ] Could the reader say the core idea in about 60 seconds without notes, then predict a fresh case, separate it from its nearest alternative, and say where it stops applying?
- [ ] Are weak areas treated honestly and load-bearing areas given depth?
- [ ] Is every unsourced section marked, and does every `@label` resolve (the build fails otherwise)?
