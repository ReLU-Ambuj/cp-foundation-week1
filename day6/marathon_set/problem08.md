# Problem 08: Alternating Binary
## Problem
Print 'YES' if a binary string alternates perfectly ('10101' or '01010').

## Format
- **Input**: String S.
- **Output**: YES / NO
- **Constraints**: Length <= 10^5

## Sample
**In:**
```text
10101
```
**Out:**
```text
YES
```

## Checklist before coding
- **Edge Cases Considered**: Length 1 is always YES.
- **Target Complexity**: O(N)

> **Hint**: Loop comparing `s[i] == s[i-1]`.\n