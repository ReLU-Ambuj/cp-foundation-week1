# Problem: Check if N is prime in O(sqrt(N))
def solve(n: int) -> bool:
    if n <= 1: return False
    # Using while loop to stop at sqrt
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False # Early Return / Guard
        i += 1
    return True

if __name__ == "__main__":
    print(solve(17)) # True
    print(solve(18)) # False\n