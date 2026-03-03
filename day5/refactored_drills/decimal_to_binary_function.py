# Problem: Number system conversion modularization
def convert_to_binary(n: int) -> str:
    if n == 0: return "0"
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

if __name__ == "__main__":
    print(convert_to_binary(10)) # "1010"\n