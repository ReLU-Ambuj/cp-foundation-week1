# Problem: Right Triangle
# row mapping: cols = row number
def solve(n: int):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()\n