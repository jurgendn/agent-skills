---
name: python-design-patterns
description: Guide Python design patterns, refactoring, and architecture decisions. Use when deciding whether to add an abstraction, splitting tangled code, choosing composition vs inheritance, reducing coupling, or making Python code easier to test and change.
---

# Python Design Patterns

Design for the next real change, not for imagined future flexibility. Simpler
code wins until complexity earns its keep.

For concrete before/after examples, read `references/pattern-catalog.md`.

## Decision Principles

- **KISS:** choose the simplest design that satisfies current requirements.
- **Single responsibility:** one reason to change per function/class/module.
- **Composition over inheritance:** combine behavior explicitly before building
  fragile hierarchies.
- **Rule of three:** do not abstract two similar cases until a third proves the
  pattern is real.
- **Dependency direction:** business logic should not depend on framework glue.

## Refactoring Workflow

1. Identify the pain: duplication, coupling, long function, unclear ownership,
   difficult testing, or repeated bug pattern.
2. Name the change the design must support.
3. Find the smallest boundary that reduces the pain.
4. Prefer extracting pure functions before classes.
5. Add an abstraction only if it removes real duplication or isolates volatility.
6. Keep tests around behavior before moving code.

## Common Moves

- Extract function for a coherent transformation.
- Extract module when related functions change together.
- Introduce a protocol/interface when multiple implementations are already real.
- Pass dependencies as parameters for testability.
- Use a repository/service boundary only when persistence or business logic is
  actually tangled.

## Avoid

- Factories, registries, and plugins before there are multiple real variants.
- Base classes with one subclass.
- Global mutable state.
- Framework models leaking into public API schemas.
- "Clean architecture" layers that only forward calls.

## Output

Return:
- current design smell;
- concrete pressure causing it;
- smallest refactor;
- abstractions to avoid for now;
- test impact;
- before/after ownership boundary.
