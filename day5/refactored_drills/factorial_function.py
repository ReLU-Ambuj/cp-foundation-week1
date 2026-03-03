# Problem: Encapsulate factorial math O(N)
def factorial(n: int) -> int:
    if n < 0: return -1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    print(factorial(5)) # 120\n