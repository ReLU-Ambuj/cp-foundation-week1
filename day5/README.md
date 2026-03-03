# Day 5: Functions, Modular Thinking, and Recursion Intro

## Day Objective
To transition from "script-kiddie" logic (where everything runs chronologically from top to bottom) to **Structured Problem Decomposition**. You will learn to construct encapsulated, heavily decoupled "Pure Functions" that map inputs directly to outputs with zero unintended side effects.

## Why Modular Thinking Matters
In Competitive Programming, monolithic scripts of 100+ lines are impossible to debug under pressure. If a bug occurs in a 30-line script parsing a matrix, it's hard to find. If that logic is separated into a 5-line `parse_row()` helper function, testing and isolating the point of failure becomes instant.

## Script vs Function-Based Design
- **Script**: Takes `input()`, processes a massive block of `for`/`while` loops, modifies global arrays, and immediately `print()`s the result.
- **Function**: Takes arguments `(matrix, target)`, executes isolated logic within its own namespace, and `return`s the exact mathematical state to the caller.

## Hour-by-Hour Execution Plan
- **Hour 0–2**: Theory (Call Stack, Scope Rules, LEGB, Recursion Trees)
- **Hour 2–5**: Refactoring Old Drills (`is_prime.py` to `average_function.py`)
- **Hour 5–8**: Advanced Function-Based Problems (`problem1.md` onwards)
- **Hour 8–11**: Designing clean helper functions
- **Hour 11–13**: Introduction to Recursion (Base cases and stack tracing)
- **Hour 13–15**: Manual Recursion Unrolling & Debugging

## Strict Rule: No Global Variables allowed
If a variable is not passed into the function as a parameter, or declared explicitly inside the function, **you cannot use it**. Eliminating globals forces you to structurally design data flow.

## Commit Strategy
Commit to `git` after every **3 refactored files**. Your message must highlight the extracted function (e.g., `refactor: extract gcd logic into pure function`).

## Clean Code Expectations
1. Use type hints (`def solve(n: int) -> int:`).
2. Early return / Guard clauses heavily enforced.
3. No nested monolithic loops if a helper function can abstract it.
