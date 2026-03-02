# The Mechanics of `range()`

## Understanding `range(start, stop, step)`
The `range` function is Python’s primary iteration factory for count-controlled loops.
- `start`: The first integer in the sequence (inclusive). Default is `0`.
- `stop`: The bounding limit (strictly **exclusive**).
- `step`: The gap between each integer. Default is `1`.

## Why is `stop` Exclusive?
Zero-indexing. C.S. standard dictates sequences start at 0.
If you want 10 elements, `range(10)` yields `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`.
The exclusive `stop` allows the length of the list to simply be `stop - start`.
Length of `range(2, 7)` is exactly $7 - 2 = 5$. If `stop` was inclusive, you'd constantly have to compute `stop - start + 1`.

## Negative Step
To iterate sequentially backwards, the `step` must be negative, AND the `start` bound must be mathematically greater than the `stop` bound.
```python
range(10, 0, -1)   # 10, 9, 8 ... 1
```
*Note: Because `stop` is exclusive, it halts BEFORE hitting 0. To reach 0, the stop must be `-1`.*

## How Python Implements Range (Iterator Concept)
In Python 2, `range()` generated an actual physical list in memory (massively inefficient for $10^9$).
In Python 3, `range()` is an **Iterator Object**. It computes the next number mathematically on the fly in $O(1)$ time and memory. It never stores the whole list in RAM.

## Common Mistakes in Competitive Programming
1. **Forgeting bounds on reverse traversal**: `for i in range(len(arr) - 1, 0, -1):` misses index `0`! Must be `range(len(arr) - 1, -1, -1)`.
2. **Modifying the iterator variable**: Writing `i += 5` manually inside a `for i in range(10):` loop. The internal iterator will strictly overwrite your manual modification on the next cycle.
3. **Using loops for math**: `sum([i for i in range(1, n+1)])` is $O(N)$. Mathematically computing `n * (n + 1) // 2` is $O(1)$.
