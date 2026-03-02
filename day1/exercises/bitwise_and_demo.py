# Problem: Bitwise AND of two numbers
# Input: A, B
# Output: A & B
# Time/Space: O(1)

def solve(a: int, b: int) -> int:
    # Bitwise AND only keeps bits that are 1 in both operands
    return a & b

if __name__ == "__main__":
    print(solve(5, 3)) # 101 & 011 = 001 (1)
