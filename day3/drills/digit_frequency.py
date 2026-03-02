# Frequency of digit D in N
def solve(n: int, d: int) -> int:
    n = abs(n)
    if n == 0 and d == 0: return 1
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n //= 10
    return count

if __name__ == "__main__":
    print(solve(122342, 2)) # 3\n