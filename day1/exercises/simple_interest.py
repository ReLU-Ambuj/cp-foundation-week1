# Problem: Compute Simple Interest
# Input: Principal P, Rate R, Time T
# Output: Simple Interest
# Constraints: P > 0, R > 0, T > 0
# Time/Space Complexity: O(1)

def solve(p: float, r: float, t: float) -> float:
    return (p * r * t) / 100

if __name__ == "__main__":
    print(solve(1000, 5, 2)) # Expected: 100.0
