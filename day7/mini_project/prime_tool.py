def is_prime(n: int) -> bool:
    """O(sqrt N) determinism for prime values."""
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def primes_till_n(limit: int) -> list:
    """Builds array of primes up to a bounded limit."""
    return [i for i in range(2, limit + 1) if is_prime(i)]

def run_prime_interface(handler):
    """Integrates logic with input loop."""
    print("\\n--- Prime Analyzer ---")
    print("1. Check single prime")
    print("2. Generator strictly up to N")
    
    choice = handler.get_menu_choice("Select [1-2]: ", 1, 2)
    
    if choice == 1:
        val = handler.get_safe_positive_int("Enter number: ")
        res = "is Prime" if is_prime(val) else "is Composite"
        print(f"Result: {val} {res}.")
    else:
        val = handler.get_safe_positive_int("Enter limit: ")
        print(f"Primes up to {val}: {primes_till_n(val)}")
        print(f"Total count: {len(primes_till_n(val))}")
