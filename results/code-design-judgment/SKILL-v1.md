---
name: code-design-judgment
description: >-
  Judge and improve the design of code: data models, ownership, invariants,
  and special cases. Use when designing a new module or data structure, when
  a change adds another special case, flag, or duplicated field, when code
  "keeps growing branches", or for "how should I model this", "is this design
  right", "this feels hacky", "should I add a flag", "is this refactor worth
  it", "why is this slow". Decides the representation before the control flow,
  and names the mechanism before any performance change. Not line-level bug
  review (code-review), an over-engineering pass (ponytail-review), root-cause
  debugging (systematic-debugging), or research experiment harnesses
  (research-codebase).
---

# Code Design Judgment

Awkward code is often an awkward representation. Fix the data model before
the control flow.

## 1. State the data
For each piece of state the design touches, state what it holds, who owns it,
how long it lives, and what must always be true. Read the actual code; the
author's description is a claim to check. If you cannot state an invariant,
that gap is the first finding.

## 2. Find the strain
Look for:
- special cases for first, last, or empty
- flags that must stay in sync
- the same fact stored twice
- branches that do one operation in different ways
- lifetime confused with locking or ownership

## 3. Look for the uniform view
Ask what all the cases have in common, and whether another representation
would make them one case. For example, deleting from a singly linked list
through a pointer to the incoming link (`Node **link`) treats the head and
every later node the same way, so the head-node branch disappears.

Keep the cases separate if their meaning differs. Similar-looking code is not
necessarily the same operation.

## 4. Compare designs
Compare the current design, the proposed patch, and the redesign on:
- resulting complexity, not diff size
- which invariants each one keeps
- what breaks for callers

Code that works can still be the wrong design. Judge how it solves the
problem, not only whether the tests pass.

Assume any change adds a bug. Name what already works and must keep working,
and the check that would show it still does.

Ask before a redesign widens the task or changes a public interface, a stored
format, or a schema. Those are hard to undo.

## 5. Start small
For new work, build one end-to-end path on the core data model before adding
features or extension points. Every abstraction must serve a current need.

## 6. Performance: mechanism first
Before changing code for speed, name the mechanism that costs the time, for
example contention on shared state, cache misses, allocation, I/O, or the
algorithm. Change that mechanism only. Report what you measured, under what
workload, and how far the result applies. A synthetic benchmark isolates a
mechanism; it does not predict real-workload speedups. A faster design must
keep the invariants from step 1.

## Output
- **Data model:** state, owner, lifetime, invariants
- **Strain:** what you found, or "none found" plus where you looked
- **Recommendation:** keep, patch, or redesign, with the reason
- **Must keep working:** behavior that must keep working, and how to check it
- **Costs:** what the recommendation costs and what it does not fix
- **Performance:** if relevant, the mechanism, the measurement, and its scope
- **Verification:** what was checked by reading and what by running, as two
  separate lists
