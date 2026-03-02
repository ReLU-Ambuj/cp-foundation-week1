# Problem: Assign grade based on marks.
# 90-100: A, 80-89: B, 70-79: C, <70: F
# Input: Integer marks
# Output: String Grade
# Constraints: 0 <= marks <= 100
# Time Complexity: O(1)
# Space Complexity: O(1)

def solve(marks: int) -> str:
    """
    Edge Cases:
    - Exactly 90 (Boundary)
    - Out of bounds (<0 or >100)
    """
    if marks < 0 or marks > 100:
        return "Invalid marks"
        
    # Python relies on sequential evaluation avoiding redundant >= checks
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"

if __name__ == "__main__":
    print(solve(90))  # Expected: A
    print(solve(89))  # Expected: B
    print(solve(65))  # Expected: F\n