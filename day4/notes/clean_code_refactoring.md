# Clean Code and Refactoring Discipline

## Variable Naming Standards
In Day 1, single letters were acceptable. In Day 4 matrix frequency logic, single letters cause cognitive collapse.
**Banned Names:** `x`, `y`, `val`, `temp1`, `temp2`
**Mandatory Names:** `char_freq`, `max_count`, `current_row`, `target_substring`
*Exception: Loop iterators `i`, `j`, `r` (row), `c` (col) are standard.*

## Removing Redundant Loops
If you are iterating over the string to find vowels, and then iterating over the string AGAIN to find consonants—you are failing the $O(N)$ efficiency test. Combine state tracking into a single pass.

## Avoiding Repeated Logic
If you copy and paste an `if/else` block and change only one variable, you need to extract the logic. Use early returns or mathematical mapping to avoid the repetition.

## Comment Quality Rules
**Bad:** `# Adding 1 to counter` (Self-evident code)
**Good:** `# Resolves edge case where string ends dynamically triggering OBOE` (Explains the *Why*, not the *What*)

## Readability Scoring Checklist
Before submitting a script today, judge it:
- [ ] Is my variable nomenclature descriptive?
- [ ] Did I use `get()` instead of a massive `if char not in dict` block?
- [ ] Did I flatten all my loops using Guard Clauses where possible?
- [ ] Are my matrix nested loops strictly localized to geometric layout without unrelated logic leaking in?\n