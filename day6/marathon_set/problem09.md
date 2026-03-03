# Problem 09: Hollow Triangle
## Problem
Print a right angle hollow triangle of size N using '*'. Space padded.

## Format
- **Input**: Integer N
- **Output**: Pattern.
- **Constraints**: N >= 3

## Sample
**In:**
```text
4
```
**Out:**
```text
*\n* *\n*   *\n* * * *
```

## Checklist before coding
- **Edge Cases Considered**: N = 3.
- **Target Complexity**: O(N^2)

> **Hint**: Boundary check logic in nested loop: `c==0` or `r==N-1` or `r==c`.\n