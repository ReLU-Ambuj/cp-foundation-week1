# Problem: Number Triangle
# mapping: print(j)
def solve(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()\n