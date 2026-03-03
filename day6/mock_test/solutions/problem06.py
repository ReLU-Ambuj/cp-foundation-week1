def longest_unique_substring(s: str) -> int:
    if not s: return 0
    seen = {}
    max_len = 0
    left = 0
    
    # Sliding window mapped linearly
    for right in range(len(s)):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 # Contract window
            
        seen[char] = right # Update absolute index
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            
    return max_len

if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb")) # 3\n