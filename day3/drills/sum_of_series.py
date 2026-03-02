# S = 1/1 + 1/2 + 1/3 ... 1/N
def solve(n: int) -> float:
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return total

if __name__ == "__main__":
    print(f"{solve(3):.2f}") # 1.83\n