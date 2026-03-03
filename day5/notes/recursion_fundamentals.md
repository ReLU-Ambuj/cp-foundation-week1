# Recursion Fundamentals

## What is Recursion?
A function that dynamically calls *itself* from within its own body to solve a smaller sub-problem, until a mathematical certainty (the Base Case) is reached.

## The Two Mandatory Pillars
1. **The Base Case**: The rock-bottom, unquestionable truth that stops the recursion. Without it, the function calls itself infinitely until RAM explodes. (e.g., `if n <= 1: return 1`).
2. **The Recursive Step**: The mathematical logic that strictly shrinks the problem space down towards the Base Case. (e.g., `return n * factorial(n - 1)`).

## Call Stack Growth
Every time a function calls itself, it pauses execution and spawns a brand-new Memory Frame cloned above it. It waits for the clone to answer.
10 recursive calls = 10 simultaneous Memory Frames suspended in your RAM.

## Stack Overflow
If your Base Case is wrong, or your Recursive Step moves away from the Base Case (e.g., `factorial(n + 1)`), Python will generate frames infinitely. At exactly 1,000 frames, Python panic-halts and throws a `RecursionError` (Stack Overflow).

## Recursion Tree Visualization
### factorial(4)
```text
factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → 1 (Base Case reached! Returns back up the chain)
            ← 2 * 1 = 2
       ← 3 * 2 = 6
  ← 4 * 6 = 24
```

## Tail Recursion (Brief)
Tail recursion occurs when the recursive call is the absolute *last* operation the function performs, meaning no mathematical logic is left hanging in suspended frames. *Note: Python does not structurally optimize tail recursion for CP, but it is architecturally important.*\n