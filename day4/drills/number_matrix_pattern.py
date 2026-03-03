# Problem: Sequential counting through a nested 2D matrix layout
def solve(rows: int, cols: int):
    count = 1
    for r in range(rows):
        for c in range(cols):
            print(f"{count:02}", end=" ")
            count += 1
        print()
if __name__ == "__main__": solve(3, 3)\n