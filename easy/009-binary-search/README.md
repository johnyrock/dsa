# 009. Binary Search

**Difficulty:** Easy | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #704

## Problem

Given an array of integers `nums` sorted in ascending order and an integer `target`, return the index of `target` in `nums`, or `-1` if it is not there.

The values are distinct. The solution has to run in O(log n) time, so a linear scan does not count.

## Examples

```
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4         # nums[4] == 9

Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1        # 2 is not in the array

Input:  nums = [5], target = 5
Output: 0
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- all values in `nums` are distinct and sorted in ascending order

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the linear scan to the halving loop, with complexity.

## Follow-up

- The linear scan is O(n). Can you use the sorted order to throw away half the array per comparison?
- What changes if duplicates are allowed and you want the *first* index equal to the target?
