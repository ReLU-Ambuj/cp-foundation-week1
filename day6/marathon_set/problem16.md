# Problem 16: Two Divisors Max
## Problem
Given A and B. Find the number in range [A, B] with the absolute maximum number of divisors.

## Format
- **Input**: A, B
- **Output**: Integer number
- **Constraints**: A <= B <= 10^3

## Sample
**In:**
```text
1 10
```
**Out:**
```text
6
```

## Checklist before coding
- **Edge Cases Considered**: Tied divisor counts.
- **Target Complexity**: O(N * sqrt N)

> **Hint**: Write a pure helper `count_divs(n)`.\n