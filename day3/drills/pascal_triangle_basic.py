# Pascal Triangle O(N^2) Math
def solve(n: int):
    for i in range(n):
        val = 1
        for j in range(1, i + 2):
            print(val, end=" ")
            val = val * (i - j + 1) // j
        print()\n