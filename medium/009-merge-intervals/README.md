# 009. Merge Intervals

**Difficulty:** Medium | **Pattern:** [intervals](../../patterns/intervals.md) | **Source:** LeetCode #56

## Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge every pair of overlapping intervals and return the resulting list of non-overlapping intervals that together cover the same points.

Intervals that merely touch, such as `[1, 4]` and `[4, 5]`, count as overlapping and are merged.

## Examples

```
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]     # [1,3] and [2,6] overlap

Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]                        # touching endpoints merge

Input:  intervals = [[1, 4], [2, 3]]
Output: [[1, 4]]                        # one interval swallows the other
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`
- the input is not guaranteed to be sorted

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from repeatedly scanning for any overlapping pair to sorting by start and merging in one sweep, with complexity.

## Follow-up

- Why does sorting by start make a single pass sufficient? What could go wrong without it?
- Insert Interval (LeetCode #57) gives you an already-merged list and one new interval. Can you do that one in O(n) without re-sorting?
