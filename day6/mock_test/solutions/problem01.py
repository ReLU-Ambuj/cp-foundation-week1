def is_palindrome(s: str) -> bool:
    # O(N) extraction
    clean = "".join(char.lower() for char in s if char.isalnum())
    
    # O(N) spatial two-pointer equivalent checking
    n = len(clean)
    for i in range(n // 2):
        if clean[i] != clean[n - 1 - i]:
            return False
            
    return True

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))\n