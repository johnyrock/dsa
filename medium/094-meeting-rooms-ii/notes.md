# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild it from the sort plus min-heap idea.

## Key insight

Sort meetings by start time and keep a min-heap of end times, one per room in use. When a meeting starts, the room that frees up soonest is `end_times[0]`; if it is already free (`end_times[0] <= start`) reuse it with `heapreplace`, otherwise `heappush` a new room. Rooms are never closed, so the heap's final size is the peak number of simultaneous meetings, which is the minimum number of rooms.

## Complexity

- Time: O(n log n) for the sort plus one O(log n) heap operation per meeting.
- Space: O(n) for the heap in the worst case, when every meeting overlaps every other.

## Mistakes to watch for

- Popping the free room and forgetting to push the new end time (`heappop` with no matching push). The room disappears instead of being reused, and `[[0,30],[5,10],[15,20]]` returns 1 instead of 2.
- Using `<` instead of `<=` in the free check. A meeting that starts exactly when another ends is then treated as a conflict, and `[[1,2],[2,3]]` returns 2 instead of 1.
- Comparing against the most recently assigned room (a single `prev_end`, as in Meeting Rooms I) instead of the heap minimum. On `[[1,5],[1,10],[5,8]]` the `prev_end` after `[1,10]` is 10, so `[5,8]` opens a third room even though the `[1,5]` room is free: 3 instead of 2. Only the smallest end time answers "is any room free".
- Returning the heap size at the moment of the last meeting with a version that pops without pushing back, or tracking `max(len(end_times))` with a `heappop` that closes rooms. The count must reflect the peak, and with `heapreplace` the heap never shrinks, so `len(end_times)` at the end is exactly that peak.

## Related

- [easy/021-meeting-rooms](../../easy/021-meeting-rooms) is the yes/no version: sort by start, compare each meeting with its predecessor.
- [medium/093-non-overlapping-intervals](../093-non-overlapping-intervals) sorts by end and counts removals instead of rooms.
- [medium/009-merge-intervals](../009-merge-intervals) is the same sort-by-start sweep, merging instead of counting.
- Review the [Intervals pattern](../../patterns/intervals.md) and its concept page.
