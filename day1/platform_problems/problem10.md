# Problem 10: Sum of Digits String Method
## Problem Statement
Compute the sum of digits of $N$ using string property.

## Clean Solution Code
```python
def solve():
    s = input().strip()
    if s[0] == '-': s = s[1:]
    total = sum(int(digit) for digit in s)
    print(total)
```
