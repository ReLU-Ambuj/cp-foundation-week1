# Edge Case Engineering

## Boundary Value Analysis
An edge case (or boundary condition) is a problem or situation that occurs only at the extreme operating parameter of a system. Competitive programming heavily tests boundaries because they expose logical holes.

In a conditional statement like `if age > 18:`, the boundaries are `17`, `18`, and `19`.
* The most common mistake is off-by-one errors (using `>` instead of `>=`).

## Off-by-One Errors
This occurs when an iteration or limit is evaluated one time too many or too few.
```python
# Intended: Print numbers 1 through 10
# Bug: Range stops BEFORE the second argument
for i in range(1, 10): 
    pass
# Fix: range(1, 11)
```

## Invalid Input Handling
Always assume the user (or the CP judge) will pass adversarial input if constraints allow it.
- **Null / Empty states**: `""`, `[]`, `None`, `0`
- **Negative values**: Lengths, ages, quantities.
- **Maximum limits**: Values causing integer overflow in other languages (Python auto-handles arbitrary precision, but algorithmic time limits still apply).

## Defensive Branching
Defensive branching means intentionally writing `else` blocks to catch states that "should be impossible." This is crucial during debugging.

```python
if color == "red":
    return "#FF0000"
elif color == "blue":
    return "#0000FF"
else:
    # Do not silently fail. Throw a loud error.
    raise ValueError(f"CRITICAL: Unhandled color state: {color}")
```

## Domain Validation Patterns
Validate domain logic up-front using early returns before doing any calculations.
```python
def calculate_discount(price, age):
    # 1. Validate Input Domain
    if price < 0 or age < 0:
        raise ValueError("Inputs cannot be negative")
    
    # 2. Process Valid Domain
    if age > 65:
        return price * 0.9
    return price
```

## How to Think Adversarially
When reading a CP problem, ask:
1. "What happens if $N=0$?"
2. "What happens if the array is already sorted?"
3. "What happens if all array elements are identical?"
4. "Can the denominator ever evaluate to zero?"
5. "What if the first `if` matches, but the second one *also* matches later? Did I need `elif`?"
