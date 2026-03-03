# Problem: Count words bypassing standard spacing anomalies
def solve(s: str) -> int:
    count = 0
    in_word = False
    for char in s:
        if char != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

if __name__ == "__main__":
    print(solve("  Hello    World  ")) # 2\n