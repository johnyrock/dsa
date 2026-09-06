# 002. Product of Array Except Self

**Difficulty:** Medium | **Pattern:** [prefix-sum](../../patterns/prefix-sum.md) | **Source:** LeetCode #238

## Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of every element of `nums` except `nums[i]`.

You must do it without using division, and the product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

## Examples

```
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]      # only the slot holding the zero gets a non-zero product

Input:  nums = [2, 3]
Output: [3, 2]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- the algorithm must run in O(n) time and must not use division

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the nested loop through the division trick that breaks on zeros to the two-sweep prefix and suffix products, with complexity.

## Follow-up

- Can you do it in O(1) extra space, not counting the output array?
- Why does the division approach fail, and how many zeros does it take to break it?
