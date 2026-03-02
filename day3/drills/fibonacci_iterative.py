# Problem: Print N terms of Fibonacci heavily optimized. O(N).
def solve(n: int) -> None:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

if __name__ == "__main__":
    solve(5) # Expected: 0 1 1 2 3\n