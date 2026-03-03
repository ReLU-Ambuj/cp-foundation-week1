# Problem: Abstract digit counting O(N) loop
def count_digits(n: int) -> int:
    if n == 0: return 1
    temp = abs(n)
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    return count

if __name__ == "__main__":
    print(count_digits(159)) # 3\n