# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `non_overlapping_intervals.py`, keep the tests, write it again.

## Key insight

Removing the fewest intervals is the same as keeping the most non-overlapping ones, and the classic activity-selection greedy does that: sort by end time and always keep the interval that finishes earliest, because it leaves the most room for whatever comes next. Sweep in end order with `prev_end`, the end of the last kept interval; an interval whose start is at or after `prev_end` is kept and becomes the new `prev_end`, anything else is counted as removed. Exchange argument: if an optimal answer keeps some other interval instead of the earliest-ending one, swapping it in never causes a new conflict.

## Complexity

- Time: O(n log n) for the sort; the sweep is O(n).
- Space: O(1) extra beyond the in-place sort.

## Mistakes to watch for

- Sorting by start instead of end and keeping whichever comes first. On `[[1, 100], [2, 3], [4, 5]]` that keeps `[1, 100]` and removes the other two, answering 2; sorting by end keeps `[2, 3]` and `[4, 5]`, removes `[1, 100]`, and answers 1. (Sorting by start does work if, on a conflict, you keep the interval with the *smaller* end, but sorting by end makes that decision automatic.)
- Using `start > prev_end` instead of `>=`. Touching intervals then count as overlapping: `[[1, 2], [2, 3]]` returns 1 instead of 0, and the running example returns 2 instead of 1.
- Updating `prev_end = end` on the *removed* interval too. In end order the removed interval ends no earlier than the kept one, so this cannot produce a wrong count here, but it breaks the invariant that `prev_end` belongs to a kept interval and will bite the moment the code is adapted to return the kept list.
- Starting with `prev_end = 0` or `-inf` and looping over all intervals. `-inf` works; `0` silently miscounts on negative coordinates (`[[-5, -1], [-2, 0]]` would be reported as 2 removals when the answer is 1).

## Related

- [medium/009-merge-intervals](../../medium/009-merge-intervals/) is the same sort-then-sweep shape, sorted by start and merging instead of discarding.
- [easy/021-meeting-rooms](../../easy/021-meeting-rooms/) is the yes/no version: is the answer here zero?
- [medium/020-insert-interval](../../medium/020-insert-interval/) uses the same touching-versus-overlapping boundary test.
- Pattern doc: [intervals](../../patterns/intervals.md).
