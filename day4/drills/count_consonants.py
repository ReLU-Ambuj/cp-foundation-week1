# Problem: Count consonants in a string
# Input: String S
# Output: Integer count
# Constraints: O(N) Time.

def solve(s: str) -> int:
    count = 0
    for char in s.lower():
        # A consonant MUST be an alphabet letter AND not a vowel
        if char.isalpha() and char not in 'aeiou':
            count += 1
    return count

if __name__ == "__main__":
    print(solve("Hello 123!")) # 3\n