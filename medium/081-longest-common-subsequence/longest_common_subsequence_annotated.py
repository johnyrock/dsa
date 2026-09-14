class Solution:
    # Return the length of the longest sequence of characters that appears, in order but not necessarily contiguously, in both strings.
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        # Cache the two lengths; they size the table and bound both loops.
        m, n = len(text1), len(text2)
        # dp[i][j] is the LCS length of the first i characters of text1 and the first j characters of text2. Row 0 and column 0 stay 0: an empty prefix shares nothing with anything.
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp[i][j]: LCS of text1[:i] and text2[:j]
        # Walk the prefixes of text1 from length 1 to m. Every cell only needs the row above and the cell to its left, so row-major order always has them ready.
        for i in range(1, m + 1):
            # Same for the prefixes of text2, so this pair (i, j) is one cell of the table.
            for j in range(1, n + 1):
                # The prefix of length i ends at index i - 1. If the two last characters are equal, they can be the final character of a common subsequence.
                if text1[i - 1] == text2[j - 1]:
                    # Match: pair these two characters up and extend the best answer for the two shorter prefixes by 1.
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Mismatch: at least one of the two last characters is not in the LCS, so drop one of them and keep the better of the two results.
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # The bottom-right cell is the answer for the two full strings.
        return dp[m][n]
