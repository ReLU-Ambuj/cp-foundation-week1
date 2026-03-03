# Problem 3: Panagram Check
## Problem
Given $S$. Does it contain every letter of the English alphabet at least once? Ignore case.
## Solution
```python
def solve():
    s = set(input().lower())
    count = sum(1 for char in s if 'a' <= char <= 'z')
    print("YES" if count == 26 else "NO")
```\n