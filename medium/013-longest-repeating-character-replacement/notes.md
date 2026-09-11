# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `longest_repeating_character_replacement.py`, keep the tests, write it again.

## Key insight

A window of length L is achievable with k replacements if `L - max_count <= k`, where `max_count` is the frequency of the most common letter in the window (that letter stays, everything else gets replaced). Once a window becomes invalid, shrink from the left by one instead of scanning for a new max — the window can only grow again once it beats the current record, and a smaller max_count could only ever produce a smaller or equal window than one already found.

## Complexity

- Time: O(n), each index enters and leaves the window at most once.
- Space: O(1), the counts dict holds at most 26 letters.

## Mistakes to watch for

- Recomputing `max_count` from scratch on every shrink — unnecessary and turns the algorithm O(26n) to O(n) either way, but it's easy to think it's required for correctness. It isn't: a stale (too-high) `max_count` only ever makes the shrink condition harder to trigger, which is safe because it can't produce an answer longer than the true best.
- Forgetting to decrement `counts[s[left]]` when the window shrinks, which corrupts every count after it.
- Off-by-one on window length: it's `right - left + 1`, not `right - left`.

## Related

- Longest Substring Without Repeating Characters (medium) is the same sliding-window shrink/grow shape with a different validity check.
- Minimum Window Substring (hard, LeetCode #76) is the mirror problem: shrink to the smallest valid window instead of growing to the largest.
