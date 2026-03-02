# Day 3: Looping Constructs & Iteration Mastery

## Day Objective
To develop a relentless "loop reflex"—the ability to instantly translate mathematical sequences, coordinate grids, and repetitive tasks into optimal $O(N)$ or $O(N^2)$ code without hesitation. You will master `for` loops, `while` loops, and the strict mathematical bounds of iteration.

## Loop Mental Model
A loop is an engine. It requires:
1. **Initial State (Fuel)**: Where does the counting begin?
2. **Condition (Engine Check)**: Should another cycle run?
3. **Body (Pistons)**: The actual work performed per cycle.
4. **State Update (Exhaust)**: Moving the counter or state forward.
If the State Update fails to bridge the gap toward the Condition, the engine explodes into an infinite loop.

## Hour-by-Hour Execution Plan
- **Hour 0–2**: Theory (Invariants, Range, While Patterns) 
- **Hour 2–5**: Drills (Numbers & Sequences: `print_1_to_n.py` to `binary_to_decimal.py`)
- **Hour 5–8**: Drills (Patterns: `pattern_set_01.py` to `pascal_triangle.py`)
- **Hour 8–11**: Platform Problems (15 CP-style looping challenges)
- **Hour 11–13**: Debugging & Error Analysis
- **Hour 13–15**: Speed Coding & Reflex Training

## Loop Invariant Explanation
A loop invariant is a theoretical property of your program state that is guaranteed to be **True** before the loop, **True** during every single execution cycle, and **True** after the loop terminates. Identifying the invariant is the secret to mathematically proving a loop will not fail.

## Common Infinite Loop Causes
1. **Missing State Update**: Forgetting `i += 1` inside a `while` loop.
2. **Condition Drift**: Updating the state in the *wrong direction* (e.g., `i -= 1` when waiting for `i > 10`).
3. **Shadowing Modifiers**: Accidentally overwriting your iterator variable inside the loop body.

## Strict Speed-Coding Rules
- Zero autocomplete.
- Commit to Git after every 4 completed drills.
- If you use brute-force $O(N^2)$ when math allows $O(N)$ or $O(1)$, the drill counts as a failure.
