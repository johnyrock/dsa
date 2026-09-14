# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `partition_labels.py`, keep the tests, write it again.

## Key insight

A part that contains a letter must extend at least to that letter's last occurrence. So walk the string keeping `end = max(end, last[ch])`, the furthest index any letter seen in the current part still needs. The moment the walk reaches `end`, every letter in the part has been fully consumed and nothing later depends on it, so cutting there is safe and, because we cut at the first such moment, produces the most parts. The `last` map is built in one pass up front so each lookup is O(1).

## Complexity

- Time: O(n), one pass to build `last` and one pass to cut.
- Space: O(1) beyond the output, since `last` holds at most 26 keys.

## Mistakes to watch for

- Testing `if i == last[ch]` (the current letter's own last index) instead of `if i == end`. On `"abab"` that closes a part at index 2, `a`'s last occurrence, and splits the two `b`s across parts: `[3, 1]` instead of `[4]`. On the running example it produces twelve parts, `[6, 2, 1, 3, 2, 1, 1, 4, 1, 1, 1, 1]`. Dropping the `max` (`end = last[ch]`) is the same bug in different clothes.
- Forgetting to reset `size = 0` after appending. The second part then reports a cumulative count: `[9, 16, 24]` on the running example.
- Building `last` with the *first* index (`setdefault`) instead of the last. On `"abab"` that maps `a` to 0 and `b` to 1, so `end` never gets past 1 and the trailing letters are never closed: `[1, 1]`, which does not even sum to the length.

## Related

- [medium/009-merge-intervals](../../medium/009-merge-intervals/) is the same shape: each letter spans `[first, last]`, and the parts are exactly the merged intervals.
- [medium/035-car-fleet](../../medium/035-car-fleet/) also sweeps once while carrying a running boundary that later elements can extend.
- Pattern doc: [greedy](../../patterns/greedy.md).
