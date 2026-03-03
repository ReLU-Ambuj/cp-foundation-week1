# Call Stack Demonstration: Factorial
def factorial(n: int) -> int:
    # 1. Base Case (Stops the infinite loop)
    if n <= 1:
        return 1
    # 2. Recursive Step (Shrinks towards base case)
    return n * factorial(n - 1)

# Visualization of factorial(4)
# factorial(4) halts -> waits for factorial(3)
# factorial(3) halts -> waits for factorial(2)
# factorial(2) halts -> waits for factorial(1)
# factorial(1) hits Base Case -> returns 1
# 2 * 1 -> 2
# 3 * 2 -> 6
# 4 * 6 -> 24

if __name__ == "__main__":
    print(factorial(4)) # 24\n