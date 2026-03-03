# Problem: Substrings nested loop logic. O(N^2)
def solve(s: str):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j], end=", ")
    print()

if __name__ == "__main__":
    solve("abc") # a, ab, abc, b, bc, c,\n