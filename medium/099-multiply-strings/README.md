# 099. Multiply Strings

**Difficulty:** Medium | **Pattern:** [math](../../patterns/math.md) ([explained](../../concepts/math.html)) | **Source:** LeetCode #43

## Problem

You are given two non-negative integers `num1` and `num2`, each represented as a string of decimal digits. Return their product, also as a string.

You must not convert the inputs directly to integers with a built-in (`int(num1)`), and you must not use a big-integer library. The point is to do the schoolbook multiplication digit by digit.

## Examples

```
Input:  num1 = "123", num2 = "456"
Output: "56088"       # 123 × 456; each digit pair lands at result[i + j + 1]

Input:  num1 = "2", num2 = "3"
Output: "6"           # the 2-cell result is [0, 6]; the leading 0 is stripped

Input:  num1 = "0", num2 = "12345"
Output: "0"           # a zero factor is caught before the loop, never "000000"
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only
- `num1` and `num2` do not contain any leading zero, except the number `0` itself

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the one-line `int()` cheat to the `i + j + 1` cell rule that lets every digit pair be added straight into its place, with complexity.

## Follow-up

- How would you add two such strings instead (LeetCode #415 Add Strings), and why is that a single pass while multiplying is nested?
- Can you cut the work below O(m · n) for very long inputs? Look up Karatsuba multiplication and work out where the three sub-products come from.
- The result cells can temporarily hold values above 9 (the tens carry is added, not normalised). Where exactly does the algorithm guarantee every cell is a single digit by the end?
