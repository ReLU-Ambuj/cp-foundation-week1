# Problem: Floyd's Triangle
# logic: independent counter mapping
def solve(n: int):
    count = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()\n