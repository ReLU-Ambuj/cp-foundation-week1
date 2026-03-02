# Problem: Count Digits in a Number
# Input: Single integer N
# Output: Number of digits in N
# Constraints: -10^18 <= N <= 10^18
# Time Complexity: O(1) mathematical, O(d) string
# Space Complexity: O(d) for string

import math

def solve(n: int) -> int:
    if n == 0:
        return 1
    # Mathematical approach is faster than string conversion for CP
    return math.floor(math.log10(abs(n))) + 1

if __name__ == "__main__":
    print(solve(12345)) # Expected: 5
    print(solve(-987))  # Expected: 3
