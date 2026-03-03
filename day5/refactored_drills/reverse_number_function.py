# Problem: Encapsulate reversing digit mapping
def reverse_digits(n: int) -> int:
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    return rev if n >= 0 else -rev

if __name__ == "__main__":
    print(reverse_digits(-123)) # -321\n