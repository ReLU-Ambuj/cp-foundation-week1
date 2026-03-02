# Problem 9: Boolean Logic
## Problem Statement
Given two boolean strings ("True" or "False"). Print the result of `A AND B`, `A OR B`, `A XOR B`.

## Clean Solution Code
```python
def solve():
    a_str, b_str = input().split()
    a = a_str == "True"
    b = b_str == "True"
    print(a and b)
    print(a or b)
    print(a ^ b)
```
