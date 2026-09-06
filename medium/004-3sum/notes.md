# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `three_sum.py`, keep the tests, write it again.

## Key insight

Sort first. Then fix the smallest element `nums[i]` and the problem collapses to Two Sum on the sorted suffix with target `-nums[i]`, which two pointers closing inward solve in O(n). Sorting also puts duplicates next to each other, so removing duplicate triplets is just "skip a value equal to the one you just used" at both the `i` level and the `left` level.

## Complexity

- Time: O(n²). Sorting is O(n log n), then n choices of `i` each with an O(n) two-pointer sweep.
- Space: O(1) extra beyond the output, ignoring whatever the sort uses internally.

## Mistakes to watch for

- Deduplicating with a set of tuples instead of skipping. It works, but it hides the reasoning the interviewer wants to see, and it costs extra memory.
- Skipping `nums[i] == nums[i + 1]` (looking forward) instead of `nums[i] == nums[i - 1]` (looking back). Looking forward skips the *first* copy, which loses triplets like `[-1, -1, 2]`.
- After recording a hit, moving only one pointer. Both must move: the same `left` with a different `right` cannot sum to zero again.
- Forgetting `left < right` inside the duplicate-skip loop, which can run the pointers past each other.
- `nums.sort()` mutates the caller's list. Fine for LeetCode; mention it out loud in an interview.

## Related

- Two Sum II (LeetCode #167) is the inner loop on its own: sorted input, two pointers.
- 4Sum (LeetCode #18) adds one more fixed outer loop for O(n³).
- 3Sum Closest (LeetCode #16) keeps the same pointer sweep but tracks the nearest total instead of exact hits.
