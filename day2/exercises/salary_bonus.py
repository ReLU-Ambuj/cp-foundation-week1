# Problem: Calculate salary bonus based on years of service and salary level.
# Years > 10: 10% bonus
# Years > 5 and <= 10: 5% bonus (only if salary < 50000, else no bonus)
# Else: No bonus
# Input: Salary(float), Years(int)
# Output: Float Bonus Amount
# Time/Space: O(1)

def solve(salary: float, years: int) -> float:
    """
    Edge logic: Flattening nested rules.
    """
    if salary < 0 or years < 0:
        return 0.0
        
    if years > 10:
        return salary * 0.10
    elif 5 < years <= 10 and salary < 50000:
        return salary * 0.05
    else:
        return 0.0

if __name__ == "__main__":
    print(solve(60000, 11)) # Expected: 6000.0
    print(solve(40000, 8))  # Expected: 2000.0
    print(solve(60000, 8))  # Expected: 0.0\n