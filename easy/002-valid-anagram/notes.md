# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, the annotated version and the walkthrough were written up front rather than derived from an attempt, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `valid_anagram.py`, keep the tests, write it again.

## Key insight

An anagram is not about order, it is about the multiset of characters. So stop comparing the strings and compare their character counts: tally `s` in a dict, then walk `t` cancelling one copy at a time. Any character `t` needs that the tally cannot supply ends it immediately.

## Complexity

- Time: O(n), one pass to build the counts and one pass to cancel them, both with O(1) dict operations.
- Space: O(k) where k is the alphabet size — 26 for lowercase English letters, so effectively O(1).

## Mistakes to watch for

- Check `len(s) != len(t)` first. Without it, `s = "aa"`, `t = "a"` cancels the single `a` and falls through to `return True`, which is wrong. The length check is what makes the final `return True` safe.
- Use `counts.get(ch, 0) == 0` rather than `ch not in counts`. A character can be present with a count of zero once it has been used up, and `in` would wave it through.
- Decrement, do not delete-on-miss: the failure signal is a count that has already hit zero, not a missing key.

## Related

- Group Anagrams (medium) uses the same character-count idea as a dictionary key.
- `collections.Counter(s) == Counter(t)` is the one-liner, but the manual dict is the version worth being able to write.
