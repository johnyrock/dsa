# 007. Maximum Subarray

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) | **Source:** LeetCode #53

## Problem

Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

A subarray must contain at least one element, so the answer for an all-negative array is the largest single element, not 0.

## Examples

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6             # [4, -1, 2, 1]

Input:  nums = [1]
Output: 1

Input:  nums = [5, 4, -1, 7, 8]
Output: 23            # the whole array

Input:  nums = [-3, -1, -2]
Output: -1            # must pick something; the least bad single element
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- the subarray must be non-empty

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from summing every subarray to Kadane's one-pass "extend or restart" rule, with complexity.

## Follow-up

- The O(n) solution is a one-line recurrence. Can you state it as dynamic programming: what is the subproblem, and why does it only need the previous answer?
- The divide-and-conquer approach is O(n log n) and more subtle. When would an interviewer ask for it?
