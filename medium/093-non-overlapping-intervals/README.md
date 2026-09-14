# 093. Non-overlapping Intervals

**Difficulty:** Medium | **Pattern:** [intervals](../../patterns/intervals.md) ([explained](../../concepts/intervals.html)) | **Source:** LeetCode #435

## Problem

You are given a list of intervals, each `[start, end]`. Return the minimum number of intervals you must remove so that the remaining intervals do not overlap.

Intervals that only touch, such as `[1, 2]` and `[2, 3]`, do not count as overlapping.

## Examples

```
Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1             # remove [1,3]; the other three are back to back

Input:  intervals = [[1,2],[1,2],[1,2]]
Output: 2             # three copies of the same interval, keep one

Input:  intervals = [[1,2],[2,3]]
Output: 0             # touching endpoints are allowed
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every subset to sorting by end time and greedily keeping whichever interval finishes first.

## Follow-up

- Return the intervals to *keep* instead of the count. What extra bookkeeping does the sweep need?
- Each interval now has a weight and you want to remove the minimum total weight. Why does the greedy break, and what replaces it?
- Meeting Rooms II (LeetCode #253) asks how many rooms the *overlapping* intervals need. How does that number relate to this one?
