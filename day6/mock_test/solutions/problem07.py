def is_array_palindrome(arr: list) -> bool:
    n = len(arr)
    if n <= 1: return True
    
    # Two pointers converging
    left = 0
    right = n - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    print(is_array_palindrome([1, 2, 3, 2, 1])) # True\n