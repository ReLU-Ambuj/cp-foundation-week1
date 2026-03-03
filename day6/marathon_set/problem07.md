# Problem 07: Harmonic Frequency
## Problem
Given string S. Which character appears with exact frequency F? If none, print '-1'. (Assume only one valid answer).

## Format
- **Input**: String S and Integer F.
- **Output**: Character or -1.
- **Constraints**: len(S) <= 10^5

## Sample
**In:**
```text
hello 2
```
**Out:**
```text
l
```

## Checklist before coding
- **Edge Cases Considered**: F > len(S).
- **Target Complexity**: O(N)

> **Hint**: One pass dictionary build. One pass dictionary scan.\n