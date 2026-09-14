class Solution:
    def num_decodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        two_back, one_back = 1, 1
        for i in range(1, len(s)):
            ways = 0
            if s[i] != "0":
                ways += one_back
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ways += two_back
            two_back, one_back = one_back, ways
        return one_back
