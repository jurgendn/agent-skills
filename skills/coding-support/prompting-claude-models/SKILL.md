---
name: prompting-claude-models
description: >-
  Design prompts, system prompts, and agent scaffolding for LLM-backed features built on Claude models — LLM-as-judge and evaluation harnesses, RAG over literature or documents, extraction/classification pipelines, and multi-step or subagent agents. Use whenever the user is writing or debugging a prompt for a Claude model: "improve this system prompt", "my LLM judge is inconsistent", "Claude ignores my instructions / over-triggers a tool / is too verbose", "how do I structure this prompt", "why won't Claude use my tool", "tune effort/thinking for this agent", or turning a research workflow into an LLM call. This is prompt *design* craft; for API/SDK mechanics (model IDs, pricing, parameters, tool-use schemas, caching, token counting) use the claude-api reference instead, and for Python code quality use the python-* skills. Model-version-specific behavior changes often, so this skill grounds those claims in the live Anthropic docs rather than reciting them from memory.
---

# Prompting Claude Models

Prompts are the interface to an LLM the way an API signature is the interface to a function — most "the model is wrong" bugs are really underspecified-prompt bugs. This skill covers the durable craft of writing prompts for Claude models in research and coding work, and points you at the live docs for the parts that change with each model release.

## When to use this skill

- Writing or revising a system prompt or task prompt for a Claude-backed feature
- Building an LLM-as-judge / evaluation rubric, a RAG answer prompt, or an extraction/classification prompt
- Designing tool definitions or agent scaffolding (when to call tools, when to spawn subagents, how to report progress)
- Debugging behavior: ignored instructions, over/under-triggered tools, wrong verbosity, refusals, inconsistent judgments
- Calibrating effort / thinking depth for an agent or pipeline

## When not to use it

- **API/SDK mechanics** (model IDs, pricing, sampling parameters, tool-use JSON schema, prompt caching, token counting, migration) → use the `claude-api` reference. This skill is about *what the prompt says*, not how the call is wired.

## Ground model-specific behavior in the live docs

Behavior that depends on the model version — default verbosity, effort levels and defaults, thinking triggers, tool-use tendencies, subagent spawning, frontend house style — **shifts with each release and goes stale fast**. Do not recite it from memory or freeze it into a prompt. When a task turns on one of these, read the relevant page first and quote what it currently says.

The live pages are catalogued in `references/live-model-docs.md` — read that file to get the URLs and pick the right page, then fetch it. Treat this SKILL.md as the *durable* layer and those docs as the *volatile* layer.

## Durable techniques

These hold across model versions. Prefer them before reaching for model-specific tuning.

### 1. Structure the prompt with XML tags

Wrap distinct components — instructions, context, retrieved documents, examples, the input to act on — in named tags (`<document>`, `<rubric>`, `<transcript>`). Tags give the model unambiguous boundaries, let you refer back to a section by name ("using the criteria in `<rubric>`"), and make the prompt far easier to template and diff. This matters most in RAG and evaluation prompts where fixed instructions and injected content sit side by side and would otherwise blur together.

### 2. Be explicit and literal; state the scope

Modern Claude models follow instructions literally rather than inferring what you probably meant — a feature for pipelines, a trap for the underspecified. If an instruction should apply broadly, say so: "apply this to *every* section, not just the first." If you want a specific output shape, show the exact template. Ambiguity the model used to paper over will now surface as literal, narrow compliance.

### 3. Show the target, don't just forbid the miss

Positive examples of the behavior you want beat negative "don't do X" instructions. To reduce over-explaining, show one concise exemplar rather than writing "don't be verbose." To fix a bad judgment pattern, add a worked example of the correct reasoning. Reserve prose rules for things you can't easily demonstrate.

### 4. Ask for reasoning before the answer, when accuracy matters

For classification, evaluation, and multi-step reasoning, have the model work through the problem before committing — list key features, compare against criteria, then decide. Put the reasoning in a tagged block (`<analysis>`) and the verdict after it. This trades latency and tokens for accuracy, so use it where correctness dominates and skip it on cheap high-volume lookups. Extended/adaptive thinking is the built-in version of the same idea; see the live docs for how the current model triggers it.

### 5. Separate fixed content from variable content

In any prompt you'll call more than once, split the static instructions from the per-call inputs (user text, retrieved chunks, prior tool results) and slot the variable parts into named placeholders. This is what makes a prompt testable (swap only the input), versionable (diff only the instructions), and safe against injection (the model knows which region is untrusted data, not instructions).

### 6. Make tool use turn on the tool description

Whether the model calls a tool is driven mostly by the tool's name and description, not by pleading in the system prompt. If a tool is under-used, sharpen its description — say *when* and *why* to reach for it and what it returns. If it fires too eagerly, narrow the description. Only after the description is right should you add system-prompt guidance, and prefer concrete triggers ("when the user asks about X, call Y") over vague encouragement.

