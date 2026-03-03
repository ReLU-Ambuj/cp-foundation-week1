# Problem: Find the character that appears the most.
# Input: String S
# Output: Optimal Character
# Constraints: O(N) Time. Single pass frequency maxing.

def solve(s: str) -> str:
    if not s: return ""
    freq = {}
    max_char = s[0]
    max_count = 0
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        if freq[char] > max_count:
            max_count = freq[char]
            max_char = char
            
    return max_char

if __name__ == "__main__":
    print(solve("abcbba")) # 'b'\n