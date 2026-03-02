# Problem 8: The Remainder Problem
## Problem Statement
Given two integers A and B. Print `A % B`. Handle B = 0 by printing "Undefined".

## Clean Solution Code
```python
def solve():
    a, b = map(int, input().split())
    if b == 0:
        print("Undefined")
    else:
        print(a % b)
```
