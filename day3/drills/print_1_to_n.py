# Problem: Print numbers from 1 to N
# Constraints: N > 0. O(N) Time, O(1) Space.

def solve(n: int) -> None:
    # Exclusive upper bound requires N+1
    for i in range(1, n + 1):
        print(i, end=" ")
    print()
    
if __name__ == "__main__":
    solve(5) # Expected: 1 2 3 4 5\n