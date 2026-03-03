# Problem: LCM using GCD helper dependency layering
def gcd(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    print(lcm(15, 20)) # 60\n