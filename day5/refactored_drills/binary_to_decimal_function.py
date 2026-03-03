# Problem: Binary strings to base 10 int pure abstraction
def convert_to_decimal(binary: str) -> int:
    res, power = 0, 0
    for char in reversed(binary):
        if char == '1': res += 2 ** power
        power += 1
    return res

if __name__ == "__main__":
    print(convert_to_decimal("1010")) # 10\n