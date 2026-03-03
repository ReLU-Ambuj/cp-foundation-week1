# Recursion Notes & Traps

## When Recursion Fails (RecursionError)
Stack Overflow occurs when:
1. You completely forgot to write a `return` in your basecase.
2. Your recursive step accidentally adds instead of subtracts `solve(n + 1)`.
3. The problem space is legally larger than 1,000 steps deep (Python's default physical memory limit).

## Memoization Intro (Future Topic)
To fix the $O(2^N)$ disaster of Fibonacci recursion, we use Memoization (caching). Before a recursive frame does math, it checks a global Dictionary to see if `fib(n)` was already mathematically solved by a previous branch. If yes, it returns the $O(1)$ dictionary value immediately, collapsing the entire tree.

## Debugging Strategy
Always forcefully trace the Base Case first.
Write on paper: "What does `solve(1)` return? What does `solve(2)` return?"
If `solve(2)` does not organically reach `solve(1)`, your logic is fundamentally broken.\n