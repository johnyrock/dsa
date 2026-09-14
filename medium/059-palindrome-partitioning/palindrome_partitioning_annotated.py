class Solution:
    # Return every way to cut s into consecutive pieces that are all palindromes.
    def partition(self, s: str) -> list[list[str]]:
        # The partitions found so far.
        result = []
        # The pieces of the partition currently being built, left to right.
        path = []

        # Is s[left..right] (inclusive) a palindrome? Compare from both ends inward.
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # start: the index where the next piece must begin. Everything before it is already cut into palindromes in path.
        def backtrack(start: int) -> None:
            # The next piece would begin past the end, so every character is accounted for: path is a complete partition. Copy it, because path keeps mutating.
            if start == len(s):
                result.append(path[:])
                return
            # Try every possible end for the piece that begins at start.
            for end in range(start, len(s)):
                # Only a palindrome may be a piece; any other candidate is discarded before recursing.
                if is_palindrome(start, end):
                    # Choose the piece s[start..end] (end is inclusive, so the slice needs end + 1).
                    path.append(s[start:end + 1])
                    # The next piece begins right after this one.
                    backtrack(end + 1)
                    # Undo the choice so the next candidate end starts from the same prefix.
                    path.pop()

        # Start cutting from the first character.
        backtrack(0)
        return result
