# Problem 5: Even Odd Swap Modulo
## Problem Statement
Given an integer N. If N is even, output N / 2. If N is odd, output N * 3 + 1.

## Clean Solution Code
```python
def solve():
    n = int(input())
    if n % 2 == 0:
        print(n // 2) # Use floor division to maintain int
    else:
        print(n * 3 + 1)
```
