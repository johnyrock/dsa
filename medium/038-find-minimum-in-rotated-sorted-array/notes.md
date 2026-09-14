# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `find_minimum_in_rotated_sorted_array.py`, keep the tests, write it again.

## Key insight

A rotated sorted array is two ascending runs, and the minimum is the first element of the second run. Comparing `nums[mid]` with `nums[hi]` tells you which run `mid` is in: if `nums[mid] > nums[hi]`, `mid` is in the left (larger) run and the minimum is strictly to its right, so `lo = mid + 1`; otherwise `mid` through `hi` is sorted, so the minimum is at `mid` or to its left, and `hi = mid`. The predicate "`nums[i] <= nums[hi]`" is false for the left run and true for the right run, which is exactly the monotone shape binary search needs. The loop ends when `lo == hi` on the minimum.

## Complexity

- Time: O(log n), the range halves on every probe.
- Space: O(1), three indices.

## Mistakes to watch for

- Comparing `nums[mid]` with `nums[lo]` instead of `nums[hi]`. The left anchor is ambiguous: `nums[mid] > nums[lo]` is true both when `mid` is in the left run and when the array is not rotated. On `[4,5,6,7,0,1,2]` it walks to the right end and returns 2 instead of 0.
- Writing `hi = mid - 1` on the else branch. `mid` might be the minimum, and throwing it away makes `[3,1,2]` return 3: mid = 1 holds the answer 1, `hi` becomes 0, and `nums[0]` is returned.
- Using `while lo <= hi` with `hi = mid`. When `lo == hi`, `mid == hi` and `hi = mid` changes nothing, so the loop never ends.
- Returning `lo` (the index) instead of `nums[lo]`. The rotation count is a valid variant, but this problem asks for the value; `[4,5,6,7,0,1,2]` would give 4 instead of 0.

## Related

- `medium/021-search-in-rotated-sorted-array` — same two-run structure, but hunting a target rather than the pivot, so it needs the "which half is sorted" case split.
- `medium/037-koko-eating-bananas` — the same `lo < hi` / `hi = mid` loop, applied to an answer range instead of an index range.
- `easy/021-meeting-rooms` — for contrast: a problem where sorting is the whole trick and no search is needed.
- Pattern doc: `../../patterns/binary-search.md`
