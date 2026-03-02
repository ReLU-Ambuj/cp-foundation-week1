# Multiplication loop
def solve(binary: str) -> int:
    dec = 0
    power = 0
    # Walk backward
    for digit in reversed(binary):
        if digit == '1':
            dec += 2 ** power
        power += 1
    return dec

if __name__ == "__main__":
    print(solve("1010")) # 10\n