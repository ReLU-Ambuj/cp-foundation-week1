# Problem 2: Divisors count
## Problem: 
Given $N$. Count how many divisors it has. O(sqrt N) required.
## Solution:
```python
def solve():
    n = int(input())
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
        i += 1
    print(count)
```\n