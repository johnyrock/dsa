# Notes

## Attempts

- 2026-09-12: Folder generated as reference material via the `add-problem` skill, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `word_container.py`, keep the tests, write it again.

## Key insight

Checking every word against every other word with Python's `in` operator is O(n² · L) and easy to write, but a trie built once over the whole list lets each word check itself against *all* other words in one walk: try every starting index inside the word, follow the trie one character at a time, and stop as soon as a completed word is found that isn't the word itself in full.

## Complexity

- Time: O(n · L²) worst case — for each of n words, try L starting positions, each walking up to L trie steps. Building the trie is O(n · L).
- Space: O(n · L) for the trie in the worst case (no shared prefixes).

## Mistakes to watch for

- Counting a word as containing itself. `start == 0 and end == n - 1` is the *entire* word, which must be excluded even though the trie legitimately marks that node as `is_word`.
- Forgetting to try every starting index. A word can appear anywhere inside another (`"suffix"` contains `"fix"` starting at index 3), not just at index 0.
- Stopping the outer loop instead of the inner one when a trie branch dead-ends (`node is None`). Only that starting index should be abandoned; other starting positions can still match.
- Treating duplicate identical words as containing each other. Two list entries with the same text are still "the same word," not "another word" — the exclusion above already prevents this because it only tracks whether a word exists, not how many times.

## Related

- Word Search (medium, LeetCode #79) walks a grid instead of a flat string but shares the "try every starting position" instinct.
- Implement Trie (medium, LeetCode #208) is the underlying data structure in isolation.
- Word Subsets (medium, LeetCode #916) is a different containment relationship (character-count subset, not substring).
