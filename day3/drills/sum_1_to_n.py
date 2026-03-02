# Problem: Sum 1 to N using iteration
# Time: O(N), Space: O(1)

def solve(n: int) -> int:
    total = 0 # Accumulator Pattern
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    print(solve(5)) # Expected: 15\n