### 7. In multi-step / agent prompts, separate coverage from filtering

When one stage both finds candidates and decides which are worth reporting, a literal-minded model may investigate thoroughly and then silently drop items it judges below your stated bar — so a "only report important issues" instruction can *lower* recall even as quality rises. Fix it by splitting the jobs: tell the finding stage its goal is coverage (surface everything, attach a confidence and severity), and let a separate ranking/verification stage filter. If you must filter in one pass, define the bar concretely (what counts as reportable) instead of qualitative words like "important." The same coverage-vs-filter split applies to any generate-then-prune agent, not just code review.

### 8. Calibrate autonomy, tool budget, and progress cadence for agents

For a multi-step agent, three dials shape behavior as much as the task instructions, and all three are set in the prompt:

- **Autonomy / stop condition.** State explicitly whether the agent should ask before acting or proceed on reasonable assumptions, and how far to carry a task before yielding. "Make reasonable assumptions and finish the task end-to-end this turn; stop to ask only when a choice is genuinely irreversible or unrecoverable" yields very different behavior from "confirm each step." Under-specifying this is the usual cause of an agent that either stalls for permission or over-reaches. Front-load the task, intent, and constraints in the first turn so it can run without round-trips.
- **Tool-call efficiency.** Tell the agent to prefer a dedicated tool over a shell equivalent when one exists, to decide which files and resources it needs *before* it starts calling, and to batch independent reads/calls in parallel rather than one at a time. This cuts latency and wasted turns.
- **Progress-update cadence.** If the agent narrates a long trajectory, specify the shape and rhythm you want — e.g. a one-line acknowledgment plus a short plan before a batch of tool calls, every few steps — rather than leaving it to emit a running log or go silent for minutes.

The version-specific defaults here — how strictly the model honors effort, how readily it volunteers updates, how eagerly it spawns subagents — shift by model; read the live docs before tuning and measure the effect on your own runs.

### 9. Control verbosity and effort deliberately

If output length or effort matters to your product, set it explicitly — a concise-output instruction with a short positive example, and the effort/thinking level appropriate to the task (higher for hard reasoning and agentic coding, lower for scoped latency-sensitive calls). The exact effort levels, defaults, and how strictly the current model honors them live in the model-specific docs; read them before tuning, then measure the effect of any change on your own evals rather than trusting a single anecdote.

### 10. Specify the outcome and constraints, not a rigid procedure

The most reliable prompts describe the *target* — what "done" looks like, the success criteria, the hard constraints, and the context available — and let the model find the path, rather than scripting every step. Long process stacks tend to *reduce* quality: they crowd out the goal and invite literal, box-checking compliance. This is complementary to being explicit (technique 2): be precise about the *destination and boundaries*, not about each move. For genuine judgment calls, prefer a decision rule ("if two sources conflict, surface both and attribute each") over an absolute ALWAYS/NEVER, which the model can only follow blindly.

### 11. Give the output a contract and a verification step

When output shape matters — structured extraction, an eval verdict, a multi-part answer — state the contract: exactly which sections or fields, in what order, and what "complete" means. Then have the model check its own work before finalizing: is every requested item covered, is each claim grounded, does the format match? Treat the task as unfinished until the whole contract is met, and tell it to mark any item it couldn't complete and say what's missing rather than quietly dropping it or padding to fill space. On an empty or partial tool result, one or two fallback strategies before concluding "nothing found" beats stopping at the first dead end.

### 12. Demand grounded, honestly-attributed output

For RAG, LLM-as-judge, and any research prompt where the answer must trace to evidence: instruct the model to base claims only on the retrieved context or tool results in front of it, attach each citation to the specific claim it supports (not a trailing bibliography), and never invent a citation, URL, or identifier. Have it label what is directly supported versus inferred, and when sources conflict, surface and attribute each side instead of blending them into a false consensus. This is prompt-level defense against the failure the `citation-auditor` skill catches after the fact — cheaper to prevent in the prompt than to repair in the draft.

## Workflow for a prompt task

1. **Name the failure precisely.** "Too verbose", "ignores instruction Z", "judge disagrees with itself across runs", "won't call the search tool." A vague complaint yields a vague fix.
2. **Reach for a durable technique first** (the list above). Most issues are structure, explicitness, or examples — not the model version.
3. **If it's genuinely model-behavioral** (effort, thinking, tool-triggering, verbosity defaults, subagents), read the right page in `references/live-model-docs.md` and apply what it currently prescribes.
4. **Change one thing and measure.** Prompt edits interact; validate against a handful of real cases or an eval set, not one example, before declaring it fixed.
