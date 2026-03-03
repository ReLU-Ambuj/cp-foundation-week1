# Problem 1: Uniqueness Detector
## Problem
Given a string $S$. Print `YES` if all characters are unique, `NO` otherwise.
## Solution
```python
def solve():
    s = input()
    seen = set()
    for char in s:
        if char in seen:
            return print("NO")
        seen.add(char)
    print("YES")
```\n