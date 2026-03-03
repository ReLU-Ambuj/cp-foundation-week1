# Problem 5: Subsequence Verification
## Problem
Given String $A$ and $B$. Is $A$ a subsequence of $B$? (Characters appear in order, but not necessarily contiguous).
## Solution
```python
def solve():
    a, b = input().split()
    i = 0
    for char in b:
        if i < len(a) and char == a[i]:
            i += 1
    print("YES" if i == len(a) else "NO")
```\n