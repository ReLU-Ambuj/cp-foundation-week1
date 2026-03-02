# Problem: Determine if character is Vowel, Consonant, or Non-Alphabet
# Input: Single character String C
# Output: String ("Vowel", "Consonant", "Invalid")
# Constraints: len(C) == 1
# Time Complexity: O(1)
# Space Complexity: O(1)

def solve(c: str) -> str:
    """
    Edge Cases:
    - Capital letters (A)
    - Symbols (@)
    - Numbers (5)
    """
    if not c.isalpha():
        return "Invalid"
    
    # Use lowercase for uniform checking
    if c.lower() in 'aeiou':
        return "Vowel"
    return "Consonant"

if __name__ == "__main__":
    print(solve('A'))  # Expected: Vowel
    print(solve('b'))  # Expected: Consonant
    print(solve('@'))  # Expected: Invalid\n