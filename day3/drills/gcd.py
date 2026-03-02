# Euclidean algorithm iter. O(log(min(a,b)))
def solve(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(solve(48, 18)) # Expected: 6\n