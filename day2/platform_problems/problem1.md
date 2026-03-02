# Problem 1: The Three Gates
## Problem Statement
You are given three integers $A, B, C$. If $A$ is true (nonzero), output $A$. Otherwise, if $B$ is true, output $B$. Otherwise, output $C$. Solve using only `or`.

## Clean Solution Code
```python
def solve():
    a, b, c = map(int, input().split())
    # Python `or` returns the first truthy value!
    print(a or b or c)
```\n