class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        for i, ch in enumerate(s2):
            window[ord(ch) - ord("a")] += 1
            if i >= k:
                window[ord(s2[i - k]) - ord("a")] -= 1
            if window == need:
                return True
        return False
