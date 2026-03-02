# Problem 2: Leap Year Verification
## Problem Statement
Given an integer `Y` representing a year, determine if it is a leap year. Output "YES" or "NO".

## Sample Input
```text
2024
```
## Sample Output
```text
YES
```

## Hint
A year is leap if it is divisible by 4. However, century years (divisible by 100) are only leap if they are also divisible by 400.

## Clean Solution Code
```python
def solve():
    y = int(input())
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
```
