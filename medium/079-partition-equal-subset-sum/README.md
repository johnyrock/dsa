# 079. Partition Equal Subset Sum

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #416

## Problem

You are given an array of positive integers `nums`. Decide whether it can be split into two groups (every element in exactly one group) whose sums are equal.

Return `True` if such a split exists, `False` otherwise.

## Examples

```
Input:  nums = [1, 5, 11, 5]
Output: True          # {1, 5, 5} = 11 and {11} = 11

Input:  nums = [1, 2, 3, 5]
Output: False         # total 11 is odd, so no two equal halves

Input:  nums = [1, 2, 5]
Output: False         # total 8 is even, but no subset sums to 4
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every subset to the 1-D reachable-sums table filled from high sums downward, with complexity.

## Follow-up

- Why must the inner loop over sums run from `target` down to `num`? Find the input where an ascending loop gives the wrong answer.
- Split into two groups whose sums differ by as little as possible (the minimum-difference variant). Which slot of the same table answers it?
- The table is a list of booleans. Can you pack it into a single Python integer and replace the inner loop with `bits |= bits << num`?
