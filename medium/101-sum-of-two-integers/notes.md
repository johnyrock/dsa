# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `sum_of_two_integers.py`, keep the tests, write it again.

## Key insight

Binary addition splits into two independent parts: `a ^ b` is the sum of each bit position ignoring carries, and `(a & b) << 1` is the carry every position sends one place left. Adding those two numbers gives `a + b`, and they can be added with the same trick, so loop until the carry is 0. Python integers are unbounded, so a negative operand has infinitely many 1 bits and the carry would shift left forever; masking both values with `0xFFFFFFFF` after each round simulates a 32-bit register, and `~(a ^ MASK)` converts a register value with bit 31 set back into the negative Python int it represents.

## Complexity

- Time: O(1), at most 32 rounds since each round moves the carry at least one bit left inside a 32-bit register.
- Space: O(1).

## Mistakes to watch for

- Forgetting the `<< 1` on the carry: `(a & b)` alone adds the carry to the wrong bit. `get_sum(5, 3)` returns 7 instead of 8 (rounds: a = 6, b = 1; a = 7, b = 0).
- Dropping the `& MASK` on both values. Positive inputs still work, but `get_sum(-2, 3)` never terminates: the carry keeps shifting left through Python's unbounded integer and `b` never reaches 0.
- Returning `a` without the final unmask. `get_sum(-3, 1)` returns `4294967294` (`0xFFFFFFFE`), the unsigned reading of the register, instead of -2.
- Writing the unmask as `a - 0x100000000` or `-(~a & MASK) - 1`: correct mathematically, but both use `-`, which the problem forbids. `~(a ^ MASK)` uses only bitwise operators.

## Related

- [easy/025-number-of-1-bits](../../easy/025-number-of-1-bits/) — the `n & (n - 1)` trick, another loop driven by a bit pattern.
- [easy/024-single-number](../../easy/024-single-number/) — XOR as addition-without-carry, one bit position at a time.
- [easy/027-reverse-bits](../../easy/027-reverse-bits/) — the same 32-bit register discipline in Python.
- Pattern doc: [patterns/bit-manipulation.md](../../patterns/bit-manipulation.md)
