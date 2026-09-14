# 094. Meeting Rooms II

**Difficulty:** Medium | **Pattern:** [intervals](../../patterns/intervals.md) ([explained](../../concepts/intervals.html)) | **Source:** LeetCode #253

## Problem

You are given a list of meeting time intervals, each a `[start, end]` pair. Two meetings whose times overlap cannot share a room, but a meeting may start in a room at the exact moment the previous meeting there ends.

Return the minimum number of conference rooms required to hold every meeting.

## Examples

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: 2             # [0,30] occupies one room the whole time; [5,10] and [15,20] take turns in a second

Input:  intervals = [[7,10],[2,4]]
Output: 1             # [2,4] is over before [7,10] begins, so one room serves both

Input:  intervals = [[1,5],[2,6],[3,7],[4,8]]
Output: 4             # at t = 4 all four meetings are running at once
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every time instant to a sort plus a min-heap of room end times, with complexity.

## Follow-up

- Return the peak time as well as the room count. Which moment does the heap approach see it at, and can you recover it without a second pass?
- Solve it with two sorted arrays (all starts, all ends) and two pointers instead of a heap. Why does that sweep give the same count, and which version is simpler to prove?
- Meetings now come with a required room size and rooms have capacities. Does the greedy "reuse the room that frees up first" still work?
