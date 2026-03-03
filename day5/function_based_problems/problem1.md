# Problem 1: Prime Palindromes in Range
## Problem: 
Given `A`, `B`. Print all numbers in range $[A, B]$ that are BOTH prime and palindromic.
## Required Decomposition:
Do not write one massive loop.
1. `is_prime(n: int) -> bool`
2. `is_palindrome(n: int) -> bool`
3. `solve(a: int, b: int) -> list`
## Solution:
```python
def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def solve(a: int, b: int) -> list:
    return [i for i in range(a, b + 1) if is_prime(i) and is_palindrome(i)]
```\n