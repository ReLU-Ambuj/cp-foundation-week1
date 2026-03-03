# Problem 04: The Reversed Modulo
## Problem
Given N. Reverse its digits algebraically (do not cast to string), then print N mod 5.

## Format
- **Input**: Integer N.
- **Output**: Integer result.
- **Constraints**: 1 <= N <= 10^7

## Sample
**In:**
```text
123
```
**Out:**
```text
1
```

## Checklist before coding
- **Edge Cases Considered**: N ending in 0 (e.g. 500 becomes 5).
- **Target Complexity**: O(log10 N) loop over digits.

> **Hint**: Standard `rev = rev * 10 + n % 10` while loop.\n