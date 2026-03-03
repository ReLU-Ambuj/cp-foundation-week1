# Problem: Reverse string manually (without slicing shorthand)
# Constraints: O(N) Time.
def solve(s: str) -> str:
    rev = ""
    # Range mechanics reverse traversal
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev

if __name__ == "__main__":
    print(solve("abcd")) # "dcba"\n