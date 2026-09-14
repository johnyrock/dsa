# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the recurrence.

## Key insight

`dp[i][j]` asks whether the first `i` characters of `s1` and the first `j` of `s2` can interleave to form the first `i + j` of `s3`. The last character of that prefix, `s3[i + j - 1]`, came from one of the two strings: either it equals `s1[i - 1]` and `dp[i - 1][j]` holds, or it equals `s2[j - 1]` and `dp[i][j - 1]` holds. Fill the `(m + 1) × (n + 1)` table in row-major order from `dp[0][0] = True`; the answer is `dp[m][n]`. A length check up front rules out the impossible case and keeps `s3[i + j - 1]` in range.

## Complexity

- Time: O(m × n), one constant-time cell per pair of prefix lengths.
- Space: O(m × n) for the table; O(n) with a single rolling row.

## Mistakes to watch for

- Starting both loops at 1 (`for i in range(1, m + 1)`) as in the LCS table. Row 0 and column 0 are not all-`True` here: `dp[0][j]` means "s2's first j characters alone match s3's first j", so they have to be computed. Skipping them leaves the border `False` and `"aabcc"`, `"dbbca"`, `"aadbbcbcac"` returns `False` instead of `True`.
- Greedy two-pointer scan (take from `s1` if it matches, else `s2`). On the running example it spends both of `s1`'s `c`s on `s3[5]` and `s3[7]`, then cannot place `s3[8] = 'a'` because `s2` still needs its `c` first, and returns `False`; only the table tries both owners of a repeated letter.
- Indexing `s3[i + j]` instead of `s3[i + j - 1]`. Cell `(i, j)` covers `i + j` characters, whose last index is `i + j - 1`; the off-by-one shifts every comparison and raises `IndexError` at the last cell.
- Dropping the `m + n != len(s3)` check. With `s3 = "aadbbcbcacx"` the table is filled as if the extra character did not exist and `dp[m][n]` is still `True`.

## Related

- [medium/081-longest-common-subsequence](../081-longest-common-subsequence) fills the same `(m + 1) × (n + 1)` prefix table with counts instead of booleans.
- [medium/012-longest-palindromic-substring](../012-longest-palindromic-substring) is another 2-D table over string indices.
- [medium/008-coin-change](../008-coin-change) is the 1-D "answer for a smaller input" version of the same idea.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
