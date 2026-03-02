# Problem: Absolute Difference Between Two Numbers
# Input: A, B
# Output: |A - B|
# Time/Space: O(1)

def solve(a: float, b: float) -> float:
    return abs(a - b)

if __name__ == "__main__":
    print(solve(10, 25)) # Expected: 15
