# Problem: Output items strictly on the primary and anti diagonals
def solve(n: int):
    for r in range(n):
        for c in range(n):
            if r == c or (r + c == n - 1):
                print("X", end="")
            else:
                print("O", end="")
        print()
if __name__ == "__main__": solve(5)\n