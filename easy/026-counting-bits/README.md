# 026. Counting Bits

**Difficulty:** Easy | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #338

## Problem

Given an integer `n`, produce an array `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`.

Return that array. The intended solution builds it in a single linear pass without recounting bits for each value.

## Examples

```
Input:  n = 2
Output: [0,1,1]       # 0 -> 0, 1 -> 1, 10 -> 1

Input:  n = 5
Output: [0,1,1,2,1,2] # 0, 1, 10, 11, 100, 101

Input:  n = 8
Output: [0,1,1,2,1,2,2,3,1]   # 8 = 1000 resets to a single bit
```

## Constraints

- `0 <= n <= 10^5`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the `x >> 1` recurrence, from calling a popcount `n` times to the one-line DP fill.

## Follow-up

- There is a second recurrence, `ans[i] = ans[i & (i - 1)] + 1`. Why does it also work, and which one is easier to explain at the whiteboard?
- Can you do it in O(n) using the "highest power of two so far" offset, `ans[i] = ans[i - offset] + 1`, without any bit operators?
- What if only `ans[n]` is needed, not the whole array? Which approach from Number of 1 Bits is best then?
