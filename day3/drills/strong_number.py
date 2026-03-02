# Sum of factorials of digits == n
def fact(k):
    res = 1
    for i in range(2, k+1): res *= i
    return res

def solve(n: int) -> bool:
    temp, total = n, 0
    while temp > 0:
        total += fact(temp % 10)
        temp //= 10
    return total == n

if __name__ == "__main__":
    print(solve(145)) # True (1! + 4! + 5!)\n