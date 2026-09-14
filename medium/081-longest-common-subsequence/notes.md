# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the recurrence.

## Key insight

`dp[i][j]` is the LCS length of the first `i` characters of `text1` and the first `j` characters of `text2`. If the two prefixes end in the same character, that character can close a common subsequence, so `dp[i][j] = dp[i-1][j-1] + 1`. If they differ, at least one of the two last characters is not part of the answer, so drop one and take `max(dp[i-1][j], dp[i][j-1])`. Row 0 and column 0 are 0 because an empty prefix shares nothing; the answer is `dp[m][n]`.

## Complexity

- Time: O(m × n), one constant-time cell per pair of prefixes.
- Space: O(m × n) for the table; O(min(m, n)) if only the previous row is kept.

## Mistakes to watch for

- Comparing `text1[i]` with `text2[j]` instead of `text1[i - 1]` and `text2[j - 1]`. Row `i` stands for the prefix of length `i`, whose last character is at index `i - 1`. The off-by-one shifts every match and returns 2 instead of 3 on `"abcde"`, `"ace"` (and raises `IndexError` on the last row without a guard).
- Using `dp[i-1][j-1]` in the mismatch branch. That only ever moves diagonally, so a match at `text1[1]` can never be combined with one at `text2[3]`; `"abcde"`, `"ace"` comes out as 1.
- Adding 1 in the mismatch branch as well (`max(dp[i-1][j], dp[i][j-1]) + 1`). The table then just counts cells and returns `min(m, n)` for any input, 3 for `"abc"`, `"def"`.
- Sizing the table `m × n` instead of `(m + 1) × (n + 1)`. Without the zero row and column the first row and column need special cases, and `dp[i-1]` at `i = 0` wraps to the last row in Python.

## Related

- [medium/085-interleaving-string](../085-interleaving-string) fills the same `(m + 1) × (n + 1)` prefix table with booleans instead of counts.
- [medium/012-longest-palindromic-substring](../012-longest-palindromic-substring) is the substring (contiguous) cousin; subsequences need the table, substrings can expand from the centre.
- [medium/008-coin-change](../008-coin-change) is the 1-D version of the same "best answer for a smaller input" idea.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
