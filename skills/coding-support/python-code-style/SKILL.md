---
name: python-code-style
description: Guide Python style, linting, formatting, naming, type annotations, and documentation conventions. Use when writing or reviewing Python code, configuring Ruff/mypy/pyright, writing docstrings, or establishing project standards.
---

# Python Code Style

Use tools for mechanical style and human judgment for names, boundaries, and
documentation. The goal is readable code that is easy to review and maintain.

For concrete config and docstring templates, read `references/style-configs.md`.

## Defaults

- Use `ruff` for linting/import sorting/formatting unless the project already has
  a different standard.
- Use type hints for public APIs and non-obvious internal boundaries.
- Prefer clear names over abbreviations.
- Keep imports grouped: standard library, third-party, local.
- Let the formatter decide line wrapping.

## Review Checklist

Check:
- names describe domain meaning;
- functions have one clear job;
- public functions/classes have type annotations;
- docstrings explain behavior, inputs, outputs, and important side effects;
- errors are explicit and useful;
- imports are organized;
- dead code and commented-out code are removed.

## Naming

- Functions/variables: `snake_case`.
- Classes: `PascalCase`.
- Constants: `SCREAMING_SNAKE_CASE`.
- Private helpers: leading underscore only when truly internal.
- Avoid one-letter names except tight mathematical/local contexts.

## Documentation

Document why and contract, not every line. Add docstrings for public APIs,
complex transformations, and anything future readers may misuse.

## Output

Return:
- style/config recommendations;
- naming issues;
- typing/docstring gaps;
- risky readability issues;
- minimal patch plan.
