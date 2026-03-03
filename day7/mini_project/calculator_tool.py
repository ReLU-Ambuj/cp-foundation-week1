def add(a: float, b: float) -> float: return a + b
def subtract(a: float, b: float) -> float: return a - b
def multiply(a: float, b: float) -> float: return a * b
def divide(a: float, b: float) -> float:
    if b == 0: raise ValueError("Division by zero")
    return a / b

def run_calculator():
    """Executes floating point calculator loops with guard clauses."""
    print("\\n--- Simple Floating Point Calculator ---")
    while True:
        try:
            expression = input("Enter expression 'A + B' or 'exit': ")
            if expression.lower() == 'exit': break
            
            parts = expression.split()
            if len(parts) != 3:
                print("Error: Invalid format. Spaces required (e.g., '5 * 4').")
                continue
                
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            
            if op == '+': print(f"Result: {add(a, b)}")
            elif op == '-': print(f"Result: {subtract(a, b)}")
            elif op == '*': print(f"Result: {multiply(a, b)}")
            elif op == '/': print(f"Result: {divide(a, b)}")
            else: print("Error: Unknown operator.")
                
        except ValueError as e:
            # Handles string conversion errors and divide by zero
            print(f"Validation Error: {e}")
