# Debugging Toolbox

Use this reference when the main debugging process needs concrete tools.

## Binary Search Debugging

- Use `git bisect` for regressions across commits.
- Use feature flags or config toggles for behavior differences.
- Bisect input size, data slices, or request fields when the bug is data-shaped.

## Differential Debugging

Compare a good run and a bad run:
- commit;
- config/env vars;
- dependency versions;
- input data;
- command flags;
- hardware/runtime;
- logs and metrics.

The useful question is not "what changed?" but "which difference can explain the
observed symptom?"

## Trace Debugging

Add structured logs at boundaries:
- request/input received;
- normalized/preprocessed data;
- branch decisions;
- external calls;
- output before serialization.

Remove or downgrade noisy logs after the fix.

## Python Tools

- `breakpoint()` / `pdb` for local stepping.
- `pytest -k <name> -vv` for focused repro.
- `pytest --maxfail=1 -x` to stop at first failure.
- `python -m cProfile` for CPU profiling.
- `tracemalloc`, `memory_profiler`, or `objgraph` for memory leaks.

## JavaScript / TypeScript Tools

- Browser DevTools for frontend state, network, layout, and performance.
- Node inspector: `node --inspect-brk`.
- `console.trace()` for unexpected call paths.
- Source maps for minified production traces.

## Production Bugs

Prefer observability over speculation:
- correlate logs, traces, metrics, and deploy times;
- reproduce on a staging copy when possible;
- avoid live-data mutation while diagnosing;
- rollback when impact is high and cause is unclear.

## Common Mistakes

- Fixing before reproducing.
- Treating stack trace location as root cause.
- Changing several variables at once.
- Ignoring intermittent failures as "just flaky."
- Deleting evidence once the symptom disappears.
