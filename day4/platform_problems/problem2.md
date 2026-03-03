# Problem 2: Anagram Permutations
## Problem
Given Strings $A, B$. Are they anagrams? Space complexity must be $O(K)$.
## Solution
```python
def solve():
    a, b = input().split()
    if len(a) != len(b): return print("NO")
    freq = {}
    for char in a: freq[char] = freq.get(char, 0) + 1
    for char in b: freq[char] = freq.get(char, 0) - 1
    print("YES" if all(v == 0 for v in freq.values()) else "NO")
```\n