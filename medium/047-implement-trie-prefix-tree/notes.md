# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `implement_trie_prefix_tree.py`, keep the tests, write it again.

## Key insight

Store words as a tree of characters: each node holds a dict of child nodes keyed by the next letter, and a boolean `is_word` on the node where an inserted word ends. Words sharing a prefix share the path for it, so `insert`, `search`, and `starts_with` all walk one character per step and cost O(len) regardless of how many words are stored. `search` and `starts_with` are the same walk; the only difference is that `search` also requires `is_word` on the final node.

## Complexity

- Time: O(L) per operation, where L is the length of the argument. Each character is one dict lookup.
- Space: O(total characters inserted) in the worst case with no shared prefixes; shared prefixes reduce it.

## Mistakes to watch for

- Forgetting `node.is_word = True` at the end of `insert`, or having `search` return `node is not None` without checking the flag. Then `search("app")` after `insert("apple")` returns `True` when it must be `False`: a prefix is not a word.
- Making `starts_with` check `is_word`. `starts_with("app")` after `insert("apple")` must be `True` even though no word "app" exists; the walk succeeding is the whole test.
- Overwriting an existing child in `insert` (`node.children[ch] = TrieNode()` unconditionally). That throws away the subtree below it, so after `insert("apple")` then `insert("app")`, `search("apple")` becomes `False`.
- Setting `is_word` on every node along the path instead of only the last one. Then every prefix of an inserted word searches as a word: `search("a")` returns `True` after `insert("apple")`.

## Related

- [medium/024-word-container](../024-word-container/) — builds the same trie and walks it from every starting index to find words inside words.
- [medium/048-design-add-and-search-words-data-structure](../048-design-add-and-search-words-data-structure/) — the same trie with a wildcard `.` that branches the search.
- [patterns/trie.md](../../patterns/trie.md)
