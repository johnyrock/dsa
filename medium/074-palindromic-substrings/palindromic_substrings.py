class Solution:
    def count_substrings(self, s: str) -> int:
        total = 0
        for centre in range(len(s)):
            for left, right in ((centre, centre), (centre, centre + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    total += 1
                    left -= 1
                    right += 1
        return total
