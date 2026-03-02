# Nested Loops and Time Complexity Multipliers

## Basic Mechanics
When Loop A (outer) surrounds Loop B (inner), Loop B must run to full completion *for every single step* of Loop A.
If Loop A runs $N$ times, and Loop B runs $M$ times, total complexity is $O(N \times M)$. If $M = N$, you have formed an $O(N^2)$ algorithm.

## Row-Column Thinking
The foundation of matrix grids, coordinate mapping, and visual patterns.
- **Outer Loop**: Represents Rows (Y-axis moving downward).
- **Inner Loop**: Represents Columns (X-axis moving to the right).
To print a 5x5 grid:
```python
for r in range(5):        # Controls which row we are on
    for c in range(5):    # Controls printing left-to-right on that specific row
        print("*", end=" ")
    print()               # Moves the cursor to the next line AFTER a row finishes
```

## Coordinate Mapping for Patterns
To build geometric patterns (triangles, diamonds), look for the mathematical relationship between the row coordinate `r` and column coordinate `c`.
Example: If `r == c`, you are directly on the main diagonal.
If `r + c == N - 1`, you are on the anti-diagonal.

## Symmetry Reasoning
When building complex mirrored structures (like a diamond), split the logic into two separate nested loop blocks:
1. Upper half expanding outward.
2. Lower half contracting inward.
Never try to force mirrored geometry into a single nested loop without heavy, unreadable conditional maths.\n