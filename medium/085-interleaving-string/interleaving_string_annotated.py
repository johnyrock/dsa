class Solution:
    # Decide whether s3 can be formed by interleaving s1 and s2: every character of both, in their original orders, merged into one string.
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        # The two lengths size the table and bound the loops.
        m, n = len(s1), len(s2)
        # An interleaving uses every character exactly once, so the lengths must add up. This also guarantees s3[i + j - 1] is always in range below.
        if m + n != len(s3):
            return False
        # dp[i][j] answers a smaller question: can the first i characters of s1 and the first j of s2 interleave to form the first i + j of s3?
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # dp[i][j]: s1[:i] and s2[:j] interleave to s3[:i + j]
        # Two empty prefixes interleave to the empty prefix of s3.
        dp[0][0] = True
        # Visit every cell in row-major order; each one only needs the cell above and the cell to its left, which are already final.
        for i in range(m + 1):
            for j in range(n + 1):
                # Case 1: the last character of s3[:i + j] came from s1. Then s3[i + j - 1] must equal s1[i - 1], and the rest must have been reachable without that character: dp[i - 1][j].
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                # Case 2: the last character came from s2 instead. Then s3[i + j - 1] must equal s2[j - 1] and dp[i][j - 1] must hold. Only one case needs to be true; if neither is, the cell stays False.
                elif j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        # The bottom-right cell is the question for the full strings.
        return dp[m][n]
