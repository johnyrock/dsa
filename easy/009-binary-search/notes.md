# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, the annotated version, and the walkthrough were written up rather than worked out, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `binary_search.py`, keep the tests, write it again.

## Key insight

Sorted order turns one comparison into a decision about half the array. Compare the target with the middle element and the half it cannot be in disappears, so the search space goes 6 → 3 → 1 → 0 instead of 6 → 5 → 4 → …

## Complexity

- Time: O(log n), the window halves every iteration.
- Space: O(1), only the three index variables.

## Mistakes to watch for

- Use `while lo <= hi`, not `while lo < hi`. With `<` the loop exits while one candidate is still unchecked, so a target sitting at that last index returns -1. On `[-1, 0, 3, 5, 9, 12]` with `target = 0` the buggy version stops at `lo = hi = 1` and never looks at it.
- Move to `mid + 1` / `mid - 1`, never to `mid`. Setting `lo = mid` when the window is two wide leaves the window the same size and the loop spins forever.
- `hi` starts at `len(nums) - 1`, an index that exists, which is what makes `<=` the right comparison. The half-open variant (`hi = len(nums)`, `while lo < hi`, `hi = mid`) is also correct, but do not mix the two.
- Check `nums[mid] == target` before the two moves, or the answer gets discarded along with its half.

## Related

- Search Insert Position is the same loop, returning `lo` instead of -1 when it falls through.
- First Bad Version and Find Minimum in Rotated Sorted Array use the same halving on a predicate rather than on equality.
- Two Sum II (sorted input) shrinks a window from both ends too, but by two pointers rather than by halving.
