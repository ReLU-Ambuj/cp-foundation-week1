# Problem: Program crashes when calculating average of an empty array
# Expected Error: ZeroDivisionError

def calculate_average(nums: list[int]) -> float:
    # BUG: If len(nums) is 0, this crashes.
    # Fix: return sum(nums) / len(nums) if len(nums) > 0 else 0
    return sum(nums) / len(nums) 

if __name__ == "__main__":
    try:
        calculate_average([])
    except Exception as e:
        print("Traceback Example:")
        print(f"ZeroDivisionError: {e}")
