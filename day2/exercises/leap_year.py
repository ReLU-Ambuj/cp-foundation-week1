# Problem: Determine if a given year is a leap year using boolean logic.
# Input: Integer Y
# Output: Boolean (True/False)
# Constraints: 1 <= Y <= 9999
# Time Complexity: O(1)
# Space Complexity: O(1)

def solve(year: int) -> bool:
    """
    Edge Cases:
    - 2024 (Divisible by 4, not 100) -> True
    - 1900 (Divisible by 100, not 400) -> False
    - 2000 (Divisible by 400) -> True
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    print(solve(2024)) # Expected: True
    print(solve(1900)) # Expected: False
    print(solve(2000)) # Expected: True\n