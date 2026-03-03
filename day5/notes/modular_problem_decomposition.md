# Modular Problem Decomposition

## Breaking Problems into Smaller Tasks
If a problem asks you to: "Find the sum of all prime numbers in an array that are also palindromes."
**BAD**: Writing one massive 50-line loop.
**GOOD**:
1. `is_prime(n)` - Handles math.
2. `is_palindrome(n)` - Handles strings.
3. `solve(arr)` - Iterates through array, returning `sum(n)` if both helpers return True.

## Function Layering
Your `main()` or `solve()` function should read like a high-level English sentence. Top-level functions orchestrate logic; low-level helper functions execute the raw bitwise/string mechanics.

## Avoiding Repetition (DRY Principle)
Don't Repeat Yourself (DRY). If you write the same `while` loop twice in a file to reverse a number, you have failed the architecture test. Extract it into `reverse_num(n)`.

## Testing Functions Independently
Because your helpers are "pure", you can write specific edge-case tests `is_prime(0)`, `is_prime(-1)` at the bottom of the file without running the entire CP problem's Input/Output logic.

## Refactoring Example

### Before (Spaghetti Script)
```python
primes = []
for n in range(10, 50):
    p = True
    temp = n
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    if n == rev:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                p = False
                break
        if p:
            primes.append(n)
print(primes)
```

### After (Structured Abstraction)
```python
def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solve(start: int, end: int) -> list:
    return [n for n in range(start, end) if is_palindrome(n) and is_prime(n)]

print(solve(10, 50))
```\n