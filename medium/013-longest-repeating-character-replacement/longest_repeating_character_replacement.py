class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_count = 0
        best = 0
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            max_count = max(max_count, counts[ch])
            window_len = right - left + 1
            if window_len - max_count > k:
                counts[s[left]] -= 1
                left += 1
            else:
                best = max(best, window_len)
        return best
