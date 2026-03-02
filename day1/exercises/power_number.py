# Problem: Compute X to the power Y
# Input: Base X, Exponent Y
# Output: X^Y
# Constraints: Keep results within memory limits
# Time/Space: O(log Y) natively in Python

def solve(x: float, y: float) -> float:
    # In CP, pow() is built-in and optimized
    return pow(x, y)

if __name__ == "__main__":
    print(solve(2, 10)) # Expected: 1024
