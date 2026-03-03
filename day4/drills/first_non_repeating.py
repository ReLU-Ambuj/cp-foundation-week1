# Problem: Find FIRST character that does not repeat.
# Input: String S
# Output: Character or None
# Constraints: O(N) Time. Two-pass dictionary algorithm.

def solve(s: str):
    freq = {}
    # Pass 1: Build map
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    # Pass 2: Find sequential first
    for char in s:
        if freq[char] == 1:
            return char
    return None

if __name__ == "__main__":
    print(solve("swiss")) # 'w'\n