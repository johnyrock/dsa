# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The binary form of `x` is the binary form of `x >> 1` with one more bit appended on the right, and that appended bit is `x & 1`. So `bits(x) = bits(x >> 1) + (x & 1)`. Since `x >> 1 < x`, filling the array in increasing order guarantees the subproblem is already answered, and each entry costs O(1).

## Complexity

- Time: O(n), one constant-time step per value.
- Space: O(n) for the output array; no extra beyond it.

## Mistakes to watch for

- Allocating `[0] * n` instead of `[0] * (n + 1)`. The range is inclusive of `n`, so the last write goes out of bounds.
- Looping `range(1, n)` instead of `range(1, n + 1)`, which leaves `counts[n]` at `0`.
- Writing `counts[value >> 1] + value & 1`. Without parentheses `+` binds tighter than `&`, so this evaluates `(counts[...] + value) & 1` and produces only 0s and 1s.
- Using `value // 2` and `value % 2` is equivalent and fine; using `value / 2` gives a float index and crashes.

## Related

- [easy/025-number-of-1-bits](../../easy/025-number-of-1-bits/) is the single-value popcount this problem asks for `n + 1` times.
- [easy/010-climbing-stairs](../../easy/010-climbing-stairs/) has the same shape: a table filled left to right where each entry depends on an earlier, already-computed one.
- [easy/020-min-cost-climbing-stairs](../../easy/020-min-cost-climbing-stairs/) is another bottom-up array fill worth comparing.
- Pattern doc: [bit-manipulation](../../patterns/bit-manipulation.md).
