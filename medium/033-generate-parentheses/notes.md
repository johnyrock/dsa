# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `generate_parentheses.py`, keep the tests, write it again.

## Key insight

Build the string one character at a time and only ever extend a prefix that can still become well-formed. Two guards are enough: add `(` while `open_count < n`, and add `)` while `close_count < open_count` (there is an unmatched opener to close). Every path that reaches length `2n` under those rules is valid, so there is no final validity check, and every valid string is reached exactly once because the two branches differ in their next character.

## Complexity

- Time: O(4^n / sqrt(n)), the Catalan number of outputs times O(n) to join each; the tree explores only valid prefixes so no work is spent on dead ends.
- Space: O(n) for `path` and the recursion depth, plus the output.

## Mistakes to watch for

- Writing the close guard as `close_count < n` instead of `close_count < open_count`. Every string with three of each bracket is then emitted: 20 strings for `n = 3` instead of 5, including `")))((("`.
- Forgetting `path.pop()` after the recursive call. The second branch then appends to a path that still holds the first branch's characters, the length check fires early on garbage, and the output contains strings longer than `2n` or nothing at all.
- Reversing the close guard to `open_count < close_count`. Starting from 0/0 it is never true, so the recursion only ever appends `(`, stops at `"((("` with length 3, and returns an empty list.
- Passing `open_count + 1` in the *close* branch (copy-paste slip). `close_count` never grows, so the guard `close_count < open_count` stays true and the recursion keeps appending `)` until the length check saves it, emitting `"((()))"`, `"(()))"`-style shapes and missing the others.

## Related

- [easy/004-valid-parentheses](../../easy/004-valid-parentheses) is the checker for the strings this problem produces; the `close_count < open_count` guard is that stack test done with a counter.
- [medium/024-word-container](../024-word-container) is another build-one-character-at-a-time recursion over a prefix structure.
- [medium/008-coin-change](../008-coin-change) shows the same choose/recurse/undo shape with memoization layered on top.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
