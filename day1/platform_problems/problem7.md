# Problem 7: Temperature Converter Array
## Problem Statement
Given a list of 3 temperatures in Celsius space-separated. Print them in Fahrenheit rounded to 2 decimal places.

## Clean Solution Code
```python
def solve():
    temps = list(map(float, input().split()))
    for c in temps:
        f = (c * 9/5) + 32
        print(f"{f:.2f}", end=" ")
    print()
```
