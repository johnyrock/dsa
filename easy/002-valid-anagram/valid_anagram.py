class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}  # character -> how many times it appears in s
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True
