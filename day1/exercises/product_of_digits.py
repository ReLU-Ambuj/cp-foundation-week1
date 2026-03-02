# Problem: Product of Digits of a Number
# Input: Integer N
# Output: Product of absolute digits
# Constraints: -10^18 <= N <= 10^18
# Time Complexity: O(log10(N))
# Space Complexity: O(1) auxiliary

def solve(n: int) -> int:
    n = abs(n)
    if n == 0: return 0
    product = 1
    while n > 0:
        product *= (n % 10)
        n //= 10
    return product

if __name__ == "__main__":
    print(solve(123))  # Expected: 6
    print(solve(405))  # Expected: 0
