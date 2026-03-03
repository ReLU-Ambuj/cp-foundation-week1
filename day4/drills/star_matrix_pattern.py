# Problem: 2D Grid mapping row-major traversal
# Grid visualization constraint: N x M
def solve(rows: int, cols: int):
    for r in range(rows):
        for c in range(cols):
            print(f"({r},{c})*", end=" ")
        print()
if __name__ == "__main__": solve(3, 3)\n