# Problem: Calculate Profit/Loss status
# Input: Cost Price (CP), Selling Price (SP)
# Output: String determining Profit, Loss, or Break Even
# Constraints: CP >= 0, SP >= 0
# Time/Space: O(1)

def solve(cp: float, sp: float) -> str:
    """
    Edge Cases:
    - cp == sp (Break Even)
    - Negative values (handled by guard clauses)
    """
    if cp < 0 or sp < 0:
        return "Invalid Prices"
        
    if sp > cp:
        return f"Profit: {sp - cp}"
    elif sp < cp:
        return f"Loss: {cp - sp}"
    else:
        return "Break Even"

if __name__ == "__main__":
    print(solve(100, 120)) # Expected: Profit: 20
    print(solve(100, 80))  # Expected: Loss: 20
    print(solve(100, 100)) # Expected: Break Even\n