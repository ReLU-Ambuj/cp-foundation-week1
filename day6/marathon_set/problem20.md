# Problem 20: Perfect Square Fast
## Problem
Is N a perfect square? No floating point math allowed (`** 0.5` is banned).

## Format
- **Input**: N
- **Output**: YES / NO
- **Constraints**: N <= 10^9

## Sample
**In:**
```text
16
```
**Out:**
```text
YES
```

## Checklist before coding
- **Edge Cases Considered**: 0, 1, negative.
- **Target Complexity**: O(sqrt N)

> **Hint**: Iterate `i=1`. While `i*i <= n`.\n