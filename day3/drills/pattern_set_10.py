# Problem: Number Pyramid Palindrome
# logic: count up to row num, then count down
def solve(n: int):
    for i in range(1, n + 1):
        print("  " * (n - i), end="")
        for j in range(1, i + 1): print(j, end=" ")
        for j in range(i - 1, 0, -1): print(j, end=" ")
        print()\n