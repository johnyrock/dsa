# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `permutations.py`, keep the tests, write it again.

## Key insight

Fill `path` one slot at a time. Unlike Subsets, the loop runs over every index `for i in range(len(nums))` each time, because an element skipped for an earlier slot must still be available later; a parallel `used` array of booleans is what stops an element appearing twice. A permutation is complete exactly when `len(path) == len(nums)`, so only the leaves of the recursion tree are recorded. The choice has two halves (`used[i] = True`, `path.append`) and so does the undo (`path.pop()`, `used[i] = False`).

## Complexity

- Time: O(n · n!). The tree has n! leaves and fewer than e · n! nodes in total; each node loops over n indices and each leaf copies a list of length n.
- Space: O(n) beyond the output, for `path`, `used`, and the recursion depth.

## Mistakes to watch for

- Popping but not unmarking (dropping `used[i] = False`). After the first leaf `[1, 2, 3]` every flag stays `True`, every later call skips every index, and the output is `[[1, 2, 3]]` alone.
- `result.append(path)` without the `[:]` copy. All six entries alias the same list, which is empty once the recursion finishes: six copies of `[]`.
- Copying the Subsets loop `for i in range(start, len(nums))`. Elements can then only appear in index order, so the only sequence to reach length 3 is `[1, 2, 3]`.
- Checking `used[i]` but never setting it to `True`. Nothing is skipped, so all 27 sequences for `[1, 2, 3]` are produced, including `[1, 1, 1]`.

## Related

- [medium/053-subsets](../053-subsets) is the order-does-not-matter counterpart: a `start` index instead of a `used` array.
- [medium/056-subsets-ii](../056-subsets-ii) shows the sort-and-skip-neighbour trick that Permutations II combines with `used`.
- [medium/033-generate-parentheses](../033-generate-parentheses) is another backtracking problem whose answers live only at the leaves.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
