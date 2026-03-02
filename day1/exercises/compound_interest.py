# Problem: Compute Compound Interest
# Input: Principal P, Rate R, Time T in years
# Output: Compound Interest (Amount - Principal)
# Constraints: Standard limits
# Time/Space Complexity: O(1)

def solve(p: float, r: float, t: float) -> float:
    amount = p * ((1 + r/100) ** t)
    return amount - p

if __name__ == "__main__":
    print(f"{solve(1000, 5, 2):.2f}") # Expected: 102.50
