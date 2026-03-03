# Problem: Spiral Traversal bounds manipulation in 2D
# Explanation: Four distinct sweeping loops contracting 4 wall variables.
def solve(n: int):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    val = 1
    
    while top <= bottom and left <= right:
        # 1. Left to Right
        for c in range(left, right + 1):
            matrix[top][c] = val; val += 1
        top += 1
        
        # 2. Top to Bottom
        for r in range(top, bottom + 1):
            matrix[r][right] = val; val += 1
        right -= 1
        
        # 3. Right to Left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = val; val += 1
            bottom -= 1
            
        # 4. Bottom to Top
        if left <= right:
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = val; val += 1
            left += 1

    # Printing Formatted
    for r in range(n):
        for c in range(n): print(f"{matrix[r][c]:02}", end=" ")
        print()

if __name__ == "__main__": solve(3)\n