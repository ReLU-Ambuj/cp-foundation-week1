# Problem: Remove duplicates keeping order of first appearance
# Constraints: O(N) Hash map tracking.
def solve(s: str) -> str:
    seen = set()
    res = ""
    for char in s:
        if char not in seen:
            res += char
            seen.add(char)
    return res

if __name__ == "__main__":
    print(solve("programming")) # progamin\n