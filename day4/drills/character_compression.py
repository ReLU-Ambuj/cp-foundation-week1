# Problem: Basic Run-Length Encoding (aabcccccaaa -> a2b1c5a3)
# Constraints: O(N) sequential tracking.
def solve(s: str) -> str:
    if not s: return ""
    
    res = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res += s[i-1] + str(count)
            count = 1  # Reset state
            
    # Final terminal bound flush
    res += s[-1] + str(count)
    return res

if __name__ == "__main__":
    print(solve("aabcccccaaa")) # a2b1c5a3
    print(solve("a")) # a1\n