# Problem: TypeError when multiplying strings
# Expected Error: TypeError: can't multiply sequence by non-int of type 'float'

def multiply_string(s: str, multiplier: float) -> str:
    # BUG: Strings can only be multiplied by integers in Python!
    # Fix: return s * int(multiplier)
    return s * multiplier

if __name__ == "__main__":
    try:
        multiply_string("Hello", 2.5)
    except Exception as e:
        print("Traceback Example:")
        print(f"TypeError: {e}")
