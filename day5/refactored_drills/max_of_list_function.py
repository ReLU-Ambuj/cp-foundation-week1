# Problem: Encapsulate max boundary loop
def find_max(arr: list) -> int:
    if not arr: raise ValueError("Empty Array")
    res = arr[0]
    for val in arr:
        if val > res: res = val
    return res

if __name__ == "__main__":
    print(find_max([1, 5, 2])) # 5\n