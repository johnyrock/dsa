class Solution:
    # Define the function that takes a string and returns the length of its longest run of distinct characters.
    def length_of_longest_substring(self, s: str) -> int:
        # For each character, remember the index where it was last seen. This is what lets the window jump instead of crawl.
        last_seen = {}  # char -> most recent index where it appeared
        # left is the start of the current window. Everything in s[left:right+1] is guaranteed distinct.
        left = 0        # start of the current window with no repeats
        best = 0
        # right walks forward one character at a time; each character enters the window exactly once.
        for right, ch in enumerate(s):
            # A repeat only matters if its previous occurrence is inside the current window. An occurrence to the left of `left` was already cut off and can be ignored.
            if ch in last_seen and last_seen[ch] >= left:
                # Jump the left edge to just past the previous occurrence. Everything between the old left and there is dropped in one move.
                left = last_seen[ch] + 1
            # Record this occurrence, whether or not the window moved.
            last_seen[ch] = right
            # The window is now valid, so its length is a candidate answer.
            best = max(best, right - left + 1)
        # best is the longest valid window seen at any point; for the empty string the loop never runs and it stays 0.
        return best
