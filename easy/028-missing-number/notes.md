# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

XOR-ing every value in `0..n` together with every value in `nums` pairs each present value with itself, and `x ^ x == 0`, so everything cancels except the one range value that has no partner. The indices `0..n-1` supply most of the range for free during `enumerate`, and `n` itself (the one index that does not exist) is seeded into the accumulator up front.

## Complexity

- Time: O(n), one pass.
- Space: O(1).

## Mistakes to watch for

- Starting `missing = 0` instead of `missing = len(nums)`. The range `[0, n]` has one more value than there are indices, and without seeding `n` the answer is off whenever `n` is the missing value (`[0,1]` returns `0` instead of `2`).
- XOR-ing only the values and not the indices, or vice versa. Both halves are needed for the pairs to cancel.
- Reaching for `sum(range(n + 1)) - sum(nums)`, which is correct but is worth knowing that in a 32-bit language `n * (n + 1) / 2` overflows well before `n = 10^5`.
- Building `set(range(n + 1)) - set(nums)` uses O(n) space, which the problem asks you to avoid.

## Related

- [easy/024-single-number](../../easy/024-single-number/) is the same pairwise XOR cancellation with the duplicates already inside the array.
- [easy/009-binary-search](../../easy/009-binary-search/) is the tool for the sorted-input follow-up (`nums[i] != i`).
- [easy/003-contains-duplicate](../../easy/003-contains-duplicate/) is the hash-set approach this problem asks you to improve on.
- Pattern doc: [bit-manipulation](../../patterns/bit-manipulation.md).
