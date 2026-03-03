# Problem: Modularize prime checking logic.
def is_prime(n: int) -> bool:
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

if __name__ == "__main__":
    print(is_prime(17)) # True\n