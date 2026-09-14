# 025. Number of 1 Bits

**Difficulty:** Easy | **Pattern:** [bit-manipulation](../../patterns/bit-manipulation.md) ([explained](../../concepts/bit-manipulation.html)) | **Source:** LeetCode #191

## Problem

Given a non-negative integer `n`, count how many bits are set to `1` in its binary representation. This count is also called the Hamming weight.

Return that count.

## Examples

```
Input:  n = 11
Output: 3             # 11 is 1011 in binary

Input:  n = 128
Output: 1             # 128 is 10000000, a single set bit

Input:  n = 2147483647
Output: 31            # 2^31 - 1 is thirty-one 1s
```

## Constraints

- `0 <= n <= 2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the bit-clearing loop, from checking all 32 positions to the `n & (n - 1)` trick that runs once per set bit.

## Follow-up

- If the function is called millions of times, how would you precompute answers for every byte and combine them?
- Can you use `n & (n - 1)` to test whether `n` is a power of two in one line?
- What changes if `n` is a signed 32-bit integer in a language without arbitrary-precision ints and you shift right with sign extension?
