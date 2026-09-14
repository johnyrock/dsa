# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Subtracting one from `n` flips the lowest set bit to `0` and every bit below it to `1`, so `n & (n - 1)` clears exactly the lowest set bit and leaves the rest untouched. Repeating that until `n` becomes `0` takes one iteration per set bit, and counting iterations is the answer. The loop never visits zero bits at all.

## Complexity

- Time: O(k), where `k` is the number of set bits (at most 32 here); the naive shift-and-test loop is O(32) regardless.
- Space: O(1).

## Mistakes to watch for

- Writing `n & n - 1` without parentheses is fine in Python (`-` binds tighter than `&`), but `n & (n - 1)` reads unambiguously; `(n & n) - 1` is the wrong grouping and would loop forever on `n = 1`.
- Using `n & (n + 1)` or `n | (n - 1)`. Neither clears a bit; the loop does not terminate.
- Counting with `while n > 0` and shifting `n >>= 1` but testing `n & 1` *after* the shift, which skips the lowest bit.
- Forgetting `n = 0`: the `while n` loop must run zero times and return `0`, so do not seed `count` at `1` or pre-check a bit before the loop.

## Related

- [easy/026-counting-bits](../../easy/026-counting-bits/) computes this count for every value from `0` to `n` at once using a DP over `x >> 1`.
- [easy/027-reverse-bits](../../easy/027-reverse-bits/) is the same fixed-width bit walk, but moving bits instead of counting them.
- [easy/024-single-number](../../easy/024-single-number/) is the other bit trick in this set worth pairing with `n & (n - 1)`.
- Pattern doc: [bit-manipulation](../../patterns/bit-manipulation.md).
