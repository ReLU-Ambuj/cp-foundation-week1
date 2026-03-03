# Problem 05: Valid IP Segment
## Problem
Given a string S. Print 'VALID' if it represents a number between 0 and 255 with no leading zeros (unless it is exactly '0').

## Format
- **Input**: String S.
- **Output**: String VALID or INVALID
- **Constraints**: S length 1 to 5.

## Sample
**In:**
```text
025
```
**Out:**
```text
INVALID
```

## Checklist before coding
- **Edge Cases Considered**: '0', '00', '256', '-1', 'abc'.
- **Target Complexity**: O(1)

> **Hint**: Length check, `isdigit()` check, then integer casting bounds.\n