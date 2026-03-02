# Loops Deep Dive: Iteration at the Machine Level

## What is Iteration?
At the CPU level, a loop does not exist as a single structural concept. It is constructed entirely of Conditional Branching (`JMP` instructions) combined with backwards memory leaps. The CPU compares a register against a limit; if the limit isn't met, it executes a `JMP` back to the memory address where the loop block began.

## Count-Controlled vs Condition-Controlled
- **Count-Controlled (`for` loops)**: You know exactly how many iterations will occur *before* the loop starts. Example: Iterating over an array of length N.
- **Condition-Controlled (`while` loops)**: Iteration count is unknown. The loop relies entirely on dynamic internal state changes to eventually hit a termination condition. Example: Simulating a game until a player dies.

## The Loop Invariant Concept
An invariant is a formalized technical promise.
If we are computing the `sum` of array `A`, our invariant is:
*"At the start of iteration `k`, `sum` holds the total of `A[0]` through `A[k-1]`."*
By strictly following loop invariants, you prevent off-by-one errors natively.

## Off-By-One Error (OBOE) Explanation
The most notorious bug in competitive programming.
Occurs due to boundary mismanagement:
- Iterating `< N` vs `<= N`
- Starting arrays at `1` instead of `0`
- Miscalculating array lengths by $N+1$ or $N-1$

## Control Flow Graph Diagram

```text
Initialization (e.g., i = 0)
      ↓
 Condition check (e.g., i < N)
   /          \ 
True         False ——> [Exit Loop]
  ↓             
Body (Execute Logic)
  ↓
Update (e.g., i += 1)
  ↓
Back to condition check
```
Every edge in this graph represents execution time. In $O(N)$ operations, the true path executes $N$ times. In an $O(N^2)$ operation, it evaluates $N \times N$ times. Keep the loop body physically minimal.
