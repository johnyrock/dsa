# 021. Search in Rotated Sorted Array

**Difficulty:** Medium | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #33

## Problem

An ascending array with all distinct values has been rotated at an unknown pivot. Given the rotated array and a target, return its index, or `-1` if it's not present, in O(log n) time.

## Examples

```
Input:  nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input:  nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- all values are unique
- must run in O(log n) time

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of identifying the sorted half at each step.

## Follow-up

- What breaks if duplicates are allowed (LeetCode #81), and how does the fix affect the time complexity?
