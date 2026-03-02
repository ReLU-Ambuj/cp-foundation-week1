# Simple menu 1:Burger($5), 2:Pizza($10). Return total. O(1)
def solve(choice: int, qty: int) -> int:
    if qty < 0: return 0
    if choice == 1: return 5 * qty
    if choice == 2: return 10 * qty
    return 0\n