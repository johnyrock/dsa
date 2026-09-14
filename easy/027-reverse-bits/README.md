# 027. Reverse Bits

**Difficulty:** Easy | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #190

## Problem

Treat `n` as a 32-bit unsigned integer and reverse the order of its bits, so bit 0 becomes bit 31, bit 1 becomes bit 30, and so on. Leading zeros count as bits and end up as trailing zeros.

Return the reversed value as an integer.

## Examples

```
Input:  n = 00000010100101000001111010011100
Output: 964176192     # 00111001011110000010100101000000

Input:  n = 1
Output: 2147483648    # the lowest bit moves to position 31, 2^31

Input:  n = 0
Output: 0             # all zeros stay all zeros
```

## Constraints

- the input is a 32-bit unsigned integer (`0 <= n < 2^32`)

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the 32-step shift-and-or loop, from string reversal to the accumulator.

## Follow-up

- If this function is called many times, how would you cache reversed bytes and assemble the answer from four lookups?
- Can you reverse the bits in O(log 32) steps by swapping halves, then quarters, then pairs, using masks like `0x55555555`?
- Why does `int(bin(n)[2:][::-1], 2)` give the wrong answer for most inputs?
