# Division logic loop
def solve(n: int) -> str:
    if n == 0: return "0"
    bin_str = ""
    while n > 0:
        bin_str = str(n % 2) + bin_str
        n //= 2
    return bin_str

if __name__ == "__main__":
    print(solve(10)) # 1010\n