# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `word_break.py`, keep the tests, write it again.

## Key insight

Ask about prefixes, not the whole string: `dp[i]` is "can `s[:i]` be segmented?". The prefix `s[:i]` is breakable exactly when some cut `j < i` has a breakable prefix `s[:j]` followed by a dictionary word `s[j:i]`. Seed `dp[0] = True` for the empty prefix, fill `i` from 1 to `len(s)`, and the answer is `dp[len(s)]`. Every prefix is decided once, which kills the repeated work of plain backtracking.

## Complexity

- Time: O(n² × L) where `n = len(s)` and `L` is the longest word — n² cut points, each building and hashing a slice of length up to n (or L, if you bound the inner loop by the longest word).
- Space: O(n) for the table plus O(total dictionary characters) for the set.

## Mistakes to watch for

- Forgetting `dp[0] = True`. Then `dp[j]` is never True for any `j`, so nothing propagates and `"leetcode"` returns `False`.
- Slicing `s[j:i + 1]` instead of `s[j:i]`. The last slot `i = len(s)` then reads a slice that silently stops at the end, and `dp[4]` checks `"leetc"` instead of `"leet"`, so `"leetcode"` returns `False`.
- Returning `dp[len(s) - 1]` (the last index of `s`) instead of `dp[len(s)]`. For `"leetcode"` that is `dp[7]`, which is `False`.
- Greedy: taking the first dictionary word that matches and moving on. `"cars"` with `["car", "ca", "rs"]` grabs `"car"`, then `"s"` matches nothing, so greedy says `False` when `"ca" + "rs"` works.

## Related

- [medium/008-coin-change](../008-coin-change/) fills the same kind of table over amounts instead of prefixes: `dp[a]` from `dp[a - c]`.
- [easy/010-climbing-stairs](../../easy/010-climbing-stairs/) is the simplest "prefix depends on earlier prefixes" table.
- [medium/012-longest-palindromic-substring](../012-longest-palindromic-substring/) also decides substrings `s[j:i]`, but from a 2-D table.
- [patterns/dynamic-programming.md](../../patterns/dynamic-programming.md)
