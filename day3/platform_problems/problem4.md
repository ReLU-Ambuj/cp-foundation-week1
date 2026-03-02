# Problem 4: Leading Zeros Binary
## Problem:
Given a binary string. Count how many leading zeros exist using iteration.
## Solution:
```python
def solve():
    s = input()
    count = 0
    for char in s:
        if char == '0': count += 1
        else: break
    print(count)
```\n