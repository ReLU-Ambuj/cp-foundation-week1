# Problem 1: Adding Two Competitive Programming Integers
## Problem Statement
Given two integers space-separated on a single line, compute their sum. The input can be negative.

## Sample Input
```text
-45 100
```
## Sample Output
```text
55
```

## Hint
Use `map(int, input().split())` to read space-separated integers gracefully.

## Complexity
- Time: $O(1)$
- Space: $O(1)$

## Clean Solution Code
```python
def solve():
    a, b = map(int, input().split())
    print(a + b)

if __name__ == '__main__':
    solve()
```
