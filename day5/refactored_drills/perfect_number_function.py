# Problem: Perfect Number Encapsulation
def is_perfect(n: int) -> bool:
    if n <= 1: return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i * i != n:
                total += (n // i)
        i += 1
    return total == n

if __name__ == "__main__":
    print(is_perfect(28)) # True\n