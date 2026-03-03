def search_matrix(grid: list, target: int) -> bool:
    rows = len(grid)
    if rows == 0: return False
    cols = len(grid[0])
    
    # Iterating row-major
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == target:
                return True # Absolute guard exit
                
    return False

if __name__ == "__main__":
    grid = [[1, 2], [3, 4]]
    print(search_matrix(grid, 4)) # True\n