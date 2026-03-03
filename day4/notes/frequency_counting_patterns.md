===== FILE: cp-foundation-week1/day4/notes/frequency_counting_patterns.md =====
# Frequency Counting Patterns

## Counting Using a Dictionary (Hash Map)
Frequencies count **how many times** specific discrete items appear.
The core CP pattern involves iterating through an iterable and updating a dictionary.

```python
# The Standard Pattern
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
```

## The `.get()` Method
The above verbose `if/else` can be radically compressed using dictionary's `.get(key, default)`.
```python
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```
*If `char` does NOT exist, `get()` returns the default `0`, then adds `1`. If it DOES exist, it grabs the current count and adds `1`.*

## `defaultdict` Concept (Brief)
Python's `collections.defaultdict` makes this completely automatic by removing the need to specify the default `0` on every assignment.
```python
from collections import defaultdict
freq = defaultdict(int) # defaults to 0
for char in s:
    freq[char] += 1
```

## Frequency Array vs Dictionary Tradeoff
If you are strictly guaranteed the input only contains English lowercase letters (`a-z`), you don't actually need the overhead of a Python dictionary. Use an array of size 26.
```python
freq = [0] * 26
for char in s:
    # Character 'a' -> index 0. 'b' -> index 1.
    idx = ord(char) - ord('a') 
    freq[idx] += 1
```
- **Dictionary**: Safe for *any* character (Unicode, spaces, emojis). Slightly higher memory/hashing overhead.
- **Freq Array**: Absolute maximum speed $O(1)$ memory mapping, strictly constrained to predictable sequential ASCII inputs.

## Two-Pass vs One-Pass Counting
- **Two-Pass**: Iterate array once to build the frequency map. Iterate a second time to use that map (e.g., finding the first non-repeating character). $O(2N) = O(N)$.
- **One-Pass**: Maintaining the target logic *while* building the frequency map. Requires heavy conditional tracking.

## Complexity
- **Time Complexity**: $O(N)$ to build the frequency dictionary.
- **Space Complexity**: $O(K)$, where $K$ is the number of **unique** characters in the string. For lowercase english letters, Space is strictly $O(1)$ because $K \le 26$.
