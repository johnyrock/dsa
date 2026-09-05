# 003. Contains Duplicate

**Difficulty:** Easy | **Pattern:** [hash-set](../../patterns/hash-set.md) | **Source:** LeetCode #217

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice, and `False` if every element is distinct.

## Examples

```
Input:  nums = [1, 2, 3, 1]
Output: True         # the 1 at index 0 repeats at index 3

Input:  nums = [1, 2, 3, 4]
Output: False        # every value is distinct

Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

## Constraints

- `1 <= nums.length <= 10^5`
- values can be negative
- the array is not sorted

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from brute force through sorting to the one-pass hash set, with complexity.

## Follow-up

- The brute force is O(n²) and sorting is O(n log n). Can you do it in one pass?
- `len(set(nums)) != len(nums)` is the same answer in one line. When is the explicit loop better?
