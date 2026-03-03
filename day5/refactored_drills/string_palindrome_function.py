# Problem: String manipulation helper
def is_palindrome(s: str) -> bool:
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

if __name__ == "__main__":
    print(is_palindrome("Race car")) # True\n