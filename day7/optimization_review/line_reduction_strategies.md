# Line Reduction Strategies (Pythonic)

## Conditional Expressions (Ternary)
**4 Lines:**
```python
if x > 5:
    res = "High"
else:
    res = "Low"
```
**1 Line:**
```python
res = "High" if x > 5 else "Low"
```

## Built-In Function Usage
Do not write 6 lines to find a maximum if you aren't forced to abstract it.
Use `max(arr)`, `min(arr)`, `sum(arr)`.

## Early Return Pattern (Guard Clauses)
End execution immediately if bad data is found. It prevents massive indentation.
**Bad:**
```python
def calc(x):
    if x > 0:
        # 50 lines of code here
        return result
    else:
        return -1
```

**Good:**
```python
def calc(x):
    if x <= 0: return -1
    # 50 lines of code here
    return result
```\n