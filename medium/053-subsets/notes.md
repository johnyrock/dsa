# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `subsets.py`, keep the tests, write it again.

## Key insight

Every state of the shared `path` list is itself a subset, so the recursion records `path[:]` on entry instead of waiting for a "complete" check. Passing a `start` index and looping `for i in range(start, len(nums))` means each subset is built in increasing index order exactly once: once `2` is in the path, `1` is never offered again, so `[2, 1]` cannot be produced. The recursion tree has exactly one node per subset and its preorder is the output.

## Complexity

- Time: O(n · 2^n). There are 2^n calls, one per subset, and each copies a path of up to n elements. The output has that size, so this is optimal.
- Space: O(n) beyond the output, for `path` and the recursion depth.

## Mistakes to watch for

- `result.append(path)` instead of `result.append(path[:])`. Every entry is then the same list object, which is empty by the time the function returns: eight copies of `[]` for `[1, 2, 3]`.
- Looping `for i in range(len(nums))` instead of `range(start, len(nums))`. The child of `[1]` pushes `1` again, and again, so the path grows without bound and Python raises `RecursionError`.
- Recursing with `backtrack(i)` instead of `backtrack(i + 1)`. The element just placed stays available, so `[1, 1]`, `[1, 1, 1]`, ... are built and the recursion never terminates. (`backtrack(i)` is right for Combination Sum, where reuse is allowed.)
- Adding a "complete" base case such as `if len(path) == len(nums): return` before the record line. It is harmless here but it is the wrong mental model: for subsets there is no completion, every prefix is an answer.

## Related

- [medium/056-subsets-ii](../056-subsets-ii) is the same loop with one skip condition for duplicate values.
- [medium/054-combination-sum](../054-combination-sum) uses the same `start` index but recurses with `i` instead of `i + 1` so a candidate can be reused.
- [medium/055-permutations](../055-permutations) drops the `start` index and uses a `used` array instead, because order matters there.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
