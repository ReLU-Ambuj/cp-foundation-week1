# Problem 1: Summing a Range
## Problem: 
Given $A, B$. Compute sum of all integers between $A$ and $B$ (inclusive).
$A$ might be strictly larger than $B$.
## Solution:
```python
def solve():
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    print(sum(range(a, b + 1)))
```\n