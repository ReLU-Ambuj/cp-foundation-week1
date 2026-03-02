# Problem 5: The Safe Division
## Problem Statement
Given $A, B$. Output $A/B$. Output "Division by Zero" if B is 0.

## Clean Python Solution
```python
def solve():
    # Early Return / Guard Clause
    a, b = map(int, input().split())
    if b == 0:
        print("Division by Zero")
        return
    print(a // b)
```\n