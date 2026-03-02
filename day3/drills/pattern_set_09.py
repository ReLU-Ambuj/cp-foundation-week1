# Problem: Diamond
# logic: Upper pyramid + Lower inverted pyramid
def solve(n: int):
    # Upper
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))\n