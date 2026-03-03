# Recursion vs Iteration

## Performance Comparison
- **Iteration (Loops)**: Fast. Requires $O(1)$ Extra Space (just updating a pointer or integer).
- **Recursion**: Slower. Requires $O(N)$ Extra Space on the Call Stack for every recursive frame suspended. Function calls have computational overhead.

## When Iteration is Safer
Strictly mathematically bounded sequences: Factorial, Fibonacci, Array summation, Pattern printing. You should almost never use recursion for standard 1D math in Python.

## When Recursion is Appropriate
Navigating non-linear, unpredictable spaces: Trees, Graphs, Depth First Search (DFS), Backtracking algorithms (generating permutations), and Divide-and-Conquer (Merge Sort).

## The Fibonacci Truth
**Iterative Fibonacci (Loop)**:
- Time: $O(N)$
- Space: $O(1)$

**Naive Recursive Fibonacci `fib(n-1) + fib(n-2)`**:
- Time: $O(2^N)$ (Catastrophic Exponential explosion as identical branches are evaluated thousands of times).
- Space: $O(N)$ Max depth of the stack tree.\n