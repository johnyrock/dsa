class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        # Frequency of each letter currently inside the window.
        counts = {}
        left = 0
        # The highest single-letter frequency seen in any window so far. It is
        # never recomputed on shrink, which is safe: see the note below.
        max_count = 0
        best = 0
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            # max_count only needs to grow to find the true answer, because a
            # window can only be valid (or the record) when it holds the
            # largest max_count seen up to this point.
            max_count = max(max_count, counts[ch])
            window_len = right - left + 1
            # A window is achievable if replacing every non-majority character
            # (window_len - max_count of them) costs at most k replacements.
            if window_len - max_count > k:
                # Shrink from the left instead of recomputing max_count, because
                # the window never needs to shrink smaller than the best one
                # already found — it just slides.
                counts[s[left]] -= 1
                left += 1
            else:
                best = max(best, window_len)
        return best
