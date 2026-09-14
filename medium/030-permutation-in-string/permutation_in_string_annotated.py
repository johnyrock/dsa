class Solution:
    # Return True if some contiguous substring of s2 is a rearrangement of s1.
    def check_inclusion(self, s1: str, s2: str) -> bool:
        # Every permutation of s1 has exactly len(s1) characters, so that is the only window size to test.
        k = len(s1)
        # A window longer than the whole text cannot exist, so answer early instead of letting the loop run and fail.
        if k > len(s2):
            return False
        # 26 counters (one per lowercase letter) for what s1 contains and for what the current window contains.
        need = [0] * 26
        window = [0] * 26
        # Fill in the target signature once. "ab" and "ba" produce the same counts, which is exactly the point.
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        # Slide the right edge across s2 one character at a time.
        for i, ch in enumerate(s2):
            # The new character enters the window.
            window[ord(ch) - ord("a")] += 1
            # Once the window would exceed k characters, the character that fell off the left (index i - k) leaves it.
            if i >= k:
                window[ord(s2[i - k]) - ord("a")] -= 1
            # Comparing two 26-slot lists is constant work; equal counts means the window is a permutation of s1.
            if window == need:
                return True
        # No window ever matched the signature.
        return False
