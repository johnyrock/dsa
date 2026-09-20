class Solution:
    # Define the function that takes a string and returns its run-length encoding, count first, runs capped at 9.
    def compressed_string(self, word: str) -> str:
        # Collect the pieces in a list and join once at the end; repeated string += would copy the growing result every time.
        parts = []
        # i marks the start of the run currently being measured.
        i = 0
        # Each pass of the outer loop consumes exactly one run, so it stops when i walks off the end.
        while i < len(word):
            # j scans forward from i; the run is word[i:j] and its length is j - i.
            j = i
            # Extend the run while there is a character, it matches the run's first character, and the run is still shorter than 9.
            while j < len(word) and word[j] == word[i] and j - i < 9:
                j += 1
            # Emit the count before the character: "2a", not "a2". The count is a single digit because of the cap.
            parts.append(str(j - i) + word[i])
            # The next run starts exactly where this one stopped; a run cut at 9 continues with the same character.
            i = j
        # One O(n) join builds the answer.
        return "".join(parts)
