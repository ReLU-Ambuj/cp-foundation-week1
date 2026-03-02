# Problem 2: Strict Inequality
## Problem Statement
Given $X, Y, Z$. Print "Sorted" if $X < Y < Z$, otherwise "Unsorted".

## Clean Python Solution
```python
def solve():
    x, y, z = map(int, input().split())
    # Chaining operators
    if x < y < z:
        print("Sorted")
    else:
        print("Unsorted")
```\n