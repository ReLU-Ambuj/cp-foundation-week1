  # Operators Deep Dive

## Arithmetic Operators
Beyond standard arithmetic (`+`, `-`, `*`), Python provides operators essential for CP:

### Floor Division vs Normal Division
- `/` (Normal Division): Always returns a `float`. `10 / 2` is `5.0`.
- `//` (Floor Division): Divides and rounds *down* to the nearest whole integer.
  - Crucially, it rounds towards negative infinity.
  - Positive: `10 // 3` -> `3`
  - Negative: `-10 // 3` -> `-4` (not `-3`)

### Modulus Behavior with Negative Numbers
Modulus `%` calculates the remainder. In Python, the remainder takes the sign of the *denominator*.
- `10 % 3` -> `1`
- `-10 % 3` -> `2` (Because it calculates `-10 - (-10 // 3) * 3` -> `-10 - (-4 * 3)` -> `-10 + 12 = 2`)
- **Use Case**: To handle negative modulo in CP elegantly, use `(a % M + M) % M` to ensure positive wrap-around.

## Comparison Chaining
Python allows mathematical chaining of comparative operators.
```python
x = 5
print(1 < x < 10) # True
```
Internally evaluated as: `(1 < x) and (x < 10)`

## Logical Short-Circuiting
Python evaluates boolean expressions lazily from left to right.
- `A and B`: If `A` is `False`, Python immediately stops and returns `False` (doesn't evaluate `B`).
- `A or B`: If `A` is `True`, Python immediately stops and returns `True` (doesn't evaluate `B`).
- **Use case in CP**: `if index < len(arr) and arr[index] == target:` avoids `IndexError` because if `index` is out of bounds, the first part is `False`, and the second part is skipped entirely.

## Bitwise Operator Intuition
Bitwise operators work directly on the binary representation of integers. Time-efficient for competitive programming.

- `&` (AND): 1 if both bits are 1. Used to mask/check bits. (e.g., `x & 1 == 1` means `x` is odd).
- `|` (OR): 1 if either bit is 1. Used to turn on bits.
- `^` (XOR): 1 if bits are different. Used for toggling bits. (Property: `x ^ x = 0`).
- `~` (NOT): Inverts bits (two's complement). `~x = -x - 1`.
- `<<` (Left Shift): Shifts bits left. Equivalent to multiplying by $2^n$. (`x << 1` is `x * 2`).
- `>>` (Right Shift): Shifts bits right. Equivalent to floor division by $2^n$. (`x >> 1` is `x // 2`).

### Truth Tables
| A | B | A AND B | A OR B | A XOR B |
|---|---|---------|--------|---------|
| 0 | 0 |    0    |   0    |    0    |
| 0 | 1 |    0    |   1    |    1    |
| 1 | 0 |    0    |   1    |    1    |
| 1 | 1 |    1    |   1    |    0    |

### Edge Cases
- When using bitwise operators with comparisons, always use parentheses because bitwise operators have *lower precedence* than expected.
  - WRONG: `if x & 1 == 0:` (Evaluated as `x & (1 == 0)` -> `x & 0` -> `0`)
  - CORRECT: `if (x & 1) == 0:`
