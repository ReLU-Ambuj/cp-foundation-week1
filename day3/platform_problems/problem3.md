# Problem 3: Next Prime
## Problem:
Given $N$. Find the smallest prime strictly greater than $N$.
## Solution:
```python
def is_prime(k):
    if k <= 1: return False
    i = 2
    while i * i <= k:
        if k % i == 0: return False
        i += 1
    return True

def solve():
    n = int(input()) + 1
    while not is_prime(n):
        n += 1
    print(n)
```\n