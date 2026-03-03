# Problem 12: Substring Occurrences
## Problem
Count overlapping occurrences of substring B in A.

## Format
- **Input**: String A, String B
- **Output**: Integer count
- **Constraints**: len(A) <= 10^4

## Sample
**In:**
```text
aaaa aa
```
**Out:**
```text
3
```

## Checklist before coding
- **Edge Cases Considered**: B larger than A.
- **Target Complexity**: O(N*M)

> **Hint**: Loop `len(A) - len(B) + 1` and slice.\n