# Capitalize starting letters of words manually
def solve(s: str) -> str:
    res = ""
    new_word = True
    for char in s:
        if char == " ":
            res += " "
            new_word = True
        elif new_word:
            res += char.upper()
            new_word = False
        else:
            res += char
    return res
if __name__ == "__main__": print(solve("hello  world")) # Hello  World\n