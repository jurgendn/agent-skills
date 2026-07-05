---
name: python-performance-optimization
description: Profile and optimize Python performance bottlenecks. Use when Python code is slow, memory-heavy, CPU-bound, I/O-bound, latency-sensitive, or needs evidence-driven optimization rather than speculative rewrites.
---

# Python Performance Optimization

Measure first. Optimize the bottleneck that matters. Keep correctness tests
around every performance change.

For advanced patterns such as NumPy vectorization, caching, memory management,
parallelism, async I/O, database optimization, and benchmarking tools, read
`references/advanced-patterns.md`.

## Intake

Collect:
- workload and input size;
- target metric: latency, throughput, memory, CPU, I/O;
- current measurement and desired target;
- environment and hardware;
- correctness tests or golden outputs.

## Profiling Order

1. Reproduce the slow path with a realistic input.
2. Add a simple wall-clock measurement.
3. Use the right profiler:
   - `cProfile` / `py-spy` for CPU;
   - `line_profiler` for line-level hot spots;
   - `memory_profiler` / `tracemalloc` for memory;
   - application metrics for production latency.
4. Identify the smallest hot path worth changing.
5. Optimize one bottleneck.
6. Re-measure and verify correctness.

## Common Fix Classes

- Better algorithm or data structure.
- Avoid repeated work with caching.
- Batch I/O or database calls.
- Use generators/streaming for memory.
- Vectorize numerical work with NumPy/Pandas/JAX/PyTorch when appropriate.
- Move true CPU-bound parallelism to multiprocessing/native libraries.

## Rules

- Do not optimize without a baseline measurement.
- Do not trade correctness for speed silently.
- Do not optimize cold code.
- Prefer algorithmic wins over micro-optimizations.
- Record before/after numbers and input sizes.

## Output

Return:
- performance target;
- measurement method;
- bottleneck evidence;
- optimization plan ranked by expected impact;
- correctness guard;
- before/after reporting template.
