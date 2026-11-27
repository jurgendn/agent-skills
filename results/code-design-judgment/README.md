# code-design-judgment evals, 2026-11-27

Setup: `claude -p --safe-mode --tools ""`, Sonnet 5.5 answering and grading (grader blind to arm), SKILL.md body appended to the system prompt, 12 evals x 5 runs per arm. v1 is `SKILL-v1.md`; v2 is the measured revision, which is not saved separately. The skill now in `skills/coding-support/code-design-judgment/` is v3 (see the end of this file).

| Iteration 2, non-format assertions | v1 | v2 | no skill |
|---|---|---|---|
| Valid answers only | 168/178 (94.4%) | 179/195 (91.8%) | 165/193 (85.5%) |
| Invalid answers counted as fail | 168/215 (78.1%) | 179/215 (83.3%) | 165/215 (76.7%) |
| Valid only, without evals 8 and 11 | 150/156 (96.2%) | 160/176 (90.9%) | 151/176 (85.8%) |
| Invalid answers (fake tool calls) | 10/60 | 5/60 | 6/60 |
| Mean output tokens | 1529 | 895 | 742 |

v1 vs v2, valid only: v2 lost eval 2 "ask before schema change" (4/5 to 1/5), "name invalid combinations" (2/5 to 0/5), and eval 10 "remove redundant state or state the invariant" (4/4 to 0/5).

Caveats:
- Eval 11 is contaminated: v2 gained a line that matches its trap.
- Eval 8 refers to code it does not include, which invites tool calls; fix the prompt before reuse.
- Evals 10 and 12 were not run before v2 was written, but their text was known to the author.
- Fake tool calls, excluding eval 8: v1 9/55 (plus 5/30 in the dev pass), v2 1/55, no skill 3/55 (plus 0/30). v1's "checked by running" wording pushed the model to try to run code; v2's rewording brought it back to baseline levels. The first detector missed several formats.
- "Valid only" is a selected subset and favours v1, which broke mostly on harder cases. "Counted as fail" over-penalizes v1, since with real tools it would simply run the check. The truth lies between the two rows.
- Some cells rest on two valid runs or fewer: v1 on evals 5 and 11 (and v2 and no skill on eval 8).
- Evals 6 and 12 reward offering a redesign, while eval 10 rewards removing the redundant state; v2's eval 10 "loss" partly reflects that conflict.
- Skill was forced on; description triggering is untested.
- Baseline already passes evals 1, 3, 4, 6, 7, 9 at or near 100%.

## v3 (current)

v2 plus two rules: ask before a public interface, stored format, or schema change on design questions; for a bug caused by redundant state, fix private state and ask first if callers can see it. **Not evaluated.**
