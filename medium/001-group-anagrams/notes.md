# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `group_anagrams.py`, keep the tests, write it again.

## Key insight

Do not compare words to each other. Give every word a canonical key that is identical for all of its anagrams and different for everything else, then bucket by key in a dictionary. The sorted string `"".join(sorted(word))` is the obvious key; a 26-slot letter tally frozen into a tuple is the O(k) one. Either way the pairwise comparison disappears.

## Complexity

- Time: O(n · k), n words of average length k, with an O(k) tally per word. The sorted-key version is O(n · k log k).
- Space: O(n · k) for the dictionary holding every word, plus O(26) per key.

## Mistakes to watch for

- Using a list as the dictionary key. Lists are unhashable; freeze the tally with `tuple(...)`.
- Keying on the sum of character codes or a product of primes as a shortcut. Different multisets can collide (`"bdddddddddd"` and `"bbbbbbbbbbc"` have equal code sums). The tally or the sorted string is exact.
- Forgetting that the empty string is a valid word and forms its own group, and that two empty strings belong together.
- Returning the dictionary itself instead of `list(groups.values())`.

## Related

- Valid Anagram (easy/002) is the two-word version of the same tally; here the tally becomes a key instead of a comparison.
- Top K Frequent Elements (LeetCode #347) is the same count-then-bucket shape applied to numbers.
