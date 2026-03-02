# Problem: Hollow Square
# mapping: if boundary (r==0|r==N-1|c==0|c==N-1) print * else space
def solve(n: int):
    for r in range(n):
        for c in range(n):
            if r == 0 or r == n - 1 or c == 0 or c == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()\n