# Problem: Check String Palindrome
# Constraints: Ignore spaces, capitalization, punctuation. O(N) Time. Two pointers.

def solve(s: str) -> bool:
    # 1. Clean data natively
    clean = ""
    for char in s:
        if char.isalnum(): clean += char.lower()
        
    # 2. Check half-length matching to save execution time
    n = len(clean)
    for i in range(n // 2):
        if clean[i] != clean[n - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    print(solve("A man, a plan, a canal: Panama")) # True\n