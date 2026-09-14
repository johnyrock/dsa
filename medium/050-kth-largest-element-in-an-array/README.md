# 050. Kth Largest Element in an Array

**Difficulty:** Medium | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #215

## Problem

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. This is the `k`th largest in *sorted order*, not the `k`th distinct element, so duplicates count separately.

Can you solve it without sorting the whole array?

## Examples

```
Input:  nums = [3,2,1,5,6,4], k = 2
Output: 5             # sorted descending: 6, 5, 4, 3, 2, 1 -> the 2nd is 5

Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4             # descending: 6, 5, 5, 4, ... -> the two 5s both count, so the 4th is 4

Input:  nums = [1], k = 1
Output: 1             # a single element is both the largest and the kth largest
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting the whole array to a min-heap that never holds more than `k` values, with complexity.

## Follow-up

- Quickselect solves this in O(n) average time in place. Sketch the partition step and explain why its worst case is O(n²).
- The values are bounded by `-10^4 <= nums[i] <= 10^4`. How does that bound enable an O(n + range) counting approach, and when would it beat the heap?
- If the numbers arrive as a stream and you must answer "kth largest so far" after every arrival, which approach survives unchanged?
