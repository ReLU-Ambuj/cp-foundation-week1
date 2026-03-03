===== FILE: cp-foundation-week1/day4/notes/string_iteration_fundamentals.md =====
# String Iteration Fundamentals

## The String as an Immutable Sequence
In Python, strings are immutable. You cannot do `s[0] = 'H'` on the string `"hello"`. Any transformation operation (replacing characters, changing cases) strictly creates a brand-new string in memory. String concatenation (`s += "a"`) inside a loop is $O(N^2)$ overall because it copies the *entire existing string* on every iteration.

## Character Traversal

### Direct Iteration (The Pythonic Way)
Use this when you only need the value of the characters, not their positions.
```python
for char in "hello":
    print(char)
```

### Index-Based Iteration (The CP Way)
Use this when you need to compare the current character to adjacent characters or jump around the string.
```python
s = "hello"
for i in range(len(s)):
    print(s[i])
```

## `ord()` and ASCII Interaction
Characters are just numeric bytes under the hood. The `ord()` function returns the integer ASCII/Unicode value of a character.
- `A` = 65, `Z` = 90
- `a` = 97, `z` = 122
- `0` = 48, `9` = 57

```python
# Shifting a character forward by 1 (e.g., 'a' -> 'b')
new_char = chr(ord('a') + 1) 
```

### ASCII Diagram Example
```text
Index:    0    1    2    3
String:  'a'  'b'  'c'  'd'
ASCII:   97   98   99   100
```

## Case Normalization
In CP, a string might be "AbCdE". To count frequencies reliably without writing complex guard clauses, strictly normalize the string up front.
```python
s = s.lower() # or s.upper()
```

## String Slicing Mechanics
Slicing `s[start:stop:step]` returns a new sub-sequence in $O(K)$ time where $K$ is the slice length.
- `s[::-1]` mathematically reverses a string in $O(N)$ time.
- `s[2:5]` extracts indices 2, 3, and 4.

## Common Beginner Mistakes
1. **IndexError**: Checking `s[i+1]` without bounding the looping range `len(s) - 1`.
2. **String Mutable Assumption**: Trying to mutate an index directly instead of building a `new_string` or using a `list(s)`.
3. **Wasted $O(N^2)$ Memory**: Using `s = s + char` inside a $10^5$ iteration loop instead of `.join()`.
