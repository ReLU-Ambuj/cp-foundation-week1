# Check discrimenant. O(1)
def solve(a: float, b: float, c: float) -> str:
    disc = (b**2) - (4*a*c)
    if disc > 0: return "Two real"
    if disc == 0: return "One real"
    return "Complex"\n