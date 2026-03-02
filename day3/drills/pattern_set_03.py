# Problem: Inverted Right Triangle
# row mapping: cols = N - row number
def solve(n: int):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()\n