# Problem: Return N terms of Fibonacci as a List (not printing)
def generate_fibonacci(n: int) -> list:
    if n <= 0: return []
    if n == 1: return [0]
    res = [0, 1]
    for _ in range(n - 2):
        res.append(res[-1] + res[-2])
    return res

if __name__ == "__main__":
    print(generate_fibonacci(5)) # [0, 1, 1, 2, 3]\n