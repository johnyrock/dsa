# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `search_in_rotated_sorted_array.py`, keep the tests, write it again.

## Key insight

A rotated sorted array still has a useful property at every binary-search step: comparing `nums[left]` to `nums[mid]` tells you which half — `[left, mid]` or `[mid, right]` — is a normal contiguous ascending run (the other half contains the rotation point). Once you know which half is properly sorted, a simple range check decides whether the target could be in it, and you discard the other half exactly like standard binary search.

## Complexity

- Time: O(log n).
- Space: O(1).

## Mistakes to watch for

- Getting the "which half is sorted" check backwards. `nums[left] <= nums[mid]` means the *left* half is sorted, not the right.
- Using `<` instead of `<=` in `nums[left] <= nums[mid]` — when `left == mid` (a 2-element window), they must compare as sorted.
- Forgetting the empty-array edge case, which a `while left <= right` loop handles fine as long as `right` starts at `len(nums) - 1`, not `len(nums)`.

## Related

- Binary Search (easy) is the unrotated base case this problem builds on.
- Find Minimum in Rotated Sorted Array (medium, LeetCode #153) finds the pivot itself using the same sorted-half logic.
