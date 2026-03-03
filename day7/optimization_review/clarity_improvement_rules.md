# Clarity Improvement Rules

## 1. Naming Conventions
- Variables represent *Data*: `user_age`, `matrix_grid`.
- Functions represent *Action*: `calculate_age()`, `parse_matrix()`.
- Booleans represent *State*: `is_valid`, `has_passed`.

## 2. Avoid Magic Numbers
If `86400` is in your code, nobody knows what it is.
```python
SECONDS_IN_DAY = 86400
time = days * SECONDS_IN_DAY
```

## 3. Single Responsibility Per Function
A function named `validate_and_save_and_print_user()` is breaking architecture. Break it into three decoupled functions directed by a main controller.

## 4. Comment Only When Needed
Do not comment *what* the code is doing (Python is readable enough). Comment *why* you did it.
```python
# Bad: Adding 1 to i
i += 1

# Good: Shift buffer index by 1 to skip the trailing whitespace edge case
i += 1 
```\n