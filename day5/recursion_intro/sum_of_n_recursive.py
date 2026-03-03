# Recursively sum 1 to N
def sum_n(n: int) -> int:
    if n == 1: return 1
    return n + sum_n(n - 1)

if __name__ == "__main__":
    print(sum_n(5)) # 15\n