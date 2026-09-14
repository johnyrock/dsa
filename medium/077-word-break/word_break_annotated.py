class Solution:
    # Return True if s can be cut into a sequence of dictionary words (words may repeat).
    def word_break(self, s: str, word_dict: list[str]) -> bool:
        # A set makes every "is this slice a word?" question O(1) instead of a scan of the list.
        words = set(word_dict)
        # dp[i] means "the prefix s[:i] can be fully segmented". One extra slot so dp[len(s)] exists.
        dp = [False] * (len(s) + 1)
        # The empty prefix is trivially segmented: zero words cover zero characters. Without this seed nothing can ever become True.
        dp[0] = True
        # Fill prefixes from shortest to longest, so every dp[j] a slot needs is already final.
        for i in range(1, len(s) + 1):
            # Try every cut point j: the last word would be s[j:i], and the part before it must itself be breakable.
            for j in range(i):
                # Both halves must work: a segmented prefix s[:j] followed by a dictionary word s[j:i].
                if dp[j] and s[j:i] in words:
                    # One valid cut is enough to prove the prefix breakable.
                    dp[i] = True
                    # No need to try the remaining cut points for this i.
                    break
        # The whole string is the prefix of length len(s).
        return dp[len(s)]
