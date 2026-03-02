# Timed Repetition: Advanced Branching

## Instructions
1. Select the 5 hardest exercises from Day 2.
2. Re-solve them locally using your terminal, completely from memory.
3. **The 50% Time Constraint Rule**: If an exercise took you 10 minutes the first time, you must now complete it in **5 minutes** max.
4. Log every single failure in the table below. Do not lie to the matrix.

## Logical Weakness Identification Matrix
| Concept | Indicator of Failure | Study Action |
|---------|----------------------|--------------|
| Short-Circuiting | Crash on ZeroDivision despite an `and` guard | Re-read `logical_operators_and_short_circuiting.md` |
| Nesting | You used 3 levels of `if/else` | Re-read `nesting_and_control_flow_graphs.md` and practice Early Returns |
| CFG Traceability | Code doesn't compile / Missing Base Case | Draw the CFG on paper before typing |

## Error Tracking Table
| Problem Name | Previous Time | Target Time | Actual Time | Mistake Type | Fix Strategy |
|--------------|---------------|-------------|-------------|--------------|--------------|
| e.g., electricity_bill | 12m | 6m | 9m | Off-by-one | Used `<` instead of `<=` on tier bounds |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## Branch Complexity Scoring Rubric
- **1 point**: Flat `if/else`
- **2 points**: `if/elif/else` chain
- **3 points**: Combined logic `if A and B or (not C):`
- **5 points**: Deeply nested `if` inside `else` (Avoid unless absolutely mathematically required).
