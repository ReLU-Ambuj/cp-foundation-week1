def is_prime(k: int) -> bool:
    if k <= 1: return False
    i = 2
    while i * i <= k:
        if k % i == 0: return False
        i += 1
    return True

def is_prime_product(n: int) -> bool:
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            factor1 = i
            factor2 = n // i
            # Are they both prime?
            if is_prime(factor1) and is_prime(factor2):
                return True
        i += 1
    return False

if __name__ == "__main__":
    print(is_prime_product(15)) # True
    print(is_prime_product(12)) # False\n