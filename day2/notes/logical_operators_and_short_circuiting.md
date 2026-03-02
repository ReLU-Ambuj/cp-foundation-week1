# Logical Operators and Short-Circuiting

## `and`, `or`, `not`
These are the fundamental logical binders in Python.
- `and`: Both operands must evaluate to True.
- `or`: At least one operand must evaluate to True.
- `not`: Inverts the boolean value.

## Evaluation Order and Precedence
Logical operators evaluate strictly from **Left to Right**.
Precedence:
1. `not` (Highest)
2. `and`
3. `or` (Lowest)

Expression: `True or False and not True`
Evaluates as:
1. `not True` -> `False`
2. `False and False` -> `False`
3. `True or False` -> `True`

*Rule of Thumb for CP: Always use parentheses to explicitly define intend, even if precedence rules cover it. Ex: `True or (False and (not True))`.*

## The Short-Circuit Mechanism
Python utilizes lazy evaluation. It stops evaluating a logical expression the absolute millisecond the final outcome is guaranteed.

### AND Short-Circuiting
If the left operand of `and` is `False`, the entire expression must be `False`. Python **will not evaluate** the right operand.
```python
if a != 0 and (b / a) > 5:
    pass
```
*Why it matters:* This acts as a **Guard Condition**. If `a == 0`, the left side is `False`. Python short-circuits. `(b / a)` is never executed, preventing a literal `ZeroDivisionError` crash.

### OR Short-Circuiting
If the left operand of `or` is `True`, the entire expression must be `True`. Python **will not evaluate** the right operand.
```python
if is_admin or fetch_permissions_from_db():
    pass
```
*Why it matters:* Performance. If the user is an admin, it skips the expensive database call entirely.

## De Morgan's Laws
Crucial for simplifying complex, unreadable negative conditions in CP.

1. `not (A and B)` is mathematically identical to `(not A) or (not B)`
2. `not (A or B)` is mathematically identical to `(not A) and (not B)`

### Complex Simplification Example
**Bad (Mental overhead is too high):**
```python
if not (x > 10 and y <= 20):
```
**Good (Applying De Morgan's):**
```python
if x <= 10 or y > 20:
```
This inverted logic drastically reduces the chance of edge-case bugs during high-pressure contests.
