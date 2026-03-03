# Problem 4: Maximum Character Frequency
## Problem
Given $S$. Output the character that appears the most. If tied, output the one that appears first alphabetically.
## Solution
```python
def solve():
    s = input()
    freq = {}
    for c in s: freq[c] = freq.get(c, 0) + 1
    
    max_c, max_count = 'z', 0
    for c, count in freq.items():
        if count > max_count or (count == max_count and c < max_c):
            max_c, max_count = c, count
    print(max_c)
```\n