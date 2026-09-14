# 084. Target Sum

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #494

## Problem

You are given an integer array `nums` and an integer `target`. Build an expression by putting either a `+` or a `-` in front of every number and concatenating them, for example `+2-1` from `[2,1]`.

Return the number of different expressions that evaluate to `target`.

## Examples

```
Input:  nums = [1,1,1,1,1], target = 3
Output: 5             # exactly one of the five 1s gets a minus: -1+1+1+1+1, +1-1+1+1+1, ... five choices

Input:  nums = [1], target = 1
Output: 1             # +1

Input:  nums = [1,2,3], target = 0
Output: 2             # +1+2-3 and -1-2+3
```

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying all 2^n sign assignments to the subset-sum reduction and a single dp row, with complexity.

## Follow-up

- `nums.length <= 20` means the 2^n brute force is only about a million expressions. When does the DP actually start to matter, and when does the brute force win (hint: `sum(nums)` large, `n` small)?
- Allow a third choice, leaving a number out entirely. Does the subset-sum reduction survive, or do you need a different table?
- Return the expressions themselves, not the count. What breaks about the 1-D row, and what do you need to keep instead?
