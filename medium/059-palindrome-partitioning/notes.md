# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `palindrome_partitioning.py`, keep the tests, write it again.

## Key insight

A partition is a sequence of cut positions, so build it left to right: `backtrack(start)` decides where the piece beginning at `start` ends. For each `end` from `start` to the last index, if `s[start..end]` is a palindrome, push that piece, recurse on `end + 1`, and pop. When `start == len(s)` every character has been placed in a palindrome piece and `path` is a complete answer. The palindrome check *before* recursing is the pruning: a non-palindrome prefix can never be fixed by later cuts, so the whole subtree is skipped.

## Complexity

- Time: O(2^n · n). There are at most 2^(n-1) partitions (one per set of cut positions, all valid for a string like `"aaaa"`), each costs O(n) to copy, and each `is_palindrome` is O(n). A precomputed `pal[i][j]` table drops the check to O(1) but not the output bound.
- Space: O(n) for `path` and the recursion depth, plus the output.

## Mistakes to watch for

- Slicing `s[start:end]` instead of `s[start:end + 1]`. `end` is inclusive in `is_palindrome`, so the slice loses its last character: `"aab"` produces `[["", "", ""], ["a", ""]]`.
- Recursing with `backtrack(end)` instead of `backtrack(end + 1)`. The single-character case `end == start` calls `backtrack(start)` again with the same argument, so the recursion never terminates.
- Forgetting `path.pop()`. The second partition of `"aab"` comes out as `["a", "a", "b", "aa", "b"]` because the pieces of the first one were never removed.
- Dropping the `is_palindrome` check (or checking after the recursive call). Every cut set is emitted: `"aab"` returns 4 partitions including `["a", "ab"]` and `["aab"]`.
- Appending `path` rather than `path[:]`. All entries in `result` alias one list that is empty by the time the function returns.

## Related

- [medium/012-longest-palindromic-substring](../012-longest-palindromic-substring) has the same inward/outward palindrome test at its core.
- [medium/033-generate-parentheses](../033-generate-parentheses) uses the same push / recurse / pop with a guard that prunes before recursing.
- [medium/057-combination-sum-ii](../057-combination-sum-ii) is another "choose where this piece ends, then continue from the next index" recursion.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
