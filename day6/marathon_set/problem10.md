# Problem 10: Array Duplicate Hunter
## Problem
Given N sorted integers. Count how many *unique* numbers exist. (Do not use python `set()`, solve iteratively).

## Format
- **Input**: Length N, then Array A.
- **Output**: Integer count.
- **Constraints**: N <= 10^5. A is strictly sorted.

## Sample
**In:**
```text
6\n 1 1 2 3 3 4
```
**Out:**
```text
4
```

## Checklist before coding
- **Edge Cases Considered**: N = 0.
- **Target Complexity**: O(N)

> **Hint**: Keep track of `prev_val` and increment count only when `curr != prev`.\n