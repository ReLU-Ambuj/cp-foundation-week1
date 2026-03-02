# Armstrong logic sum(digits^len)
def solve(n: int) -> bool:
    temp = n
    length = len(str(n))
    total = 0
    while temp > 0:
        total += (temp % 10) ** length
        temp //= 10
    return total == n

if __name__ == "__main__":
    print(solve(153)) # True\n