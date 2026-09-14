# 023. Plus One

**Difficulty:** Easy | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #66

## Problem

A non-negative integer is given as an array `digits`, most significant digit first, with no leading zeros. Add one to the number.

Return the resulting digits in the same format. The answer may be one digit longer than the input.

## Examples

```
Input:  digits = [1,2,3]
Output: [1,2,4]       # 123 + 1 = 124, only the last digit changes

Input:  digits = [1,2,9]
Output: [1,3,0]       # the 9 rolls over and carries into the 2

Input:  digits = [9,9]
Output: [1,0,0]       # every digit was 9, so a new leading 1 appears
```

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` has no leading zeros (except the single number `[0]`)

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the right-to-left carry scan, from converting to an integer and back to the early-return loop.

## Follow-up

- How would you add an arbitrary `k` instead of one, or add two digit arrays together (Add Two Numbers, LeetCode #2 with the list stored as a linked list)?
- The solution mutates the input in place. When would that be unacceptable, and what does it cost to avoid?
- Why is `int(''.join(map(str, digits))) + 1` a poor answer in an interview even though it works in Python?
