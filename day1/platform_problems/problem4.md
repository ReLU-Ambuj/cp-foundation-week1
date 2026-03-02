# Problem 4: Character Type Classification
## Problem Statement
Given a single English alphabet character, output "Vowel" if it is A, E, I, O, U. Otherwise output "Consonant". Case-insensitive.

## Clean Solution Code
```python
def solve():
    char = input().strip().lower()
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
```
