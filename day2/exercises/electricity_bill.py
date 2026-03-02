# Problem: Calculate staggered electricity bill
# Tiered pricing:
# 0-50 units: $0.50/unit
# 51-150 units: $0.75/unit
# >150 units: $1.20/unit
# Plus 20% surcharge on final total always.
# Input: Integer units
# Output: Float Total Bill
# Time/Space: O(1)

def solve(units: int) -> float:
    """
    Edge Cases:
    - Exactly 50, 150 units 
    - 0 units
    - Negative units (invalid)
    """
    if units < 0:
        raise ValueError("Units cannot be negative")
        
    bill = 0.0
    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = (50 * 0.50) + ((units - 50) * 0.75)
    else:
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
        
    # Surcharge
    return bill * 1.20

if __name__ == "__main__":
    print(solve(40))  # Expected: 24.0
    print(solve(100)) # Expected: 75.0
    print(solve(200)) # Expected: 192.0\n