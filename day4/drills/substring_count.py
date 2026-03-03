# Problem: Count non-overlapping occurrences of substring Sub in S
# Constraints: O(N * M) checking
def solve(s: str, sub: str) -> int:
    if not sub: return 0
    count = 0
    n, m = len(s), len(sub)
    i = 0
    while i <= n - m:
        if s[i:i+m] == sub:
            count += 1
            i += m # Skip over the hit completely (non-overlapping)
        else:
            i += 1
    return count

if __name__ == "__main__":
    print(solve("aaaa", "aa")) # 2\n