# Problem: Solid Rectangle
# logic: outer=rows, inner=cols. mapping: print("* ")
def solve(r: int, c: int):
    for i in range(r):
        for j in range(c):
            print("*", end=" ")
        print()\n