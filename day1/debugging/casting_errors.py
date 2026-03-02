# Problem: Value error when casting invalid strings
# Expected Error: ValueError: invalid literal for int() with base 10

def parse_input(user_input: str) -> int:
    # BUG: "10.5" cannot be cast directly to int()
    # Fix: return int(float(user_input))
    return int(user_input)

if __name__ == "__main__":
    try:
        parse_input("10.5")
    except Exception as e:
        print("Traceback Example:")
        print(f"ValueError: {e}")
