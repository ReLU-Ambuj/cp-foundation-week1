# Simple tax percentage. O(1)
def solve(inc: float) -> float:
    if inc < 10000: return 0.0
    if inc < 50000: return inc * 0.1
    return inc * 0.2\n