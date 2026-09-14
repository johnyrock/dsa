# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `subsets_ii.py`, keep the tests, write it again.

## Key insight

Sort so equal values are adjacent, then run the ordinary Subsets recursion (record `path[:]` on entry, loop from `start`, recurse with `i + 1`) with one skip: `if i > start and nums[i] == nums[i - 1]: continue`. A repeated value is only a duplicate when it is offered as a *sibling* choice at the same level (`i > start`), because that sibling would rebuild the subtree the previous iteration already explored. When `i == start` the previous equal value was placed by the parent call, so this is the second copy stacked after the first, which is a new subset such as `[2, 2]`.

## Complexity

- Time: O(n log n) for the sort plus O(n · 2^n) in the worst case (all distinct), the same as Subsets. With repeats the tree is smaller and every call still records an answer, so the work is proportional to the output.
- Space: O(n) beyond the output, for `path` and the recursion depth. No hash set is needed.

## Mistakes to watch for

- Writing `i > 0` instead of `i > start`. The second copy is then never placed, not even after the first: `[1, 2, 2]` gives `[[], [1], [1, 2], [2]]`, losing `[1, 2, 2]` and `[2, 2]`.
- Forgetting `nums = sorted(nums)`. With `[2, 1, 2]` the two 2s are not neighbours, the check never fires, and the output has eight entries including `[2]` twice and both `[2, 1]` and `[1, 2]`.
- Dropping the skip and deduplicating with a set of tuples afterwards. Correct, but it builds every one of the 2^n subsets and holds them all; on `[2, 2, 2, 2, 2]` that is 32 built for 6 kept.
- Comparing `nums[i] == nums[i + 1]` and skipping the *first* copy instead of later ones. That skips the very branch that leads to `[2, 2]` and also mis-handles the last index.

## Related

- [medium/053-subsets](../053-subsets) is this algorithm without the sort and the skip.
- [medium/055-permutations](../055-permutations) is the ordered counterpart; Permutations II combines this skip with its `used` array.
- [medium/054-combination-sum](../054-combination-sum) shares the `start`-index loop; Combination Sum II adds exactly this skip.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
