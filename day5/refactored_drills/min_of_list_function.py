# Problem: Encapsulate min boundary loop
def find_min(arr: list) -> int:
    if not arr: raise ValueError("Empty Array")
    res = arr[0]
    for val in arr:
        if val < res: res = val
    return res

if __name__ == "__main__":
    print(find_min([1, 5, 2])) # 1\n