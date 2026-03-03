# Problem: Count frequency of all characters
# Input: String S
# Output: Dictionary Mapping {Char: Count}
# Constraints: O(N) Time. O(K) Space (K = unique chars).

def solve(s: str) -> dict:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    print(solve("apple")) # {'a': 1, 'p': 2, 'l': 1, 'e': 1}\n