# Problem: Check if number is divisible by 5 and 11
# Input: Integer N
# Output: Boolean
# Constraints: N is integer
# Time/Space: O(1)

def solve(n: int) -> bool:
    # Math shortcut: divisible by 5 and 11 means divisible by LCM(5,11) = 55
    return n % 55 == 0

if __name__ == "__main__":
    print(solve(55)) # Expected: True
    print(solve(20)) # Expected: False
