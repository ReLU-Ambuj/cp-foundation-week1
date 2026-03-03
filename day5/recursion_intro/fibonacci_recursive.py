# Warning: Naive Recursion Exponential Blowup O(2^N)
def fib(n: int) -> int:
    # Base cases for Fib:
    if n == 0: return 0
    if n == 1: return 1
    
    # Recursive branches (Splits execution into TWO parallel trees)
    return fib(n - 1) + fib(n - 2)

# If you run fib(40), your computer will freeze because it evaluates fib(2) millions of times manually.
# Iteration is structurally superior for standard Fibonacci.

if __name__ == "__main__":
    print(fib(6)) # 8\n