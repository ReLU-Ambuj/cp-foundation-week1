# Problem: Strong Number checking via layered helper functions
def factorial(k: int) -> int:
    res = 1
    for i in range(2, k + 1): res *= i
    return res

def is_strong(n: int) -> bool:
    temp, total = n, 0
    while temp > 0:
        total += factorial(temp % 10)
        temp //= 10
    return total == n

if __name__ == "__main__":
    print(is_strong(145)) # True\n