def factorial(n: int) -> int:
    """Returns factorial. Expected non-negative."""
    if n < 0: return -1
    res = 1
    for i in range(2, n + 1): res *= i
    return res

def gcd(a: int, b: int) -> int:
    """Euclidean algorithm for Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Calculates LCM using GCD abstraction."""
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

def reverse_number(n: int) -> int:
    """Reverses integer map iteratively."""
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    return rev if n >= 0 else -rev

def sum_of_digits(n: int) -> int:
    """Aggregates digits of an integer algebraically."""
    temp = abs(n)
    total = 0
    while temp > 0:
        total += temp % 10
        temp //= 10
    return total
