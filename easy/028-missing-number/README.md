# 028. Missing Number

**Difficulty:** Easy | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #268

## Problem

The array `nums` holds `n` distinct integers drawn from the range `[0, n]`. That range has `n + 1` values, so exactly one of them is absent.

Return the missing value. The intended solution runs in linear time and constant extra space, without sorting or a hash set.

## Examples

```
Input:  nums = [3,0,1]
Output: 2             # n = 3, range is 0..3, only 2 is absent

Input:  nums = [0,1]
Output: 2             # the missing value is n itself

Input:  nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Input:  nums = [1]
Output: 0             # the missing value can be 0
```

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- all values in `nums` are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the XOR cancellation, from sorting and scanning to the single fold over indices and values.

## Follow-up

- The arithmetic version, `n * (n + 1) / 2 - sum(nums)`, is just as short. When could it overflow in a fixed-width language, and why does XOR not have that problem?
- What if the array is sorted? Can you find the missing number in O(log n) with binary search on `nums[i] != i`?
- What if two numbers are missing from `[0, n + 1]`? How would you split the XOR into two groups (compare Single Number III)?
