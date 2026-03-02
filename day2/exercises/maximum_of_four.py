# Problem: Find maximum of 4 integers using only if/else (No max() function).
# Input: 4 Integers
# Output: Integer Max
# Time/Space: O(1)

def solve(a: int, b: int, c: int, d: int) -> int:
    """
    Edge Cases:
    - All equal
    - Negatives
    - Max is the first or last argument
    """
    current_max = a
    if b > current_max: current_max = b
    if c > current_max: current_max = c
    if d > current_max: current_max = d
    return current_max

if __name__ == "__main__":
    print(solve(10, 50, 20, 5)) # Expected: 50
    print(solve(-5, -2, -10, -1)) # Expected: -1
    print(solve(4, 4, 4, 4)) # Expected: 4\n