# While Loop Design Patterns

## 1. Sentinel Loops
A loop that runs continuously reading data until a specific "Sentinel Value" (like `None`, `-1`, or `"EOF"`) is encountered.
```python
user_input = int(input())
while user_input != -1:  # -1 is the sentinel
    process(user_input)
    user_input = int(input())
```

## 2. Input Validation Loops
Trapping a user (or automated input buffer) until constraints are satisfied.
```python
n = int(input())
while n <= 0:
    n = int(input("Must be positive. Try again: "))
```

## 3. Accumulator Pattern
Maintaining a running total or aggregation dynamically over an unknown iteration count.
```python
total_sum = 0
while condition:
    total_sum += current_value
```

## 4. Counter Pattern
A custom implementation of `range()`. Usually used when `step` is highly dynamic or non-linear.
```python
count = 0 
while count < N:
    if specific_condition: count += 5
    else: count += 1
```

## 5. Infinite Loop with Break Pattern
The most common CP structural pattern for complex condition logic. Force the loop continuously, then break internally using guard clauses.
```python
while True:
    state = fetch_state()
    if not state.is_valid:
        break # Exit immediately
    process(state)
```

## Termination Proof Mindset
Before writing `while`, manually prove to yourself that the loop condition *will eventually* become false. If your `while` depends on dividing `N` by `2`, know that due to integer division `1 // 2` -> `0`, which provides a clean base-case termination.\n