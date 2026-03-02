# Problem: Centered Pyramid
# logic: spaces = N-i, stars = (2*i)-1
def solve(n: int):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)\n