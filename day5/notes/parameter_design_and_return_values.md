# Parameter Design and Return Values

## Input Validation Inside Functions
Never blindly trust arguments. If your mathematical function requires positive integers, execute a guard clause on line 1.
```python
def factorial(n: int) -> int:
    if n < 0:
        return -1 # Or raise ValueError
```

## Avoiding Print Inside Logic Functions
A function that contains `print(result)` is essentially dead-ended. You cannot reuse that result mathematically.
**Banned CP Pattern:**
```python
def sum_two(a, b):
    print(a + b) # Useless to the caller
```

## Returning vs Printing
Always `return` the computed state. Let the caller (`main()`) deal with formatting the I/O.
```python
def sum_two(a, b) -> int:
    return a + b
```

## Multiple Return Values
Python automatically bundles comma-separated returns into an immutable `Tuple`.
```python
def min_max(arr) -> tuple:
    return min(arr), max(arr)

# Unpacking
minimum, maximum = min_max([1, 5, 2])
```

## Designing Reusable Functions
Functions should do exactly ONE thing perfectly. Do not combine checking primality and printing the first 10 primes into a single `prime_manager()` function. Build `is_prime(n)` and call it 10 times from a loop in `main()`.

## Default Arguments
If a parameter rarely changes, assign it a default value during definition.
```python
def compute_power(base, exp=2):
    return base ** exp

compute_power(5)    # 25
compute_power(5, 3) # 125
```

## Named Arguments
You can explicitly name parameters during the call to completely bypass positional ordering.
```python
compute_power(exp=3, base=5)
```
