# Problem: Check Even or Odd
# Input: Integer N
# Output: String "Even" or "Odd"
# Constraints: N is integer
# Time/Space: O(1)

def solve(n: int) -> str:
    # Bitwise AND is marginally faster than modulo
    return "Odd" if n & 1 else "Even"

if __name__ == "__main__":
    print(solve(42)) # Expected: Even
    print(solve(7))  # Expected: Odd
