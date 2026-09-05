# Binary Search

## When to use

- The input is sorted, or the answer space is monotonic (if x works then everything past x works).
- You need O(log n) and a linear scan is too slow.

## Template

```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/009 Binary Search](../easy/009-binary-search/) | Easy | inclusive bounds, `lo <= hi` |

## Common mistakes

- `while lo < hi` with inclusive `hi`, which skips the last candidate.
- Setting `lo = mid` or `hi = mid` instead of `mid + 1` / `mid - 1`, which can loop forever.
- Mixing inclusive and exclusive bounds. Pick one convention and keep it.
