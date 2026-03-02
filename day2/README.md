# Day 2: Advanced Conditional Logic

## Day Objective
To achieve absolute supremacy over branching logic, boolean algebra, and Control Flow Graphs (CFGs). By the end of this day, you will evaluate complex nested conditions deterministicly and write competitive-programming-ready conditional structures without hesitation.

## Hour-by-Hour Breakdown
- **Hour 0–2**: Deep Theory (CFGs, Short-Circuiting, De Morgan's Laws)
- **Hour 2–5**: Ex 1-10 (Levels 1-3: Linear to Nested Branching)
- **Hour 5–8**: Ex 11-20 (Levels 4-5: Multiple Conditions to Decision Trees)
- **Hour 8–13**: Platform Problems (15 specific CP-style challenges)
- **Hour 13–15**: Timed Repetition & Edge Case Analysis

## Mental Model of Branching
Think of standard code as a train on a single track. Conditionals are railroad switches. The CPU must evaluate the condition (the boolean expression) before it knows which track to send the execution down. In CP, slow or redundant evaluations cost time. Unhandled edge cases derail the train entirely.

## Common Logical Traps
1. **Redundant Conditions**: Writing `elif x > 5:` when the previous `if x <= 5:` already handles the inverse.
2. **Equality vs Identity**: Using `is` when you mean `==`.
3. **Floating Point Branching**: Checking `if float_a == float_b:` instead of using an epsilon `abs(a - b) < 1e-9`.
4. **Missing the Base Case**: Forgetting the `else` trapdoor for invalid domain inputs.

## Strict Training Rules
- No IDE autocomplete or AI assistance.
- Commit to GitHub after every 3 exercises to enforce muscle memory of the Git workflow.
- Write the CFG mentally before typing the `if` statement.
