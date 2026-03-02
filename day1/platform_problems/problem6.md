# Problem 6: Last Digit Extraction
## Problem Statement
Given an integer N (can be negative), output the absolute value of its last digit.

## Hint
`-123 % 10` in Python yields `7`, not `3`. Use `abs(N) % 10`.

## Clean Solution Code
```python
def solve():
    n = int(input())
    print(abs(n) % 10)
```
