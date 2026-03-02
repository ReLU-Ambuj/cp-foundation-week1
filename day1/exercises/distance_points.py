# Problem: Distance between 2 Cartesian 2D points
# Input: x1, y1, x2, y2
# Output: Euclidean Distance
# Time/Space: O(1)

import math

def solve(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)

if __name__ == "__main__":
    print(solve(0, 0, 3, 4)) # Expected: 5.0
