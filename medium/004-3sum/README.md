# 004. 3Sum

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) | **Source:** LeetCode #15

## Problem

Given an integer array `nums`, return every triplet `[nums[i], nums[j], nums[k]]` with three distinct indices whose values sum to `0`.

The result must not contain duplicate triplets. Two triplets are duplicates if they contain the same three values, regardless of order or which indices produced them.

## Examples

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]     # order of triplets and within a triplet does not matter

Input:  nums = [0, 1, 1]
Output: []                            # nothing sums to zero

Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]                   # one triplet, not three
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
- the output may list triplets in any order

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the triple loop through sorting to fixing one number and closing two pointers on the rest, with the duplicate-skipping that makes it correct.

## Follow-up

- Two Sum used a hash map. Why does sorting plus two pointers win here once duplicates have to be removed?
- How would you generalise to 4Sum, and what is the running time?
