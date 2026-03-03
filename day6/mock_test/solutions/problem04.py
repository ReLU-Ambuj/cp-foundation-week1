def find_missing(arr: list, n: int) -> tuple:
    # Total intended scope is 1 to N+2
    scope = n + 2
    seen = set(arr) # O(1) lookups
    missing = []
    
    # O(N) sweep
    for i in range(1, scope + 1):
        if i not in seen:
            missing.append(i)
            
    return tuple(missing)

if __name__ == "__main__":
    print(find_missing([1, 4, 5], 3)) # (2, 3)\n