# Before and After Refactoring Optimization

## Example 1: The Spaghetti Anagram Check

### Before
```python
def anag(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        d1 = {}
        for c in s1:
            if c in d1:
                d1[c] = d1[c] + 1
            else:
                d1[c] = 1
        d2 = {}
        for c in s2:
            if c in d2:
                d2[c] = d2[c] + 1
            else:
                d2[c] = 1
        if d1 == d2:
            return True
        else:
            return False
```

### After (Optimized & Pythonic)
```python
def build_char_map(s: str) -> dict:
    f_map = {}
    for char in s:
        f_map[char] = f_map.get(char, 0) + 1
    return f_map

def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    return build_char_map(s1) == build_char_map(s2)
```

**Why it's better:**
1. Separated the dictionary building into a pure helper function (`build_char_map`).
2. Eliminated DRY violation (building dicts manually twice).
3. Used dictionary `.get()` to avoid `if/else` checks.
4. Directly evaluated the return statement `return d1 == d2` instead of `if d1 == d2: return True`.\n