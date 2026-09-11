# 020. Insert Interval

**Difficulty:** Medium | **Pattern:** [intervals](../../patterns/intervals.md) ([explained](../../concepts/intervals.html)) | **Source:** LeetCode #57

## Problem

Given a list of non-overlapping intervals sorted by start, and a new interval, insert it into the list, merging any overlaps, and return the result still sorted by start.

## Examples

```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Constraints

- `intervals` is sorted by start and pairwise non-overlapping
- `0 <= intervals.length <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of the three-phase scan: before, merge, after.

## Follow-up

- Solve it with binary search on the start times instead of a linear scan, since the input is already sorted.
