# Divisible by 2, 3, both, or neither. O(1)
def solve(n: int) -> str:
    ans = ""
    ans += "2" if n % 2 == 0 else ""
    ans += "3" if n % 3 == 0 else ""
    return ans if ans else "None"\n