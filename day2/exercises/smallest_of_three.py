# Smallest of 3 relying on explicit CFG. O(1)
def solve(a: int, b: int, c: int) -> int:
    res = a
    if b < res: res = b
    if c < res: res = c
    return res\n