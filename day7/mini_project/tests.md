# Mini Project Test Matrix

Run `python3 main.py` and execute the following manual tests to ensure system stability.

## Test Case 1: The Input Handlers (Robustness)
- At the main menu, type `hello`. (Should print Error: Please enter a valid integer).
- Type `10`. (Should print Error: Select an option between 1 and 5).
- Type `-1`. (Should throw the bounded error).

## Test Case 2: Number Utils Edge Cases
- Select `1` (Number Ops).
- Select `1` (Factorial).
- Enter `-5`. (Should gracefully return -1 as per `number_utils.py` bounds).
- Select LCM. Enter `0` and `5`. (Should return 0, no math error).

## Test Case 3: Prime Tool Large Scale
- Select `2` (Prime Engine).
- Check Single Prime: `1000000007` (Should return True almost instantly $O(\sqrt N)$).
- Generate Primes up to `100` (Should print the list and say Total count: 25).

## Test Case 4: The Calculator Crises
- Select `3` (Calculator).
- Type `1 + 2 * 3` (Wait, this is invalid format by our parser). Will throw Invalid Format error (needs exactly 3 items split by space).
- Type `5 / 0` (Will trigger the custom ValueError("Division by zero") and handle it gracefully by re-prompting).
- Type `exit` (Returns safely to Main Menu).

## Test Case 5: The Visualizer
- Select `4` (Pattern Generator).
- Select `1` (Pyramid).
- Enter `0` or `-1` (Should be blocked by the `check_positive` validation function inside Input Handlers).
- Enter `5`. Should clearly print a perfectly centered 5-row star pyramid.
