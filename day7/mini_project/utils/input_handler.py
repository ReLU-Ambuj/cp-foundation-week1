def get_int(prompt: str) -> int:
    """Safely forces integer input via a while loop catching ValueError."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_float(prompt: str) -> float:
    """Safely forces float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number (e.g. 1.5).")

def get_menu_choice(prompt: str, min_val: int, max_val: int) -> int:
    """Ensures input is an integer and strictly bounds it."""
    while True:
        choice = get_int(prompt)
        if min_val <= choice <= max_val:
            return choice
        print(f"Error: Select an option between {min_val} and {max_val}.")
