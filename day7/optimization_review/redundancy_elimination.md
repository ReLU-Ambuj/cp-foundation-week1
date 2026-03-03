# Redundancy Elimination

## Removing Repeated Conditions
If you check `if x > 0` 4 times in a function, extract the logic.

## Extracting Helper Functions (DRY Principle)
Don't Repeat Yourself.
If you reverse an array in two different `if/else` execution paths, abstract `reverse_array()` entirely outside the flow, or execute it after the branches merge.

## Simplifying Nested Logic
Never write:
```python
if a == True:
    if b == True:
        if c == True:
            return 1
```
Use boolean algebra:
```python
if a and b and c:
    return 1
```

## Replacing Repeated Loops
If you iterate over the same array twice sequentially $O(2N)$:
```python
# Bad
for item in arr: total += item
for item in arr: mult *= item
```

Calculate them in a single pass $O(N)$ unless it strictly violates single-responsibility logic in a harmful way.
```python
# Good
for item in arr:
    total += item
    mult *= item
```\n