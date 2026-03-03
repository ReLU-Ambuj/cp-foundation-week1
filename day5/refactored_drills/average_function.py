# Problem: Return float average. Throw if empty.
def calculate_average(arr: list) -> float:
    if not arr: raise ValueError("Cannot average empty list")
    total = sum(arr)
    return total / len(arr)

if __name__ == "__main__":
    print(calculate_average([1, 2, 3])) # 2.0\n