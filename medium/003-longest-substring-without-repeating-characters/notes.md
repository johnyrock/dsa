# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `longest_substring_without_repeating_characters.py`, keep the tests, write it again.

## Key insight

Keep a window `s[left:right+1]` that never contains a repeat. Extend `right` one character at a time. When the new character was already seen *inside the window*, move `left` to one past its previous position, which throws out the old copy and everything before it in a single jump. A dictionary of `char -> last index` answers "was it inside the window, and where?" in O(1).

## Complexity

- Time: O(n). `right` moves n times, and `left` only ever moves forward, so it moves at most n times in total.
- Space: O(min(n, alphabet)). The dictionary holds at most one entry per distinct character.

## Mistakes to watch for

- Moving `left` backwards. In `"abba"`, when the final `a` arrives its previous index is 0, but `left` is already 2. Only jump when `last_seen[ch] >= left`, or take `max(left, last_seen[ch] + 1)`.
- Confusing substring with subsequence. `"pwke"` in `"pwwkew"` is not a valid answer.
- Updating `best` before fixing the window, which counts a window that still contains the repeat.
- Returning the substring itself when only the length is asked for, or vice versa.
- The set-based version (`while ch in window: window.remove(s[left]); left += 1`) is also O(n) and is fine, it just crawls `left` forward instead of jumping.

## Related

- Longest Repeating Character Replacement (LeetCode #424) is the same window with a "how many mismatches can I afford" budget instead of a "no repeats" rule.
- Minimum Window Substring (LeetCode #76) is the shrinking-window version: extend until valid, then shrink while still valid.
