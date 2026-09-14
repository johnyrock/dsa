# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Peel the lowest bit off `n` with `n & 1` and push it onto the low end of `result` with `result << 1 | bit`. The first bit peeled ends up shifted left 31 times, the last one zero times, which is exactly the reversal. The loop runs a fixed 32 times so that leading zeros in `n` become trailing zeros in the output, even after `n` itself has shifted down to `0`.

## Complexity

- Time: O(1), always exactly 32 iterations.
- Space: O(1).

## Mistakes to watch for

- Looping `while n:` instead of `for _ in range(32)`. That stops early once the remaining bits are zero, so `1` returns `1` instead of `2147483648`.
- Shifting `result` *after* the OR (`result |= n & 1; result <<= 1`). That leaves one extra shift at the end and doubles the answer.
- Forgetting `n >>= 1`, which ORs the same bit 32 times.
- Using `bin(n)[2:][::-1]` without `zfill(32)` first; the leading zeros are dropped before the reversal, so the width is wrong.

## Related

- [easy/025-number-of-1-bits](../../easy/025-number-of-1-bits/) walks the same bits with the same shifts, counting rather than moving them.
- [easy/026-counting-bits](../../easy/026-counting-bits/) uses `x >> 1` and `x & 1` as this problem does, in the other direction.
- [easy/006-valid-palindrome](../../easy/006-valid-palindrome/) is the same "reverse and compare" idea over characters instead of bits.
- Pattern doc: [bit-manipulation](../../patterns/bit-manipulation.md).
