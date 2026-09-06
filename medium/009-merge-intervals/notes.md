# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `merge_intervals.py`, keep the tests, write it again.

## Key insight

Sort by start. Then walk the list once, comparing each interval only with the last one in the output. Because starts are non-decreasing, the current interval overlaps the last merged one exactly when `start <= last.end`; if so, extend `last.end` with `max`. Otherwise there is a gap and this interval begins a new output entry. Everything before the last output entry is finished for good.

## Complexity

- Time: O(n log n) for the sort, then O(n) for the sweep.
- Space: O(n) for the output; O(1) extra beyond that and whatever the sort uses.

## Mistakes to watch for

- Skipping the sort. `[[4, 7], [1, 4]]` must give `[[1, 7]]`, and a single pass over unsorted input cannot see that.
- Writing `merged[-1][1] = end` instead of `max(merged[-1][1], end)`. `[1, 4]` followed by `[2, 3]` would shrink the merged interval to `[1, 3]`.
- Using `<` instead of `<=` in the overlap test. Touching intervals like `[1, 4]` and `[4, 5]` are supposed to merge.
- Appending the caller's own inner lists and then mutating them. Build fresh lists with `[start, end]`.
- Comparing against the previous *input* interval instead of the last *output* interval. After a merge, the output's end may be far beyond the previous input's end.

## Related

- Insert Interval (LeetCode #57) is this with one new interval and an already-sorted, already-merged input; it avoids the sort.
- Non-overlapping Intervals (LeetCode #435) sorts by end instead and counts removals.
- Meeting Rooms (LeetCode #252) is "does anything overlap?", which is this sweep with an early return.
