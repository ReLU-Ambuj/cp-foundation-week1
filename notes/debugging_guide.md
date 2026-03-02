# Debugging Guide

## How to Read a Traceback
A "traceback" (or stack trace) is Python's way of explicitly telling you the history of an error.
**Read it from the BOTTOM UP.**
The last line tells you the exact error type and the descriptive message.
The line immediately above it tells you the file and line number where the code crashed.

## Stack Trace Anatomy
```
Traceback (most recent call last):                  <-- Declaration of stack trace
  File "script.py", line 10, in <module>            <-- Entry point of crash
    main()
  File "script.py", line 6, in main                 <-- The function called
    calculate(x)
  File "script.py", line 2, in calculate            <-- The exact line of execution
    return 10 / y
ZeroDivisionError: division by zero                 <-- THE ACTUAL ERROR TO FIX
```

## Common Beginner Errors
1. **`SyntaxError`**: You forgot a colon `:`, parenthesis `()`, or wrote invalid Python. (Evaluated before the code even runs).
2. **`IndentationError`**: Your spaces/tabs are misaligned.
3. **`TypeError`**: You tried to perform an operation on incompatible types (e.g., `5 + "5"`, or iterating over an `int`).
4. **`ValueError`**: You passed the right type but inappropriate value (e.g., `int("abc")`).
5. **`NameError`**: You misspelled a variable name or used a variable before defining it.

## Step-by-Step Debugging Workflow
1. **Breathe**. Do not randomly change code.
2. Read the very last line of the traceback.
3. Check the exact line number mentioned just above the error.
4. If the error isn't obvious on that line, check the line immediately proceeding it (sometimes a missing parenthesis on line 5 causes a SyntaxError on line 6).
5. Mentally walk through the variable states, or use an IDE Debugger or `print()` statements to verify assumed values.

## How to Intentionally Break Code to Learn
Do not fear stack traces. Cause them on purpose.
- Type `10 / 0` to see a ZeroDivisionError.
- Try `int("hello")` to observe a ValueError.
The faster you recognize an error shape, the faster your competitive programming resolution times become.

## Mental Debugging Checklist
- [ ] Are my variables tracking the types I expect?
- [ ] Did I forget to read all inputs from the test case?
- [ ] Is my loop terminating?
- [ ] Am I dividing by variables that might be zero?
- [ ] Am I mutating an array while iterating over it?
