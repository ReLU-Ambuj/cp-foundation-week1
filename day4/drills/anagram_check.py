# Problem: Check if two strings are anagrams of one another.
# Constraints: Fast dictionary comparison. O(N).

def solve(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
        
    freq = {}
    # Increment for s1, decrement for s2
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        freq[char] = freq.get(char, 0) - 1
        
    # If anagram, all values return to 0 perfectly
    for count in freq.values():
        if count != 0:
            return False
            
    return True

if __name__ == "__main__":
    print(solve("listen", "silent")) # True\n