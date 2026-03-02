# Reverse digits looping mod 10.
def solve(n: int) -> int:
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10
    return rev if n >= 0 else -rev

if __name__ == "__main__":
    print(solve(1234)) # 4321\n