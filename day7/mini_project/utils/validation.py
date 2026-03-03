def check_positive(n: int) -> bool:
    """Returns True if strictly positive."""
    return n > 0

def check_non_negative(n: int) -> bool:
    """Returns True if zero or positive."""
    return n >= 0

def get_safe_positive_int(prompt: str) -> int:
    """Blocks until a strictly > 0 integer is provided (utilizing input_handler logic locally)."""
    while True:
        try:
            val = int(input(prompt))
            if check_positive(val):
                return val
            print("Error: Value must be strictly positive (> 0).")
        except ValueError:
            print("Error: Invalid integer.")
