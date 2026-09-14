# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

XOR is commutative and associative, `x ^ x == 0`, and `x ^ 0 == x`. So XOR-ing the whole array in any order is the same as grouping each duplicate pair together first: every pair collapses to `0`, and the lone value XOR `0` is the lone value. One accumulator starting at `0` folds the array in a single pass.

## Complexity

- Time: O(n), one pass.
- Space: O(1), a single integer.

## Mistakes to watch for

- Seeding the accumulator with `nums[0]` and then looping over all of `nums`. That XORs the first element twice and cancels it; either start at `0` or loop from index 1.
- Reaching for `sum(set(nums)) * 2 - sum(nums)`. It is correct but needs O(n) space for the set, which is exactly what the problem forbids.
- Using `+` or `|` instead of `^`. Addition does not cancel pairs and OR is not invertible, so neither leaves only the single value.
- Assuming the answer is the first or last element after sorting. Sorting is O(n log n) and the single value can sit anywhere.

## Related

- [easy/028-missing-number](../../easy/028-missing-number/) is the same cancellation trick with the full range `0..n` XOR-ed against the array.
- [easy/003-contains-duplicate](../../easy/003-contains-duplicate/) is the hash-set version of "have I seen this value before" that XOR replaces here.
- Single Number II (medium, LeetCode #137) counts each bit modulo 3 instead of modulo 2.
- Pattern doc: [bit-manipulation](../../patterns/bit-manipulation.md).
