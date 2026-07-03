# Live model-prompting docs (volatile layer)

Model-version-specific prompting behavior changes with each release. **Do not answer from memory** — fetch the relevant page below and quote what it currently says. If a URL 404s, the docs were reorganized; search the Anthropic docs for "prompt engineering" and update this file.

## Which page to read

| You need… | Page |
| --- | --- |
| The umbrella guide: general principles, output/formatting, tool use, thinking, agentic systems, migration | Prompting best practices |
| Console tooling: prompt generator, prompt improver, templates & variables | Prompting tools |
| Opus 4.8 behavior: verbosity, effort/thinking calibration, tool-use triggering, subagents, literal instruction-following, code-review recall, frontend defaults | Prompting Claude Opus 4.8 |
| Sonnet 5 behavior deltas | Prompting Claude Sonnet 5 |
| Fable 5 behavior deltas | Prompting Claude Fable 5 |

## URLs

- Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Prompting tools (Console: generator/improver/templates) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools
- Prompting Claude Opus 4.8 — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8
- Prompting Claude Sonnet 5 — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- Prompting Claude Fable 5 — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5

## Note

These are public docs, so `WebFetch` works. For model IDs, pricing, API parameters, tool-use JSON schemas, caching, and token counting, use the `claude-api` reference instead of these pages — that material is API mechanics, not prompt design.
