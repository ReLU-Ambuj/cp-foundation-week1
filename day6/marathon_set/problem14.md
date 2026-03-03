# Problem 14: Matrix Border Sum
## Problem
Given an N x M matrix, calculate the sum of strictly the outer border elements.

## Format
- **Input**: N, M. Then matrix.
- **Output**: Integer sum.
- **Constraints**: N, M <= 100

## Sample
**In:**
```text
3 3\n1 2 3\n4 5 6\n7 8 9
```
**Out:**
```text
40 (1+2+3+6+9+8+7+4)
```

## Checklist before coding
- **Edge Cases Considered**: 1x1 matrix, 1xM matrix.
- **Target Complexity**: O(N*M)

> **Hint**: If `r==0` or `r==N-1` or `c==0` or `c==M-1`, add to sum.\n