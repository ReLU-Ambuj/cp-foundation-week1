# Problem: Average of 5 numbers
# Input: List/Tuple of 5 floats
# Output: Average float
# Time/Space: O(1)

def solve(nums: list[float]) -> float:
    return sum(nums) / len(nums)

if __name__ == "__main__":
    print(solve([10, 20, 30, 40, 50])) # Expected: 30.0
