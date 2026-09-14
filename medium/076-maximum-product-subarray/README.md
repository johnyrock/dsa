# 076. Maximum Product Subarray

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #152

## Problem

Given an integer array `nums`, find the contiguous, non-empty subarray whose elements multiply to the largest product, and return that product.

The array can contain negatives and zeros. The product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

## Examples

```
Input:  nums = [2, 3, -2, 4]
Output: 6             # [2, 3]; including the -2 flips the sign and the 4 on its own is only 4

Input:  nums = [-2, 0, -1]
Output: 0             # -2 * -1 = 2 would need to span the 0; the best subarray is [0]

Input:  nums = [-2, 3, -4]
Output: 24            # the whole array: two negatives cancel
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- the product of any prefix or suffix of `nums` fits in a 32-bit integer

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every subarray to Kadane's idea with a second running value for the smallest product, with complexity.

## Follow-up

- Return the subarray itself, not just the product. Which running value do you need to attach a start index to, and why is that harder than in Maximum Subarray?
- Solve it with two passes instead, one left to right and one right to left, taking the max prefix product with a reset at zeros. Why does that work?
- What if the array contained floats between 0 and 1? Does the sign trick still cover everything?
