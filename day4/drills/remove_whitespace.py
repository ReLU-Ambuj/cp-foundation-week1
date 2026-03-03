# Problem: Strip all spaces completely
def solve(s: str) -> str:
    return "".join(char for char in s if char != " ")
if __name__ == "__main__": print(solve(" a b c ")) # abc\n