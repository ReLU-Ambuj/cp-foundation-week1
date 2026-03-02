# 1-12 month input return days. O(1)
def solve(month: int) -> int:
    if month in (4,6,9,11): return 30
    if month == 2: return 28
    return 31\n