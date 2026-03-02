# Problem 3: Point in Rectangle
## Problem Statement
Given bottom-left $(x1, y1)$, top-right $(x2, y2)$, and point $(px, py)$. Print "Inside" if strictly inside, "Boundary" if on line, "Outside" otherwise.

## Clean Python Solution
```python
def solve():
    x1, y1, x2, y2, px, py = map(int, input().split())
    # Bounding Box Logic
    if x1 < px < x2 and y1 < py < y2:
        print("Inside")
    elif x1 <= px <= x2 and y1 <= py <= y2:
        print("Boundary")
    else:
        print("Outside")
```\n