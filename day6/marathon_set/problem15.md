# Problem 15: Run Length Decoder
## Problem
Given standard RLE format 'a2b3c1', reconstruct 'aabbbc'.

## Format
- **Input**: String S
- **Output**: String expanded
- **Constraints**: Len(S) <= 100

## Sample
**In:**
```text
a2b3
```
**Out:**
```text
aabbb
```

## Checklist before coding
- **Edge Cases Considered**: Multiplier could theoretically be 10 or more (e.g. a12).
- **Target Complexity**: O(Final String Length)

> **Hint**: Iterate, keeping track of current char and building a numeric multiplier dynamically.\n