# Problem: Pure Function Euclidean GCD
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    print(gcd(48, 18)) # 6\n