# 043. Find the Duplicate Number

**Difficulty:** Medium | **Pattern:** [fast-slow-pointers](../../patterns/fast-slow-pointers.md) ([explained](../../concepts/fast-slow-pointers.html)) | **Source:** LeetCode #287

## Problem

You are given an array `nums` of `n + 1` integers, each in the range `[1, n]`. By the pigeonhole principle at least one value is repeated; the problem guarantees there is exactly one repeated value, though it may appear more than twice.

Return that repeated number. You must not modify the array and must use only constant extra space.

## Examples

```
Input:  nums = [1,3,4,2,2]
Output: 2             # following i -> nums[i] from 0: 0 -> 1 -> 3 -> 2 -> 4 -> 2, the cycle enters at 2

Input:  nums = [3,1,3,4,2]
Output: 3             # 0 -> 3 -> 4 -> 2 -> 3, the cycle enters at 3

Input:  nums = [3,3,3,3,3]
Output: 3             # the duplicate can appear many times; 0 -> 3 -> 3 is a self-loop at 3
```

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- all the integers in `nums` appear only once except for precisely one integer which appears two or more times

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the sort/set approaches, the array-as-linked-list reframing, Floyd's two phases traced on the example, pitfalls, and complexity.

## Follow-up

- Why does the cycle's entry point, and not just "some node on the cycle", equal the duplicate? Which value has two incoming edges?
- Can you solve it with binary search on the *value* range in O(n log n) time and O(1) space, without modifying the array?
- If you were allowed to modify the array, how would negating `nums[abs(x)]` find the duplicate in one pass?
