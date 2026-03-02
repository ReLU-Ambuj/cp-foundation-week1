# Chessboard coord to color (White/Black). O(1)
def solve(x: int, y: int) -> str:
    return "Black" if (x + y) % 2 == 0 else "White"\n