# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `maximum_subarray.py`, keep the tests, write it again.

## Key insight

Ask, at each index, "what is the best subarray that ends *right here*?" It is either the previous best-ending-here plus this element, or this element alone. That is `current = max(x, current + x)`: a negative running sum is dead weight, so drop it and restart. The overall answer is the largest `current` seen at any index. This is Kadane's algorithm, and it is dynamic programming with a one-element table.

## Complexity

- Time: O(n), one pass with two comparisons per element.
- Space: O(1), two scalars.

## Mistakes to watch for

- Initialising `best` or `current` to 0. For `[-3, -1, -2]` the answer is -1, and a 0 seed returns 0, which is not the sum of any subarray. Seed with `nums[0]`.
- Writing `current = max(0, current + x)` (the "reset to 0" variant). It works only when a positive element exists; it fails on all-negative input for the same reason.
- Updating `best` before `current`, which compares against the previous index's run.
- Confusing "best ending here" with "best so far". They are different quantities, and the recurrence is only correct for the first one.

## Related

- Best Time to Buy and Sell Stock (easy/005) is the same running-best trick applied to differences instead of sums.
- Maximum Product Subarray (LeetCode #152) is the same shape but must track both the max and min running products because a negative flips them.
- Climbing Stairs (easy/010) is the other DP here whose table collapses to O(1) variables.
