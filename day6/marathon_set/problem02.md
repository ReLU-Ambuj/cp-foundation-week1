# Problem 02: Character Type Divider
## Problem
Given a single character C. Print 'VOWEL' if it is a vowel, 'CONSONANT' if it is a consonant, and 'OTHER' if it is a digit or symbol.

## Format
- **Input**: A single character C.
- **Output**: String representing type.
- **Constraints**: C is a valid ASCII character.

## Sample
**In:**
```text
E
```
**Out:**
```text
VOWEL
```

## Checklist before coding
- **Edge Cases Considered**: Uppercase vs lowercase vowels, numbers, whitespace.
- **Target Complexity**: O(1)

> **Hint**: Normalize to lowercase immediately. `c.isalpha()`.\n