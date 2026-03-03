# Problem: Count total vowels in a string
# Input: String S
# Output: Integer count
# Constraints: S can contain spaces, numbers, cases. O(N) Time. O(1) Space.

def solve(s: str) -> int:
    count = 0
    # Normalize case immediately to reduce branching logic
    for char in s.lower():
        if char in 'aeiou':
            count += 1
    return count

if __name__ == "__main__":
    print(solve("Hello World")) # 3\n