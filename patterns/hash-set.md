# Hash Set

## When to use

- You need "have I seen this exact value before?" and nothing else. No index, no count.
- Deduplication, or detecting the first repeat while scanning.
- A hash map where the value would always be `True` is a set.

## Template

```python
seen = set()
for x in items:
    if x in seen:
        return True      # first repeat
    seen.add(x)
return False
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/003 Contains Duplicate](../easy/003-contains-duplicate/) | Easy | early exit on first repeat |
| [medium/027 Valid Sudoku](../medium/027-valid-sudoku/) | Medium | Every filled cell belongs to exactly three groups: its row, its column, and its 3x3 box |
| [medium/028 Longest Consecutive Sequence](../medium/028-longest-consecutive-sequence/) | Medium | Put the values in a set so `x in seen` is O(1) |

## Common mistakes

- Using a list for membership, which makes each check O(n).
- Forgetting that `len(set(nums)) != len(nums)` builds the whole set and cannot exit early.
