# Problem: Calculate Percentage
# Input: Obtained marks, Total marks
# Output: Percentage
# Time/Space: O(1)

def solve(obtained: float, total: float) -> float:
    if total == 0: return 0.0
    return (obtained / total) * 100

if __name__ == "__main__":
    print(solve(45, 50)) # Expected: 90.0
