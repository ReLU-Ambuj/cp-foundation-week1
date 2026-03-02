# Day 1 Theory: Memory, Types, and I/O Models

## Variables from a Memory Model Perspective
In Python, variables are **not containers**; they are **labels or references** pointing to objects in memory.
When you write `x = 10`, Python:
1. Creates an integer object with the value `10` in Random Access Memory (RAM).
2. Assigns the memory address of that object to the label `x`.

If you later write `y = x`, both `x` and `y` point to the *exact same object* in memory.

## Python Dynamic Typing Internal Mechanics
Dynamic typing means types are bound to the **object**, not the variable name.
- When `x = 5`, Python notes the object is of type `int`.
- When `x = "Hello"`, Python creates a new `str` object and redirects `x` to it. The old `int` object is garbage-collected if no other references exist.

### Core Primitives
- **`int`**: Arbitrary-precision integers. Python automatically handles incredibly large numbers (useful for CP without risking overflow natively).
- **`float`**: C-style `double` (IEEE 754 format). Occupies 8 bytes (64 bits). Always remember: floating-point math is technically an approximation.
- **`bool`**: A subclass of `int`. `True` evaluates to `1`, `False` evaluates to `0`.
- **`str`**: An immutable array of Unicode characters.

## Immutable vs Mutable Concept (Brief Intro)
- **Immutable**: Once created in RAM, their state cannot change (`int`, `float`, `bool`, `str`, `tuple`). If you modify a string, you are actually creating a completely *new* string in memory.
- **Mutable**: Objects that can be modified in place (`list`, `dict`, `set`).

## Input/Output Mechanics
### `input()`
The `input()` function pauses execution, reads bytes from standard input (`stdin`) until a newline character `\\n` is encountered, and returns it as a string.
- *Crucial*: `input()` ALWAYS returns a string.

### `print()`
The `print()` function writes to standard output (`stdout`). Internally, it calls the `__str__()` method of the objects passed to it.
Using `sys.stdout.write()` instead of `print()` is slightly faster in CP because `print()` adds a newline and space overhead.

## Operator Precedence
Precedence determines the order of evaluation (PEMDAS/BODMAS applies, but Python has more operators).
1. `()` Parentheses
2. `**` Exponentiation
3. `+x`, `-x` Unary plus/minus
4. `*`, `/`, `//`, `%` Multiplication, Division, Floor division, Modulo
5. `+`, `-` Addition, Subtraction
6. `==`, `!=`, `>`, `<`, `>=`, `<=` Comparisons
7. `not` Logical NOT
8. `and` Logical AND
9. `or` Logical OR

## Common Beginner Mistakes
1. Forgetting to cast `input()` to `int` leading to `TypeError` on addition.
2. Assuming `int / int` returns an `int` (it returns a `float` in Python 3).
3. Using `=` (assignment) instead of `==` (comparison).

## Mental Models for Competitive Programming
1. **The Constraints Model**: Always look at the constraints before writing code. If constraints say $N \le 10^5$, an $O(N^2)$ brute-force solution will fail (Time Limit Exceeded).
2. **The Edge Case Habit**: Before submitting, mechanically ask: "What if N is 0? What if N is 1? What if all numbers are negative?"
