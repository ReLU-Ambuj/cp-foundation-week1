# Problem: Reverse a Given Integer
# Input: Single integer N
# Output: Single integer (reversed), maintaining the sign
# Constraints: -10^9 <= N <= 10^9
# Time Complexity: O(log10(N)) - number of digits
# Space Complexity: O(log10(N)) - string conversion space

def solve(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_abs = int(str(abs(n))[::-1])
    return sign * reversed_abs

if __name__ == "__main__":
    # Test cases
    print(solve(1234))  # Expected: 4321
    print(solve(-567))  # Expected: -765
