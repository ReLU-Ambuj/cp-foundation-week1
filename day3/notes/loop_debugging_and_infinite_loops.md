# Loop Debugging Protocol

## Infinite Loop Diagnosis
If your terminal hangs or CPU spikes to 100%:
1. `Ctrl+C` immediately.
2. Verify the **State Update** clause. Is your counter incrementing?
3. Did an interior `if A: continue` skip the State Update entirely?

## Variable Mutation Errors
```python
n = 10
for i in range(n):
    n += 1 # WARNING: Modifying loop bounds while iterating
```

## Loop Variable Shadowing
Reusing the literal character `i` for both the outer and inner loops. The inner loop completely destructs the outer loop's state mapping.
```python
for i in range(5):
    for i in range(3): # Catastrophic overwrite
        pass
```

## The Manual Dry-Run Method
The only way to master loops initially is executing them on paper.
Create a table:
| Iteration | i | condition | output | update |
|-----------|---|-----------|--------|--------|
| 1 | 0 | True | * | 1 |
| 2 | 1 | True | * | 2 |
| ... | | | | |\n