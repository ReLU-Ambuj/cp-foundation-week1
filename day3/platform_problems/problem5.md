# Problem 5: Collatz Conjecture
## Problem:
Given $N$. If even, $N = N/2$. If odd, $N = 3N+1$. How many steps to reach 1?
## Solution:
```python
def solve():
    n = int(input())
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(steps)
```\n