# 101. Sum of Two Integers

**Difficulty:** Medium | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #371

## Problem

Given two integers `a` and `b`, return their sum without using the operators `+` and `-`.

The intended tool is bitwise arithmetic: XOR adds each bit position without carrying, AND finds the positions that generate a carry, and a left shift moves those carries into place. Because Python integers are unbounded, the solution also has to simulate a 32-bit register so that negative operands terminate.

## Examples

```
Input:  a = 5, b = 3
Output: 8             # 101 ^ 011 = 110 (6), carry (101 & 011) << 1 = 010 (2); repeat until the carry is 0

Input:  a = 2, b = 3
Output: 5             # 010 ^ 011 = 001, carry 100; 001 ^ 100 = 101 = 5

Input:  a = -3, b = 1
Output: -2            # bit 31 is set after masking, so the register value is converted back to a negative int
```

## Constraints

- `-1000 <= a, b <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from repeated increments to the XOR / AND-shift loop, with the bit rows of `a`, `b`, `a ^ b`, and `(a & b) << 1` shown for every round, and why Python needs the `0xFFFFFFFF` mask.

## Follow-up

- How would you subtract `a - b` with the same tools? (Hint: negate `b` first, using only `~` and this function.)
- How many rounds can the loop take at most for 32-bit inputs, and what pair of inputs achieves it?
- In a language with fixed-width integers (Java, C++) the mask is unnecessary. Which two lines change, and what does the language do for you in their place?
