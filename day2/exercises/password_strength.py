# Evaluate weak, med, strong (length >8, >12). O(1)
def solve(pw: str) -> str:
    length = len(pw)
    if length < 8: return "Weak"
    if length <= 12: return "Medium"
    return "Strong"\n