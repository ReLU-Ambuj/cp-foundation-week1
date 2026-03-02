# Problem 3: Max of Three Variations
## Problem Statement
Given three integers $A$, $B$, $C$, output exactly the largest one without using the built-in `max()` function.

## Clean Solution Code
```python
def solve():
    a, b, c = map(int, input().split())
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print(largest)

if __name__ == '__main__':
    solve()
```
