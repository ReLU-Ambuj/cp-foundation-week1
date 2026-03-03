# Problem 11: Largest Prime Factor
## Problem
Given N. Find the largest prime factor of N. O(sqrt N).

## Format
- **Input**: N
- **Output**: Prime Integer
- **Constraints**: N <= 10^9

## Sample
**In:**
```text
15
```
**Out:**
```text
5
```

## Checklist before coding
- **Edge Cases Considered**: N is prime.
- **Target Complexity**: O(sqrt N)

> **Hint**: Repeatedly divide N by `i` starting from 2.\n