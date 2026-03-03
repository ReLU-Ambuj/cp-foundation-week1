# Performance Comparison

## Measuring Execution Time
Strict time limits apply in CP.
- $O(1)$ : Arithmetic, Hash Map dict lookups.
- $O(N)$ : Single `for` loops. Usually passes $10^8$ operations per second.
- $O(N^2)$ : Nested Loops. Will usually fail (Time Limit Exceeded - TLE) if $N > 10^4$.

## Big-O vs Realistic Overhead
Sometimes an algorithm is $O(N)$, but its constant overhead is huge because you build 4 arrays and delete them constantly. An optimized $O(N)$ algorithm does the math in-place using variables.

## Micro-Optimization vs Readability
- **Micro-Optimization**: Using bitwise shifts `x >> 1` instead of `x // 2`.
- **Readability**: Using `x // 2` so your brain can instantly read it 2 hours later.
*Rule:* Choose readability unless you are specifically failing a CP Time Limit on that exact function.\n