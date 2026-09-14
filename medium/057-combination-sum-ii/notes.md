# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `combination_sum_ii.py`, keep the tests, write it again.

## Key insight

Sort the candidates, then build combinations in ascending order by only ever choosing from index `start` onward and recursing with `i + 1`, so each index is used at most once. Sorting makes two prunes trivial: `candidates[i] > remaining` means every later candidate is also too big, so `break`; and `i > start and candidates[i] == candidates[i - 1]` means this value already started a branch at this level, so `continue`. The second copy of a value is still allowed *inside* a branch (`i == start`), which is how `[1, 1, 6]` is produced without `[1, 7]` being produced twice.

## Complexity

- Time: O(2^n · n) in the worst case (every subset could be a distinct answer and each is copied), plus O(n log n) for the sort; the break and skip prune most of the tree in practice.
- Space: O(n) for `path` and the recursion depth, plus the output.

## Mistakes to watch for

- Writing the skip as `i > 0 and candidates[i] == candidates[i - 1]` instead of `i > start`. That also blocks the second `1` right after the first one was chosen, so `[1, 1, 6]` is never built: the running example returns 3 combinations instead of 4.
- Dropping the skip entirely. Both `1`s start their own branch at the top level and each finds `[1, 2, 5]` and `[1, 7]`, so the output has 6 lists with two exact duplicates.
- Recursing with `backtrack(i, ...)` (the Combination Sum I call) instead of `backtrack(i + 1, ...)`. Indices get reused and the running example returns 10 combinations including `[1, 1, 1, 1, 1, 1, 1, 1]`.
- Using `continue` instead of `break` for `candidates[i] > remaining`. The output is still correct, but every branch scans to the end of the sorted list, which is the whole point of sorting lost.
- Appending `path` instead of `path[:]`. Every entry in `result` then aliases the same list, which is empty by the time the function returns.

## Related

- [medium/033-generate-parentheses](../033-generate-parentheses) is the same choose / recurse / pop shape with guards instead of a `break`.
- [medium/008-coin-change](../008-coin-change) is the counting version of "reach a target with these values", solved with DP instead of enumeration.
- [medium/004-3sum](../004-3sum) uses the same sort-then-skip-equal-neighbours trick to avoid duplicate triples.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
