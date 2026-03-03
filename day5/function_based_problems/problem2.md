# Problem 2: Anagram Groups
## Problem:
Given a list of strings, return how many strict pairs of anagrams exist.
## Required Decomposition:
1. `are_anagrams(s1, s2) -> bool`
2. `solve(arr) -> int` (Uses nested loops to check pairs)
## Solution:
```python
def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def solve(arr: list) -> int:
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if are_anagrams(arr[i], arr[j]):
                count += 1
    return count
```\n