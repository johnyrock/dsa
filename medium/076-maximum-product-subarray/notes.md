# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `maximum_product_subarray.py`, keep the tests, write it again.

## Key insight

Kadane's idea, "best subarray ending here is either this element alone or this element joined to the best ending just before it", is not enough for products, because a negative element turns the *smallest* product before it into the largest. So carry two values for subarrays ending at each index, `cur_max` and `cur_min`, and at every element pick both extremes from the same three candidates `(x, x * cur_max, x * cur_min)`. A zero falls out naturally: all three candidates become 0 or `x`, so the running products restart. The answer is the largest `cur_max` seen at any index.

## Complexity

- Time: O(n), one pass with three multiplications per element.
- Space: O(1), three integers.

## Mistakes to watch for

- Tracking only `cur_max` (plain Kadane with `*`). On `[-2, 3, -4]` it returns 3 instead of 24, because the -6 that becomes 24 was thrown away as "worse".
- Initialising `best = 0` (or `cur_max = cur_min = 1`) and looping over all of `nums`. On `[-2]` the answer is -2, but a zero seed returns 0. Seed everything with `nums[0]` and loop from index 1.
- Updating `cur_max` first and then computing `cur_min` from the *new* `cur_max`. The two must be computed from the same old pair; the tuple assignment does that in one statement.
- Treating a zero as a wall to split the array on and forgetting that `[0]` itself is a valid subarray. On `[-2, 0, -1]` the answer is 0, not the -1 or -2 from either side.

## Related

- [Maximum Subarray](../007-maximum-subarray) (medium/007) is the sum version, where one running value is enough.
- [House Robber](../072-house-robber) (medium/072) is another O(1)-space scan that keeps two values per position.
- [Product of Array Except Self](../002-product-of-array-except-self) (medium/002) also uses prefix and suffix products, which is the alternative two-pass solution here.
- Pattern doc: [dynamic-programming](../../patterns/dynamic-programming.md).
