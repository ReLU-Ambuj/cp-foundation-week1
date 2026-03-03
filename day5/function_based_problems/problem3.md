# Problem 3: Safe Matrix Extraction
## Problem:
Given an $N \times M$ matrix $grid$, coordinates $R, C$ and a radius $K$. Return a list of all items within that radius bounds.
## Required Decomposition:
1. `is_valid_cell(r, c, rows, cols) -> bool` (Guard clause for index out of bounds)
2. `extract_radius(grid, r, c, k) -> list`
## Solution:
```python
def is_valid(r: int, c: int, rows: int, cols: int) -> bool:
    return 0 <= r < rows and 0 <= c < cols

def solve(grid: list, r: int, c: int, k: int) -> list:
    res = []
    rows, cols = len(grid), len(grid[0])
    for i in range(r - k, r + k + 1):
        for j in range(c - k, c + k + 1):
            if is_valid(i, j, rows, cols):
                res.append(grid[i][j])
    return res
```\n