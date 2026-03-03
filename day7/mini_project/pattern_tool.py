def print_pyramid(n: int):
    """Standard padding space centered pyramid."""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

def print_right_triangle(n: int):
    """Standard bounded left-flush triangle."""
    for i in range(1, n + 1):
        print("*" * i)

def print_inverted_triangle(n: int):
    """Descending iteration visualization."""
    for i in range(n, 0, -1):
        print("*" * i)

def run_pattern_interface(handler):
    """Routes CLI parameters to Pattern Visualizations."""
    print("\\n--- Pattern Generation Matrix ---")
    print("1. Centered Pyramid")
    print("2. Left-Flush Triangle")
    print("3. Inverted Left-Flush Triangle")
    
    choice = handler.get_menu_choice("Select format [1-3]: ", 1, 3)
    size = handler.get_safe_positive_int("Enter pattern bounded size (rows): ")
    
    print("\\nGenerating Pattern:\\n")
    if choice == 1: print_pyramid(size)
    elif choice == 2: print_right_triangle(size)
    elif choice == 3: print_inverted_triangle(size)
