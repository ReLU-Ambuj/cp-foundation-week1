# Type System Explained

## Type Conversion
Type conversion (or casting) transforms an object from one data type to another.

### Implicit vs Explicit Casting
1. **Implicit Casting (Coercion)**: Python automatically converts compatible types to prevent data loss.
   - Example: Adding an `int` and a `float` results in a `float`.
     ```python
     result = 5 + 3.2 # result is inherently float 8.2
     ```
2. **Explicit Casting**: Forcing a variable to be a specific type using constructor functions like `int()`, `float()`, `str()`.
   - Essential when types are mutually exclusive without instruction.
     ```python
     age_str = "25"
     age_int = int(age_str)
     ```

## Why `input()` returns a string
The `input()` function acts as an interface between the program and standard input streams (which transport data as raw bytes/text). Python safely interprets these bytes strictly as string characters because it cannot infer the user's intent. The string `"100"` is fundamentally different from the integer `100`. The developer must explicitly cast it.

## The Float Precision Problem (0.1 Issue)
Due to IEEE 754 standards, floating-point numbers are represented as binary fractions. Some decimal numbers cannot be represented exactly in binary.
```python
print(0.1 + 0.2) # Outputs: 0.30000000000000004
```
**Impact:** Never use `==` to compare floating-point values. Instead, check if their absolute difference is less than a tiny epsilon margin (`abs(a - b) < 1e-9`).

## When to use `int()` vs `float()`
- Use `int()` when dealing with discrete, countable items (indexes, array lengths, iterations).
- Use `float()` when dealing with continuous measurements (physics simulations, percentages, geometry).
- *Warning*: Converting a float to an int (`int(3.9)`) truncates the decimal, it does NOT round. It simply drops `.9` returning `3`.

## Defensive Programming Habits
- Always validate types when receiving input if you aren't sure of the constraint adherence.
- During Competitive Programming inputs often come space-separated.
  ```python
  # Safe CP pattern to read two integers
  a, b = map(int, input().split())
  ```
- If doing heavy cumulative sums, prefer integer math over floating-point math to completely avoid precision deviation.
