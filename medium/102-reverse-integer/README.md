# 102. Reverse Integer

**Difficulty:** Medium | **Pattern:** [math](../../patterns/math.md) ([explained](../../concepts/math.html)) | **Source:** LeetCode #7

## Problem

You are given a signed 32-bit integer `x`. Return `x` with its decimal digits reversed, keeping the sign in front.

If the reversed value falls outside the signed 32-bit range `[-2^31, 2^31 - 1]`, return `0`. Assume the environment cannot store 64-bit integers, so the overflow has to be detected before it happens, not after.

## Examples

```
Input:  x = -123
Output: -321          # digits 1,2,3 reversed to 3,2,1; the sign stays at the front

Input:  x = 120
Output: 21            # reversed digits 0,2,1 read as 021, and the leading zero disappears

Input:  x = 1534236469
Output: 0             # reversed digits 9646324351 exceed 2^31 - 1 = 2147483647
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from string reversal to peeling digits with `% 10` and `// 10` while checking for overflow one step ahead, with complexity.

## Follow-up

- The overflow check compares against `INT_MAX // 10 = 214748364` and the digit `7`. Why is the negative limit's last digit `8` never needed when you work on the magnitude?
- Reverse the bits of the integer instead of its decimal digits (Reverse Bits, LeetCode #190). Which operations replace `% 10` and `// 10`?
- Reverse the digits in base `b` for an arbitrary `b`. What changes in the loop, and what is the new overflow threshold?
