# Problem 19: Second Largest Element
## Problem
Find strictly the second largest element in a list in O(N). No sorting allowed.

## Format
- **Input**: N length. Array A.
- **Output**: Int or -1
- **Constraints**: N >= 1

## Sample
**In:**
```text
4\n 10 5 10 2
```
**Out:**
```text
5
```

## Checklist before coding
- **Edge Cases Considered**: All elements identical returns -1.
- **Target Complexity**: O(N)

> **Hint**: Track `largest` and `second_largest` simultaneously in one loop.\n