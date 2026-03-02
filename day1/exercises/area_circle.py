# Problem: Compute Area of a Circle
# Input: Radius R
# Output: Area
# Constraints: R >= 0
# Time/Space: O(1)

import math

def solve(r: float) -> float:
    return math.pi * r * r

if __name__ == "__main__":
    print(f"{solve(5):.2f}") # Expected: 78.54
