# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `product_of_array_except_self.py`, keep the tests, write it again.

## Key insight

"Everything except `nums[i]`" is "everything to the left of i" times "everything to the right of i". Both of those are running products you can compute in one sweep each: a left-to-right pass writes the prefix products into the output, and a right-to-left pass multiplies the suffix products on top. No division, and the output array is the only storage.

## Complexity

- Time: O(n), two passes over the array.
- Space: O(1) extra beyond the output array, which the problem does not count. Using separate prefix and suffix arrays is O(n) extra and is a fine first version.

## Mistakes to watch for

- Reaching for total product divided by `nums[i]`. It is forbidden by the statement, and it breaks on zeros: with one zero every other slot divides by zero, and with two zeros even the special-casing falls apart.
- Including `nums[i]` in its own prefix. Write `result[i] = prefix` **before** `prefix *= nums[i]`, and likewise for the suffix.
- Off-by-one in the reverse loop. `range(n - 1, -1, -1)` visits n-1 down to 0 inclusive.
- Initialising `prefix` or `suffix` to 0 instead of 1. Zero is the identity for sums, not products.

## Related

- Prefix sums (range-sum queries) are the additive version of this trick: one pass builds the running total, and any range is two lookups.
- Trapping Rain Water (LeetCode #42) uses the same left-max and right-max sweeps to compute a per-index answer.
