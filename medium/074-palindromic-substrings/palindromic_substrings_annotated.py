class Solution:
    # Count every substring of s that reads the same forwards and backwards. Substrings at different positions count separately even if their text is identical.
    def count_substrings(self, s: str) -> int:
        # Running count of palindromic substrings found so far.
        total = 0
        # Every palindrome has a centre. There are len(s) character-centres (odd length) and len(s) - 1 gap-centres (even length).
        for centre in range(len(s)):
            # (centre, centre) grows an odd-length palindrome from one character; (centre, centre + 1) grows an even-length one from the gap after it.
            for left, right in ((centre, centre), (centre, centre + 1)):
                # Keep stepping outward while both ends are inside the string and match. Bounds are checked first so s[-1] never wraps around.
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    # Each successful match is one more palindrome: s[left:right + 1]. Count it before growing further.
                    total += 1
                    # Widen by one on each side and test again.
                    left -= 1
                    right += 1
        # Every palindrome was counted exactly once, from its own centre.
        return total
