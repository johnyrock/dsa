# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Once the meetings are sorted by start time, an overlap can only happen between neighbors: if meeting `i` overlaps some later meeting `j`, it must also overlap `i + 1`, because `i + 1` starts no later than `j` and `i` is still running at that point. So one pass comparing each start against the previous end is enough, and the first `start < previous_end` decides the answer.

## Complexity

- Time: O(n log n) for the sort; the scan afterwards is O(n).
- Space: O(1) extra beyond the sort (Python's sort is in place; Timsort uses O(n) internally in the worst case).

## Mistakes to watch for

- Comparing with `<=` instead of `<`. `[1,2]` and `[2,3]` share an endpoint but do not overlap; `<=` would report a conflict.
- Comparing against the previous *start* instead of the previous *end*. Sorting guarantees starts are non-decreasing, so that check never fires.
- Forgetting to sort and only checking neighbors in input order. `[[0,30],[15,20],[5,10]]` looks conflict-free at index 1 vs 2 when it is not.
- The loop starts at index 1, so an empty list or a single meeting falls through to `return True` without touching `intervals[-1]`.

## Related

- [medium/009-merge-intervals](../../medium/009-merge-intervals/) uses the same sort-by-start-then-compare-neighbors scan, but merges instead of bailing out.
- [medium/020-insert-interval](../../medium/020-insert-interval/) is the same overlap test applied to one new interval against an already sorted list.
- Meeting Rooms II (medium, LeetCode #253) asks for the minimum number of rooms and needs a heap or a sweep over sorted starts and ends.
- Pattern doc: [intervals](../../patterns/intervals.md).
