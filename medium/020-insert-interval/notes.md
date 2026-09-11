# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `insert_interval.py`, keep the tests, write it again.

## Key insight

Because the input is already sorted and non-overlapping, a single linear scan splits cleanly into three phases: intervals entirely before the new one (append untouched), intervals that overlap it (fold into a running `[start, end]` by taking min/max), and intervals entirely after (append untouched). No sorting or re-merging pass is needed — the overlap phase produces exactly one merged interval because the input was already non-overlapping.

## Complexity

- Time: O(n), one pass through the intervals.
- Space: O(n) for the output (or O(1) extra if overwriting in place isn't required).

## Mistakes to watch for

- Using `<` instead of `<=` for the overlap test `intervals[i][0] <= end` — touching intervals like `[1,2]` and `[2,3]` do overlap (share the point 2) and must merge.
- Appending the merged interval to `result` before or during the merge loop instead of once, after it exits.
- Forgetting the case where `intervals` is empty, or where the new interval doesn't overlap anything.

## Related

- Merge Intervals (medium) is the general case: merge a whole unsorted list, which this problem's overlap phase is a specialized instance of.
- Non-overlapping Intervals (medium, LeetCode #435) asks how many intervals to remove to make the rest non-overlapping.
