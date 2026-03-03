import sys
from utils import input_handler
import number_utils
import prime_tool
import calculator_tool
import pattern_tool

def print_menu():
    """Outputs the primary interface."""
    print("\\n" + "="*40)
    print("   CP FOUNDATION WEEK 1 - UTILITY SUITE   ")
    print("="*40)
    print("1. Number Operations (Factorial, LCM, Reverse)")
    print("2. Prime Engine")
    print("3. Calculator")
    print("4. Pattern Generator")
    print("5. Exit System")
    print("="*40)

def run_number_module():
    print("\\n--- Number Operations ---")
    print("1. Factorial")
    print("2. LCM")
    print("3. Reverse Number")
    
    choice = input_handler.get_menu_choice("Select operation [1-3]: ", 1, 3)
    
    if choice == 1:
        n = input_handler.get_int("Enter n (>=0): ")
        print(f"Factorial of {n} is: {number_utils.factorial(n)}")
    elif choice == 2:
        a = input_handler.get_int("Enter A: ")
        b = input_handler.get_int("Enter B: ")
        print(f"LCM of {a}, {b} is: {number_utils.lcm(a, b)}")
    elif choice == 3:
        n = input_handler.get_int("Enter integer to reverse: ")
        print(f"Reversed: {number_utils.reverse_number(n)}")

def main():
    while True:
        print_menu()
        choice = input_handler.get_menu_choice("Routing Code [1-5]: ", 1, 5)
        
        if choice == 1:
            run_number_module()
        elif choice == 2:
            prime_tool.run_prime_interface(input_handler)
        elif choice == 3:
            calculator_tool.run_calculator() # Note: I'll need to remove the arg it expected
        elif choice == 4:
            pattern_tool.run_pattern_interface(input_handler)
        elif choice == 5:
            print("\\nSystems down. Exiting suite... Goodbye.")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\n\\n[!] Emergency Halt Detected. Exiting.")
        sys.exit(0)
