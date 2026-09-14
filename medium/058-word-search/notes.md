# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `word_search.py`, keep the tests, write it again.

## Key insight

Start a depth-first search from every cell. `dfs(r, c, k)` asks "can `word[k:]` be spelled starting at `(r, c)`?": it fails if the cell is off the board or holds the wrong letter, succeeds when `k == len(word)`, and otherwise marks the cell with `"#"`, tries the four neighbours for `k + 1`, and restores the letter before returning. Overwriting the board is the visited set, so no extra memory is needed, and the restore is what lets a cell that was tried on one failed path be used again on another.

## Complexity

- Time: O(m · n · 3^L) where L is the word length. Every cell is a start, and after the first step each call has at most 3 unvisited neighbours to try.
- Space: O(L) for the recursion depth; the board itself is the visited set.

## Mistakes to watch for

- Forgetting `board[r][c] = saved` after the four recursive calls. Cells from failed attempts stay `"#"` forever. On the example board `exist(board, "CCB")` returns `False` instead of `True`: the start at `(0,2)` marks `(0,2)` and `(1,2)`, fails, and leaves them marked, so the real path `(1,2) → (0,2) → (0,1)` is gone.
- Not marking at all (no `"#"`). The path may revisit a cell, so `"ABCB"` returns `True` by bouncing back to the `B` at `(0,1)`.
- Checking `k == len(word)` *after* the bounds check instead of before. The last letter is matched at `k = len(word) - 1`, then every neighbour call has `k == len(word)` and must return `True` even when it is off the board; with the order swapped, a word whose last letter sits in a corner can fail.
- Using a set of `(r, c)` for visited but forgetting to `remove` on the way back is the same bug as the missing restore; `add` without `remove` still leaks between branches.
- Scanning only cells equal to `word[0]` is a fine optimisation, but the DFS must still verify `board[r][c] == word[k]` for every later letter, not just the first.

## Related

- [medium/010-number-of-islands](../010-number-of-islands) is the same grid DFS with the same trick of overwriting cells as the visited set, minus the undo.
- [medium/033-generate-parentheses](../033-generate-parentheses) shows the choose / recurse / undo shape on a string instead of a grid.
- [medium/047-implement-trie-prefix-tree](../047-implement-trie-prefix-tree) is the structure that turns this into Word Search II.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
