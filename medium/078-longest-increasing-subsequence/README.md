# 078. Longest Increasing Subsequence

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #300

## Problem

You are given an integer array `nums`. A subsequence keeps some of the elements in their original order but may skip any it likes. Return the length of the longest subsequence whose elements are strictly increasing.

Only the length is required, not the subsequence itself.

## Examples

```
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4             # 2, 3, 7, 101 (or 2, 5, 7, 18) — no increasing run of 5 exists

Input:  nums = [0, 1, 0, 3, 2, 3]
Output: 4             # 0, 1, 2, 3

Input:  nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1             # strictly increasing, so equal values never chain
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating subsequences to the `dp[i]` = "longest run ending at i" table, with complexity.

## Follow-up

- The O(n²) table is fine for 2500 elements. Can you get O(n log n) by keeping a `tails` array and binary-searching where each new value belongs?
- Return the subsequence itself, not just its length. What extra array do you need, and how do you read it back?
- Change "strictly increasing" to "non-decreasing". Which single character in the solution changes, and what does `[7, 7, 7]` return afterwards?
