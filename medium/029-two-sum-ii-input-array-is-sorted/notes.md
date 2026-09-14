# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `two_sum_ii_input_array_is_sorted.py`, keep the tests, write it again.

## Key insight

Because the array is sorted, the pair `(numbers[left], numbers[right])` with `left` at the start and `right` at the end tells you which direction to move. If the sum is too small, nothing paired with `numbers[left]` can reach the target (the right value is already the largest), so `left` is discarded forever. If the sum is too big, `numbers[right]` is discarded the same way. Each step removes one element from consideration, so the scan is one pass with no extra memory.

## Complexity

- Time: O(n), the pointers together move at most n − 1 times.
- Space: O(1), two indices and a running sum.

## Mistakes to watch for

- Returning 0-based indices. `return [left, right]` gives `[0, 1]` for the running example; the problem is 1-indexed and wants `[1, 2]`.
- Looping with `while left <= right`. The pointers can then meet on the same element and sum it with itself: `numbers = [2,7,11,15], target = 4` returns `[1, 1]` instead of never matching.
- Moving the wrong pointer. Writing `left += 1` on `total > target` walks away from the answer; on the running example it goes 17 → 22 → 26 and falls off the end.
- Reaching for the hash-map version out of habit. It is correct but O(n) space, and the follow-up explicitly asks for constant space.

## Related

- `easy/001-two-sum` is the unsorted version, solved with a hash map instead of two pointers.
- `medium/004-3sum` fixes one element and runs this exact inward scan on the remainder.
- `medium/005-container-with-most-water` moves two pointers inward with the same "discard the side that cannot improve" argument.
- Pattern doc: `patterns/two-pointers.md`
