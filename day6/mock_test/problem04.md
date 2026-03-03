# Problem 04: The Missing Elements

## Setup
Given an array of N integers containing values from 1 to N+2. Exactly two numbers are missing. Find them in O(N).

## Format
- **Input**: Array length N. Then array.
- **Output**: Two missing numbers sorted ascending.
- **Constraints**: N <= 10^5. Do not use sorting. Use frequency maps.
- **Difficulty**: 3/5

## Example
**In:**
```text
3\n 1 4 5
```
**Out:**
```text
2 3
```

## Checklist
- Edge Cases: Missing 1 and N+2 (the extreme edges).
- Required Complexity: O(N)
