# Problem: Series summation returning float
def calculate_harmonic_series(n: int) -> float:
    return sum(1 / i for i in range(1, n + 1))

if __name__ == "__main__":
    print(f"{calculate_harmonic_series(3):.2f}") # 1.83\n