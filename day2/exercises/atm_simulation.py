# PIN Check and Balance. O(1)
def solve(db_pin: int, pin: int, bal: float, withdrawal: float) -> str:
    if pin != db_pin: return "Wrong PIN"
    if withdrawal > bal: return "Insufficient"
    return str(bal - withdrawal)\n