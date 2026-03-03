# Mistake Classification Matrix

Use this to formally identify *why* you failed a problem today.

## Categories

- [ ] **Logic Error**: The mathematical/algorithmic approach was fundamentally wrong.
- [ ] **Off-by-one**: Failed boundary conditions (`<` instead of `<=`).
- [ ] **Incorrect Condition Order**: `if/elif` executed in wrong priority.
- [ ] **Missed Edge Case**: Code handles 99%, but crashes on $N=0$ or negatives.
- [ ] **Inefficient Loop**: Solution works, but is $O(N^2)$ and exceeds time limits.
- [ ] **Variable Misuse**: Shadowing loops (`for i` inside `for i`), or mutating global state.
- [ ] **Wrong Type Conversion**: Math crashed due to `str` vs `int` or division `/` vs `//`.
- [ ] **Time Pressure Panic**: You knew how to do it, but froze or deleted working code.
- [ ] **Syntax Oversight**: Forgetting a colon `:`, unaligned indents, or misspelled variables.\n