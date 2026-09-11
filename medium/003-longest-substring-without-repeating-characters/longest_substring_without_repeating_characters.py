class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        last_seen = {}  # char -> most recent index where it appeared
        left = 0        # start of the current window with no repeats
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best
