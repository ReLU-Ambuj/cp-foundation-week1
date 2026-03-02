# Problem: Job eligibility check
# Age must be between [18, 50]. If age > 50, require 'senior=True' flag.
# Output: True/False
# Time/Space: O(1)

def solve(age: int, senior: bool) -> bool:
    if age < 18:
        return False
    if age > 50 and not senior:
        return False
    return True

if __name__ == "__main__":
    print(solve(16, False)) # Expected: False
    print(solve(30, False)) # Expected: True
    print(solve(60, False)) # Expected: False
    print(solve(60, True))  # Expected: True\n