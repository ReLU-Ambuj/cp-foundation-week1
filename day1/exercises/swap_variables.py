# Problem: Swap Two Variables
# Input: Two integers A and B
# Output: Tuple (B, A)
# Constraints: N/A
# Time/Space Complexity: O(1)

def solve(a: int, b: int) -> tuple[int, int]:
    # Pythonic tuple unpacking swap
    a, b = b, a
    return a, b

if __name__ == "__main__":
    print(solve(5, 10)) # Expected: (10, 5)
