===== FILE: cp-foundation-week1/day4/notes/nested_loop_matrix_thinking.md =====
# Nested Loop Matrix Thinking

## The 2D Iteration Model
A 2D matrix in Python is simply a List containing other Lists.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## Row-Major Traversal Grid
You must adopt this exact visual coordinate mapping in your mind:
```text
(0,0) (0,1) (0,2)  [Row 0]
(1,0) (1,1) (1,2)  [Row 1]
(2,0) (2,1) (2,2)  [Row 2]
```
- `matrix[1][2]` means -> Go to Row Index `1`. Inside that row, go to Col Index `2`. The value is `6`.

## Row-Major Iteration Implementation
```python
rows = len(matrix)
cols = len(matrix[0]) # Assumes rectangular matrix

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print() # New line per row
```

## Diagonal Index Relationships
In a strictly Square matrix ($N \times N$):
1. **Main Diagonal** (Top-Left to Bottom-Right): The row always equals the column. `r == c`
2. **Anti Diagonal** (Top-Right to Bottom-Left): The row and column always sum to $N - 1$. `r + c == N - 1`

## Spiral Traversal Intuition
To traverse spirally, you cannot use a simple nested `for r.. for c..`. 
You must maintain 4 strict bounding walls: `top`, `bottom`, `left`, `right`.
You perform 4 distinct horizontal/vertical sweeps, strictly shrinking the wall boundaries inward after each sweep completes until the walls cross each other.\n