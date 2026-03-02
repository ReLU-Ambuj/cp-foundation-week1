# Problem: Check if 3 sides form a valid triangle
# Input: 3 integers a, b, c
# Output: Boolean
# Constraints: a, b, c > 0
# Math Logic: Sum of any two sides must strictly be > third side.
# Time/Space: O(1)

def solve(a: int, b: int, c: int) -> bool:
    """
    Edge Cases:
    - Non-positive sides (<= 0)
    - Collinear sides (sum of two == third) -> Invalid
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
        
    # Validate strictly via triangle inequality theorem
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == "__main__":
    print(solve(3, 4, 5)) # Expected: True
    print(solve(1, 2, 3)) # Expected: False (Collinear)
    print(solve(-1, 2, 3))# Expected: False\n