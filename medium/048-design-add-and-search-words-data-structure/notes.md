# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `design_add_and_search_words_data_structure.py`, keep the tests, write it again.

## Key insight

Store the words in a trie exactly as in Implement Trie. A literal letter in the pattern follows one child, as before; a `.` has to try *every* child of the current node, so the search becomes a recursive `match(node, i)` that returns whether `word[i:]` can be matched from `node`. At a `.` it is `any(match(child, i + 1) for child in node.children.values())`, and `any` short-circuits at the first branch that works. When the pattern is used up, the answer is `node.is_word`, not `True`, so a prefix like `"ba"` or `"b."` does not match `"bad"`.

## Complexity

- Time: `add_word` is O(L). `search` is O(L) with no dots; each dot can fan out to up to 26 children, so a pattern with `d` dots is O(26^d · L) in the worst case, which the "at most 2 dots" constraint keeps small.
- Space: O(total characters added), less with shared prefixes.

## Mistakes to watch for

- Returning `True` instead of `node.is_word` when `i == len(word)`. Then `search("b.")` on `{bad, dad, mad}` returns `True`: the walk reaches `ba`, runs out of pattern, and never checks that no word ends there.
- Treating `.` as a literal, i.e. no wildcard branch at all. `search(".ad")` looks up `"."` in the root's children, finds nothing, and returns `False`.
- Using `all` instead of `any` at a dot. It happens to give the right answers on `{bad, dad, mad}` because every branch matches, but `search(".")` on an empty dictionary returns `True` (`all()` of nothing is `True`), and any dictionary where one child branch fails makes a good pattern return `False`.
- Recursing with `match(child, i + 1)` without the `child is not None` guard. `search("pad")` calls `match(None, 1)` and dies with `AttributeError: 'NoneType' object has no attribute 'children'`.

## Related

- [medium/047-implement-trie-prefix-tree](../047-implement-trie-prefix-tree/) — the same trie without the wildcard; `add_word` is its `insert` line for line.
- [medium/024-word-container](../024-word-container/) — a trie walked from every starting index instead of branched at a dot.
- [medium/019-clone-graph](../019-clone-graph/) — another recursion that fans out over all neighbours and needs a base case to stop.
- [patterns/trie.md](../../patterns/trie.md)
