# 001. Two Sum

**Difficulty:** Easy | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #1

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

Assume exactly one valid answer exists, and you can't use the same element twice.

## Examples

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]        # 2 + 7 = 9

Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]

Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- values can be negative
- exactly one valid answer exists

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from brute force to the one-pass hash map, with complexity.

## Follow-up

- The brute force is O(n²). Can you do it in one pass?
