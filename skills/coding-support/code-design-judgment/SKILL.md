---
name: code-design-judgment
description: >-
  Judge and improve the design of code: data models, ownership, invariants,
  and special cases. Use when designing a new module or data structure, when
  implementing a feature that adds another special case, flag, or duplicated
  field, when code "keeps growing branches", or for "how should I model
  this", "is this design right", "this feels hacky", "should I add a flag",
  "is this refactor worth it", "why is this slow". Decides the representation
  before the control flow, and names the mechanism before any performance
  change. Not line-level bug
  review (code-review), an over-engineering pass (ponytail-review), root-cause
  debugging (systematic-debugging), or research experiment harnesses
  (research-codebase).
---

# Code Design Judgment

Awkward code is often an awkward representation. Look at the data model before
the control flow, and keep the answer in proportion to the problem.

## 1. Look at the data
For the state the change touches, work out what it holds, who owns it, how
long it lives, and what must always be true. Read the actual code; the
author's description is a claim to check.

Signs of strain: special cases for first, last, or empty; flags that must stay
in sync; the same fact stored twice; lifetime confused with locking.

## 2. Look for the uniform view
Could another representation make the cases one case? For example, deleting
from a singly linked list through a pointer to the incoming link (`Node **`)
removes the head-node branch. Keep cases separate if their meaning differs,
including when a "special" value carries information that callers rely on.

## 3. Decide how far to go
- **Asked to implement or fix something:** do that. If it adds to the strain,
  say so in a sentence or two and offer the redesign instead of slipping it in.
- **Bug caused by redundant state:** if the state is private, fix the
  representation, not only the symptom. If callers can see it, or you cannot
  tell, fix the bug and ask before changing the representation.
- **Asked about design:** compare keeping, patching, and redesigning by the
  complexity each leaves, not by diff size. Code that works can still be the
  wrong design. If your recommendation changes a public interface, a stored
  format, or a schema, present it as a proposal and ask for confirmation before
  writing the migration or changing callers.
- **New work:** build the smallest thing that serves the current need. Say what
  would justify more.
- **Plain bug with a sound representation:** fix it and stop.

## 4. Protect what works
Assume any change adds a bug. Name the existing behavior and callers that must
keep working, and how to check them. Ask before a change that is hard to undo,
such as a public interface, a stored format, or a schema.

For performance, name the mechanism that costs the time before changing code,
and say how far a measurement applies.

## Output
Lead with the answer or the code. Then add only what applies, in a few lines
each:
- the strain in the representation, and the redesign you offer
- what must keep working, and how to check it
- what the change costs or does not fix
- what you verified: run checks only if a tool that executes code is available
  to you; otherwise run nothing, and say the code is untested

Skip anything that has nothing to say. A small fix gets a short answer.
