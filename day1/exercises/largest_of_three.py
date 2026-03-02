# Problem: Find Largest of Three Numbers
# Input: Three floats A, B, C
# Output: Maximum float
# Constraints: Standard float limits
# Time/Space Complexity: O(1)

def solve(a: float, b: float, c: float) -> float:
    # Built-in max is optimized in C
    return max(a, b, c)

if __name__ == "__main__":
    print(solve(10.5, 20.1, 15.0)) # Expected: 20.1
