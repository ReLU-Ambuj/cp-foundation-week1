# Problem 13: Trailing Zeros Fast
## Problem
How many trailing zeros are in N!? Do NOT compute N!.

## Format
- **Input**: Integer N
- **Output**: Integer count
- **Constraints**: N <= 10^9

## Sample
**In:**
```text
10
```
**Out:**
```text
2
```

## Checklist before coding
- **Edge Cases Considered**: N < 5.
- **Target Complexity**: O(log5 N)

> **Hint**: Count how many times 5 divides into N iteratively.\n