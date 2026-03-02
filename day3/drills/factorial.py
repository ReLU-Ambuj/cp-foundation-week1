# Problem: Compute N!
# Constraints: N >= 0. O(N) Time.

def solve(n: int) -> int:
    if n < 0: return -1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(solve(5)) # Expected: 120\n