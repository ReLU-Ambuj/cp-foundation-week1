# Problem 02: Prime Product Checker

## Setup
Given N. Is N the product of exactly two prime numbers? (e.g. 15 = 3 * 5). Pure function.

## Format
- **Input**: N
- **Output**: Boolean
- **Constraints**: N <= 10^8
- **Difficulty**: 2/5

## Example
**In:**
```text
15
```
**Out:**
```text
True
```

## Checklist
- Edge Cases: N is prime, N is 1. N is square of a prime (e.g. 9 = 3*3).
- Required Complexity: O(sqrt N)
