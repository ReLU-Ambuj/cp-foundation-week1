# Problem: Convert Celsius to Fahrenheit
# Input: Float C
# Output: Float F
# Constraints: C >= -273.15 (Absolute Zero)
# Time/Space Complexity: O(1)

def solve(c: float) -> float:
    return (c * 9/5) + 32

if __name__ == "__main__":
    print(solve(0))    # Expected: 32.0
    print(solve(100))  # Expected: 212.0
