===== FILE: cp-foundation-week1/day4/notes/string_edge_cases.md =====
# String Edge Cases

## Defensive Branching in String Logic
Strings coming from competitive programming inputs or raw files are notoriously dirty. You must structurally handle input anomalies before running your main loop.

### 1. The Empty String
`s = ""`
If you use index traversal (`s[0]`), an empty string immediately triggers an `IndexError`.
*Fix: Early Return Guard*
```python
if not s: # Pythonic check for empty string
    return ""
```

### 2. The Single Character
`s = "A"`
If your logic depends on looking ahead (`s[i] == s[i+1]`), a length 1 string will crash.
*Fix: Length conditional checks*
```python
if len(s) == 1:
    return s
```

### 3. All Identical Characters
`s = "AAAAAA"`
Certain compression or sliding window algorithms often fail to record the final compression block because the state never transitions into a "new" character.
*Fix: Always force terminal logic execution after the loop fully completes.*

### 4. Whitespace Handling
Tabs `\t`, Newlines `\n`, and standard spaces `. `
If counting words, multiple consecutive spaces will create empty string elements if split incorrectly.
*Fix: `s.split()` inherently handles arbitrary whitespace. `s.split(" ")` strictly splits on single spaces, causing bugs.*

### 5. Unicode Considerations
Not all characters have a length of 1 visual byte. However, for 99% of CP algorithms, assume ASCII standard sequential bytes.

### 6. Case Sensitivity
`"apple" != "Apple"`
If a problem dictionary logic requires case insensitivity, strictly execute `s = s.lower()` on line 1 before traversing anything.\n