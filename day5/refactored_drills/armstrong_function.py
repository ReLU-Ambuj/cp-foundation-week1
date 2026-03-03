# Problem: Armstrong validation pure function
def count_digits(n: int) -> int:
    return len(str(n))

def is_armstrong(n: int) -> bool:
    temp, total, length = n, 0, count_digits(n)
    while temp > 0:
        total += (temp % 10) ** length
        temp //= 10
    return total == n

if __name__ == "__main__":
    print(is_armstrong(153)) # True\n