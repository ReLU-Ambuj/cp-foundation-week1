# Problem 08: Most Frequent Word Breakdown

## Setup
Given a paragraph of text. Find the most frequent word. Ignore case. Ignore punctuation `. , ! ?`.

## Format
- **Input**: String S.
- **Output**: The most frequent word.
- **Constraints**: N <= 10^4
- **Difficulty**: 3/5

## Example
**In:**
```text
Hello world. Hello Python!
```
**Out:**
```text
hello
```

## Checklist
- Edge Cases: Ties map to alphabetically first.
- Required Complexity: O(N)
