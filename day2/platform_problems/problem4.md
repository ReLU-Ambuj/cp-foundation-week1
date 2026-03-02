# Problem 4: Quadrant Extractor
## Problem Statement
Given X, Y. Output Quadrant 1, 2, 3, 4, Origin, X-axis, or Y-axis.

## Clean Python Solution
```python
def solve():
    x, y = map(int, input().split())
    if x == 0 and y == 0: print("Origin")
    elif x == 0: print("Y-axis")
    elif y == 0: print("X-axis")
    elif x > 0 and y > 0: print("1")
    elif x < 0 and y > 0: print("2")
    elif x < 0 and y < 0: print("3")
    else: print("4")
```\n