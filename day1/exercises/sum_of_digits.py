# Problem: Sum of Digits of a Number
# Input: Integer N
# Output: Sum of absolute digits
# Constraints: -10^18 <= N <= 10^18
# Time Complexity: O(log10(N))
# Space Complexity: O(log10(N))

def solve(n: int) -> int:
    # Generator expression memory efficient sum
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == "__main__":
    print(solve(123))   # Expected: 6
    print(solve(-456))  # Expected: 15
