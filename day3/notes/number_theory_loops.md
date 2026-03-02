# Number Theory via Simulation

## Divisibility Logic
Use modulo `%` to extract remainder properties. E.g. finding factors of N involves iterating $1 \dots N$ and checking `N % i == 0`.

## Prime Detection Optimization ($O(\sqrt{N})$)
Brute forcing primality means testing 2 up to $N$.
Optimized mental model: Factors come in pairs $(A \times B = N)$. The largest value $A$ can be without overlapping $B$ is the square root of $N$.
Iterate `while i * i <= N`. This drops $1,000,000$ iterations down to $1,000$.

## GCD Euclidean Algorithm (Iterative)
Finding the Greatest Common Divisor mathematically via remainders.
```python
while b != 0:
    a, b = b, a % b
return a
```

## Digit Extraction
To parse a number digit by digit backward mathematically:
- `last_digit = N % 10`
- `N = N // 10` (Truncates the last digit)
Run this inside `while N > 0`.\n