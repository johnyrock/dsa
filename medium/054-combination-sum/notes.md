# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `combination_sum.py`, keep the tests, write it again.

## Key insight

Build a combination in a shared `path` while tracking `remaining`. Looping `for i in range(start, ...)` never looks back at earlier candidates, so each multiset is built in one order only; recursing with `backtrack(i, ...)` rather than `i + 1` keeps the candidate just placed available for reuse. Sorting first makes `if candidates[i] > remaining: break` safe: once one candidate overshoots, all later ones do, so the loop ends instead of visiting dead ends. `remaining == 0` on entry is the only base case.

## Complexity

- Time: O(n^(target / min(candidates))) as the standard upper bound, where the recursion depth is at most `target / min` and each level branches over at most `n` candidates. The `start` index and the `break` cut most of that tree in practice (10 calls for the running example, versus 48 count vectors for the brute force).
- Space: O(target / min(candidates)) for `path` and the recursion depth, plus the output.

## Mistakes to watch for

- Recursing with `backtrack(i + 1, ...)` (the Subsets habit). Reuse is then impossible: `[2, 2, 3]` is never built and `[2, 3, 6, 7], 7` returns `[[7]]`.
- Looping `for i in range(len(candidates))` instead of `range(start, ...)`. The same multiset is produced in every order: `[2, 2, 3]`, `[2, 3, 2]`, `[3, 2, 2]`, `[7]`, four answers instead of two.
- Keeping the `break` but forgetting `sorted(candidates)`. With `[5, 2]` and target 4, `5 > 4` breaks the root loop before `2` is seen and the output is `[]` instead of `[[2, 2]]`.
- Replacing the `break` with nothing and relying on a `remaining < 0` check that was never written. Then `remaining` goes negative and keeps going: the recursion never terminates.

## Related

- [medium/053-subsets](../053-subsets) is the same `start`-index loop with `i + 1`, no reuse, and no target.
- [medium/008-coin-change](../008-coin-change) asks for the *fewest* coins to reach a target; the same choose/recurse/undo with memoization instead of enumeration.
- [medium/033-generate-parentheses](../033-generate-parentheses) is another backtracking problem where a guard on the current state prunes before recursing.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
