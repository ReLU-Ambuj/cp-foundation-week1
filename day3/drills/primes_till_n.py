# Problem: Print primes up to N
def is_prime(k: int) -> bool:
    if k <= 1: return False
    i = 2
    while i * i <= k:
        if k % i == 0: return False
        i += 1
    return True

def solve(n: int) -> list[int]:
    return [i for i in range(2, n + 1) if is_prime(i)]

if __name__ == "__main__":
    print(solve(20)) # Expected: [2, 3, 5, 7, 11, 13, 17, 19]\n