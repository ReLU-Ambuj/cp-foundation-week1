# Problem: Get ASCII value of character
# Input: Single string character C
# Output: Integer ASCII code
# Constraints: len(C) == 1
# Time/Space: O(1)

def solve(c: str) -> int:
    return ord(c)

if __name__ == "__main__":
    print(solve('A')) # Expected: 65
    print(solve('a')) # Expected: 97
