# Reflex Training: The 5-Minute Loop Test

## Objective
To build raw, unfiltered speed in translating standard mathematical and geometric sequences into strict, deterministic Python loops.

## Instructions
1. Delete your previous code.
2. Open a blank file.
3. Start a timer for exactly **5 minutes**.
4. Attempt to recode the following 4 foundational loops entirely from memory.

### The 4 Reflex Scenarios
1. **Prime Check ($O(\\sqrt{N})$)**: Implement `is_prime(n)` using a `while` loop stopping at the square root.
2. **Fibonacci (Iterative)**: Print the first $N$ terms in $O(N)$ time with $O(1)$ space using tuple unpacking.
3. **Centered Pyramid**: Print `N` rows of a centered `*` pyramid. You must map spaces and stars mathematically.
4. **Greatest Common Divisor**: Implement the iterative Euclidean algorithm.

## Time Tracking Table
| Problem | Initial Time | Strict Constraint | Final Time | Mistake Type | 
|---------|--------------|-------------------|------------|--------------|
| Prime Check |  | 5m | | |
| Fibonacci | | 5m | | |
| Pyramid Pattern | | 5m | | |
| GCD | | 5m | | |

## Loop Mistake Classification Table
If you fail the 5-minute constraint, map your error here:
- [ ] **Off-by-One**: Tripped over `<` vs `<=`.
- [ ] **Missing State Update**: Forgot to increment `i += 1` in a while loop.
- [ ] **Inefficient Math**: Used $O(N)$ when $O(1)$ math existed.
- [ ] **Bad Variable Scope**: Shadowed an iteration variable (`for i` inside `for i`).

## Optimization Improvement Checklist
- [ ] Could I replace this `for` loop with a direct math formula?
- [ ] Is my `while` loop guaranteed to terminate on edge cases ($N=0$ or negatives)?
- [ ] Did I print inside the loop when I should have aggregated a string or list?
