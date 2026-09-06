def longest_palindrome(s):
    best_start, best_len = 0, 0
    for centre in range(len(s)):
        # odd-length palindromes centred on a character, then even-length ones centred between two
        for left, right in ((centre, centre), (centre, centre + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1  # the pointers overshot by one on each side
            if length > best_len:
                best_start, best_len = left + 1, length
    return s[best_start:best_start + best_len]
