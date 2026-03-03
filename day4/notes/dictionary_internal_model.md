===== FILE: cp-foundation-week1/day4/notes/dictionary_internal_model.md =====
# Understanding the Dictionary Internal Model

## Conceptual Hashing Basics
A standard List looks up data via an integer index: `arr[5]`.
A Dictionary looks up data via a Hash: `dict["Ambuj"]`.

Under the hood, Python passes the string `"Ambuj"` into a complex mathematical function (the hashing algorithm) which converts the text into a massive pseudo-random integer. Python then uses that integer as an exact memory array index to store and retrieve the value.

## Key Uniqueness
Because dictionaries map keys to strict memory locations, **Keys must be absolutely unique**.
If you execute:
```python
my_dict["score"] = 10
my_dict["score"] = 20
```
There is only one `"score"` slot in memory. It gets permanently overwritten to `20`.

## Object Hashability
Only **immutable** objects can be Dictionary Keys in Python.
- VALID Keys: `int`, `float`, `str`, `tuple`, `bool`
- INVALID Keys: `list`, `dict`, `set` (Because lists can mutate, their hash would violently change, breaking the lookup table).

## Collision Concept (High Level)
What happens if two totally different strings mathematically generate the *exact same* hash integer? This is a "Collision". Python internally resolves this using an algorithm called Open Addressing. As a competitive programmer, you don't need to manually handle this, but you must know collisions cause brief performance drops.

## Lookup Complexity
- **Time to find item in List without knowing index**: $O(N)$ (Must scan sequentially)
- **Time to find item in a Set or item by Key in Dictionary**: $O(1)$ (Average case).
Because $O(1)$ lookup is instant, dictionaries are the ultimate CP weapon for tracking seen values, caches, and graph edges.\n