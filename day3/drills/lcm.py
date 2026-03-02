# LCM = (A * B) // GCD(A, B)
def gcd(a, b):
    while b: a, b = b, a % b
    return a

def solve(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

if __name__ == "__main__":
    print(solve(15, 20)) # Expected: 60\n