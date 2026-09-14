# Intervals

## When to use

- The input is a list of `[start, end]` pairs: meetings, bookings, ranges on a number line.
- The question is about overlap: merge them, count conflicts, find free slots, insert one more.

## Template

```python
intervals.sort(key=lambda iv: iv[0])     # by start
merged = []
for start, end in intervals:
    if merged and start <= merged[-1][1]:            # overlaps the last output interval
        merged[-1][1] = max(merged[-1][1], end)      # extend, never shrink
    else:
        merged.append([start, end])                  # gap: new interval
return merged
```

After sorting by start, an interval can only overlap the *last* merged one. Everything earlier is finished. Some variants sort by end instead (removing the fewest intervals to make the rest disjoint).

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/009 Merge Intervals](../medium/009-merge-intervals/) | Medium | sort by start, extend the last output interval or append |
| [easy/021 Meeting Rooms](../easy/021-meeting-rooms/) | Easy | Sort by start time and compare neighboring meetings. |
| [medium/093 Non-overlapping Intervals](../medium/093-non-overlapping-intervals/) | Medium | Removing the fewest intervals is the same as keeping the most non-overlapping ones,… |
| [medium/094 Meeting Rooms II](../medium/094-meeting-rooms-ii/) | Medium | Sort meetings by start time and keep a min-heap of end times, one per room in use |
## Common mistakes

- Not sorting first. A single pass over unsorted input cannot see overlaps that appear out of order.
- Writing `merged[-1][1] = end` instead of `max(...)`, which shrinks the merged interval when the new one is contained.
- Using `<` where touching intervals (`[1, 4]` and `[4, 5]`) should merge; the problem statement decides.
- Comparing against the previous *input* interval instead of the last *output* interval.
- Mutating the caller's inner lists. Append fresh `[start, end]` lists.
