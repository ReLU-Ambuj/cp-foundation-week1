# Problem: Check if Number is Palindrome
# Input: Single integer N
# Output: Boolean (True/False). Negative numbers are not palindromes (-121 != 121-)
# Constraints: -2^31 <= N <= 2^31 - 1
# Time Complexity: O(log10(N))
# Space Complexity: O(log10(N))

def solve(n: int) -> bool:
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    print(solve(121))   # Expected: True
    print(solve(-121))  # Expected: False
