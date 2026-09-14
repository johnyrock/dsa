class Solution:
    # Count the ways to split a digit string into codes 1..26 (A..Z). "0" on its own is never a code.
    def num_decodings(self, s: str) -> int:
        # An empty string has nothing to decode, and a leading "0" cannot start any code, so both are 0.
        if not s or s[0] == "0":
            return 0
        # dp[0] = 1: the empty prefix has exactly one decoding (do nothing). dp[1] = 1: the first digit, known non-zero, is one code. two_back and one_back are dp[i - 2] and dp[i - 1].
        two_back, one_back = 1, 1
        # Fill dp[2] .. dp[n]; i is the index of the digit that ends the prefix s[:i + 1].
        for i in range(1, len(s)):
            # dp[i + 1] starts empty and collects the two ways the prefix can end.
            ways = 0
            # Ending with a one-digit code s[i]: legal unless the digit is "0". Then the rest is any decoding of s[:i], which is one_back.
            if s[i] != "0":
                ways += one_back
            # Ending with a two-digit code s[i - 1]s[i]: legal only for 10..26 (the lower bound rejects "01".."09"). The rest is a decoding of s[:i - 1], which is two_back.
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ways += two_back
            # Slide the window: the previous one_back becomes two_back, and the freshly computed count becomes one_back. The right side is read before either name is rebound.
            two_back, one_back = one_back, ways
        # After the last digit, one_back is dp[n], the count for the whole string.
        return one_back
