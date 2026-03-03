# Problem 18: Anagram Pallindrome Builder
## Problem
Can the characters of String S be rearranged to form a palindrome?

## Format
- **Input**: S
- **Output**: YES / NO
- **Constraints**: Len(S) <= 10^5

## Sample
**In:**
```text
aabbc
```
**Out:**
```text
YES (abcba)
```

## Checklist before coding
- **Edge Cases Considered**: Even length vs Odd length.
- **Target Complexity**: O(N)

> **Hint**: Dict count frequencies. A palindrome can have at most ONE character with an odd frequency.\n