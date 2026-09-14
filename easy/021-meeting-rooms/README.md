# 021. Meeting Rooms

**Difficulty:** Easy | **Pattern:** [intervals](../../patterns/intervals.md) ([explained](../../concepts/intervals.html)) | **Source:** LeetCode #252

## Problem

You are given a list of meeting time intervals, each a `[start, end]` pair. One person wants to attend every meeting.

Return `true` if that is possible, meaning no two meetings overlap, and `false` otherwise. A meeting that starts exactly when another one ends does not count as an overlap.

## Examples

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: false         # [5,10] starts while [0,30] is still running

Input:  intervals = [[7,10],[2,4]]
Output: true          # [2,4] ends before [7,10] begins

Input:  intervals = [[1,2],[2,3]]
Output: true          # touching endpoints are allowed
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the sort-then-scan approach, from the O(n^2) pairwise check to the single pass over sorted neighbors.

## Follow-up

- How many rooms are needed to hold all the meetings at once (Meeting Rooms II, LeetCode #253)?
- If the intervals arrive already sorted by start, can you skip the O(n log n) step? What if they arrive one at a time?
- What changes if the input uses half-open ranges `[start, end)` versus closed ranges `[start, end]`?
