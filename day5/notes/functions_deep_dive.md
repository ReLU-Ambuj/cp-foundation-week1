# Functions Deep Dive

## What is a Function at Runtime
A function is not just a block of text; it is an isolated memory environment created "on demand." When you call a function, the Python interpreter dynamically allocates a secure Memory Frame strictly for that function's execution.

## Call Stack Explanation
The Call Stack is a LIFO (Last In, First Out) data structure tracking where the program is.
If `main()` calls `solve()`, the execution of `main()` freezes. `solve()` is pushed to the top of the stack and takes absolute control of the CPU. Once `solve()` returns a value, its Memory Frame is destroyed, and CPU control falls back down to `main()`.

## Function Memory Frame
Every local variable you create inside `solve()` lives inside its isolated Memory Frame. The moment the function hits a `return` statement, that frame is violently purged from RAM. This is why you cannot access a function's counter variable from outside the function.

## Parameter Passing (Call by Object Reference)
Python passes arguments by Object Reference.
- **Immutable Types** (Int, String, Tuple): Passed by value-like behavior. Modifying them inside the function creates a new local copy. The outside variable is completely safe.
- **Mutable Types** (List, Dictionary, Set): Passed by reference. If you do `arr.append(5)` inside a function, the original list in the caller's scope is permanently modified. **This is a dangerous side-effect.**

## Deterministic Behavior
A deterministic function always produces the exact same output for a given input, regardless of when or how many times it is called.

## Side Effects vs Pure Functions
- **Impure (Side-Effect)**: A function that mutates a global list, writes to a file, or modifies arguments directly without returning anything.
- **Pure Function**: Maps parameters to a return value. Period. It touches absolutely nothing else in the universe. Pure functions are the holy grail of CP reliability.

## Diagram Example

```text
CPU Control Flow:

main()  [Paused]
  ↓
is_prime(17) [Active]
  |
  |-- i = 2
  |-- i * i <= 17 (True)
  |-- return True
  ↓
Frame is destroyed, Control returns to main()
```
