# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `permutation_in_string.py`, keep the tests, write it again.

## Key insight

A permutation of `s1` is any string with the same letter counts as `s1`, and it is always exactly `len(s1)` characters long. So slide a window of that fixed width across `s2`, keep a 26-slot count of what is inside it, and after each slide compare the window's counts to `s1`'s counts. Adding the entering character and removing the leaving one keeps the window's counts correct in O(1), and the 26-slot comparison is constant work.

## Complexity

- Time: O(26 · n) = O(n) where n = len(s2); one increment, one decrement, and one 26-slot comparison per character.
- Space: O(26) = O(1), two fixed-size count arrays regardless of input length.

## Mistakes to watch for

- Removing the left character one step late (`if i > k` instead of `if i >= k`). The window then holds `k + 1` characters, never matches, and the running example returns `False` instead of `True`.
- Removing the wrong index. The character that leaves is `s2[i - k]`; using `s2[i - k + 1]` shrinks the window to `k - 1` characters and, for `s1 = "ab"`, a window of one letter can never equal a two-letter signature.
- Testing set membership instead of counts (`set(window) == set(s1)`). `s1 = "aab"` and window `"abb"` have the same letter set and would wrongly return `True`.
- Skipping the `len(s1) > len(s2)` guard. The loop then finishes without a match and returns `False`, which happens to be correct, but the guard documents the impossibility and avoids the wasted pass. Do not, however, return `True` for it.

## Related

- `medium/003-longest-substring-without-repeating-characters` is the variable-width cousin: the window grows and shrinks instead of sliding at fixed width.
- `medium/013-longest-repeating-character-replacement` also maintains letter counts inside a window.
- `easy/002-valid-anagram` is the same 26-count comparison applied once to whole strings.
- Pattern doc: `patterns/sliding-window.md`
