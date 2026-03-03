# Problem 17: Collatz Peak
## Problem
For a given N, simulate the Collatz rules. Print the absolute maximum value reached during the sequence before it hit 1.

## Format
- **Input**: N
- **Output**: Max Integer
- **Constraints**: N <= 10^5

## Sample
**In:**
```text
7
```
**Out:**
```text
52
```

## Checklist before coding
- **Edge Cases Considered**: N = 1.
- **Target Complexity**: Simulation Bound O(C)

> **Hint**: `while n != 1` loop tracking `max_val`.\n