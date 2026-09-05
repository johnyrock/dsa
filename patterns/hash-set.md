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

## Common mistakes

- Using a list for membership, which makes each check O(n).
- Forgetting that `len(set(nums)) != len(nums)` builds the whole set and cannot exit early.
