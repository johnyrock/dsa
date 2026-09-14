# 024. Single Number

**Difficulty:** Easy | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #136

## Problem

In the integer array `nums`, every value appears exactly twice except for one value that appears once.

Return that single value. The solution must run in linear time and use constant extra space, which rules out a hash map or sorting.

## Examples

```
Input:  nums = [2,2,1]
Output: 1             # the 2s pair off

Input:  nums = [4,1,2,1,2]
Output: 4             # 1 and 2 each cancel, 4 is left

Input:  nums = [1]
Output: 1             # a single element is its own answer
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- every element appears twice except for one, which appears once

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the XOR fold, from the hash-map count to the single accumulator.

## Follow-up

- What if every other element appears three times instead of twice (Single Number II, LeetCode #137)? XOR alone no longer cancels them.
- What if exactly two elements appear once (Single Number III, LeetCode #260)? How do you split the array so each half has one of them?
- Why does the XOR trick work for negative numbers in Python, which has arbitrary-precision integers?
