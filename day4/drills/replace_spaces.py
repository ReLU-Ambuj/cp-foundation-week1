# Problem: Replace spaces with '%20'
def solve(s: str) -> str:
    res = ""
    for char in s:
        res += "%20" if char == ' ' else char
    return res
if __name__ == "__main__": print(solve("a b")) # a%20b\n