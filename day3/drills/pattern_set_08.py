# Problem: X Pattern / Cross
# mapping: main diagonal (r==c) or anti-diagonal (r+c == N-1)
def solve(n: int):
    for r in range(n):
        for c in range(n):
            if r == c or r + c == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()\n