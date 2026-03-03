# Refactoring & Code Quality Checklist

## Evaluation Table

| File | Variable Naming | Redundancy | Clarity | Efficiency | Refactored |
| ---- | --------------- | ---------- | ------- | ---------- | ---------- |
| `count_vowels.py` | | | | | |
| `anagram_check.py` | | | | | |
| `spiral_matrix_basic` | | | | | |
| `problem_04` | | | | | |

## Redundancy Detection Checklist
- [ ] Are you looping over the array/string twice when you could map it in a single pass?
- [ ] Are there consecutive `if/elif` statements checking the exact same index?
- [ ] Did you use `list.count()` inside a `for` loop? (Catastrophic $O(N^2)$ anti-pattern).

## Logical Clarity Audit
- [ ] Does your Matrix iteration use `r` and `c` instead of `i` and `j`?
- [ ] Is your `freq {}` initialization clean, relying on `.get()`?
- [ ] If extracting a substring, did you clearly map the slice bounds `s[start:stop]`?

## Before vs After Example

### BEFORE (Poor Naming, Redundant Bounds, Unpythonic)
```python
def x(string1):
    count = 0
    for i in range(len(string1)):
        if string1[i] == 'a' or string1[i] == 'A':
            count = count + 1
    return count
```

### AFTER (Clean, Normalised, O(N))
```python
def count_a_occurrences(s: str) -> int:
    # Normalized for immediate branch evaluation
    return sum(1 for char in s.lower() if char == 'a')
```\n