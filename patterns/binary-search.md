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
| [medium/036 Search a 2D Matrix](../medium/036-search-a-2d-matrix/) | Medium | Because every row is sorted and each row starts after the previous one ends, reading… |
| [medium/037 Koko Eating Bananas](../medium/037-koko-eating-bananas/) | Medium | The answer is a number, not a position, and feasibility is monotonic in it: if speed… |
| [medium/038 Find Minimum in Rotated Sorted Array](../medium/038-find-minimum-in-rotated-sorted-array/) | Medium | A rotated sorted array is two ascending runs, and the minimum is the first element of… |
| [medium/039 Time Based Key-Value Store](../medium/039-time-based-key-value-store/) | Medium | Because timestamps for one key arrive strictly increasing, appending to a per-key list… |

## Common mistakes

- `while lo < hi` with inclusive `hi`, which skips the last candidate.
- Setting `lo = mid` or `hi = mid` instead of `mid + 1` / `mid - 1`, which can loop forever.
- Mixing inclusive and exclusive bounds. Pick one convention and keep it.
