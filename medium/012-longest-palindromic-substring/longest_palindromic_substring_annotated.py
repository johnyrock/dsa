class Solution:
    # Define the function that takes a string and returns its longest palindromic substring.
    def longest_palindrome(self, s: str) -> str:
        # Track the answer as a start index and a length rather than slicing on every improvement.
        best_start, best_len = 0, 0
        # Every palindrome has a centre. Try each character as a centre, and each gap between characters too.
        for centre in range(len(s)):
            # (centre, centre) grows an odd-length palindrome from one character; (centre, centre + 1) grows an even-length one from a pair.
            for left, right in ((centre, centre), (centre, centre + 1)):
                # Expand outward while both pointers are in bounds and the characters match. Every step confirms a palindrome two longer than before.
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                # The loop stops one step too far on each side, so the palindrome is s[left + 1 : right], whose length is right - left - 1.
                length = right - left - 1  # the pointers overshot by one on each side
                if length > best_len:
                    best_start, best_len = left + 1, length
        # Slice once at the end. For a non-empty string best_len is at least 1, because every single character is a palindrome.
        return s[best_start:best_start + best_len]
