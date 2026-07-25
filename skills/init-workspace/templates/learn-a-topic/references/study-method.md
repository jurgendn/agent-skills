# Study method (reference)

How to use this vault so reading turns into understanding. These are the methods the agent should encourage and apply; for explaining a specific hard concept, route to `professor-mentor-technical-teaching`.

## Active over passive

- **Re-derivation** — after reading a result, close the source and reconstruct it. Gaps you hit are exactly what to study. Capture them in `open-questions.md`.
- **Feynman test** — explain the concept in plain language in `summaries/`. If you can't, you don't understand it yet.
- **Self-testing** — write questions in `exercises/` and answer them later without notes; retrieval beats re-reading.
- **Uncertainty marking** — after each note, write what you are confident about, what you are guessing, and what evidence would change your mind. Confidence is a control signal for what to revisit, not a performance score.

## Spacing and connection

- **Spaced revisit** — come back to `confidence: low` sources after a few days; the dashboard surfaces them.
- **Interleave** — alternate subtopics rather than finishing one in isolation; connections live at the boundaries.
- **Map as you go** — keep `summaries/map.md` current; a concept you can't place on the map isn't integrated yet.

## Depth control

- **Breadth first, then depth.** Get the landscape (`literature-triangulation`) before deep-diving one source. Don't rabbit-hole early.
- **One canonical source per subtopic** to anchor, then triangulate with others.
- When a single object deserves mastery (a key paper/proof/method), switch to a depth-first pass — that's what `flow-deep-understanding` is for.

## Documentation discipline

- **The system exists to enable research, not replace it.** Keep notes low-effort and close to the work. A wiki/vault is succeeding when it makes sources, experiments, questions, and results easier to retrieve and synthesize; it is failing when maintaining the system becomes the main activity.
- **One useful page beats a perfect taxonomy.** Add structure only when a real retrieval or synthesis problem appears.
- **Capture links between papers, datasets, experiments, and results.** Those links are the main payoff of wiki-style research management.

## AI-assisted learning discipline

`agents/note-method.md` holds the mechanics of the capture → expand → store → query loop. This section is the learning discipline that constrains it.

- **Use AI to expose gaps, not to outsource understanding.** Good uses: ask for questions, counterexamples, alternative explanations, and checks of your own summary. Weak uses: accepting a generated synthesis before reading the source.
- **Keep the human load-bearing step.** Before trusting an AI explanation, close it and write the idea yourself, derive the key step, or solve a small exercise. This is why the loop's expand pass ends in *your* review and edit: LLM expansion is measured to save effort, but whether it preserves the encoding benefit of writing it yourself has never been tested.
- **Querying the vault is not retrieval practice.** Asking an agent to find and synthesize across your notes delegates the retrieval, and with it the learning benefit. Query to locate what to re-derive; then close the answer and reconstruct it yourself.
- **Log AI-suggested sources in `search-log.md`.** Treat them as candidates until primary sources support the claims.

## Signals you actually understand it

- You can re-derive the key result.
- You can state what it assumes and where it breaks.
- You can explain it to someone else without the source open.
- You have specific open questions, not vague unease.
