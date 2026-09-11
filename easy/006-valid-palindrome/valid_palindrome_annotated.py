class Solution:
    # Define the function that takes the string and returns True when it is a palindrome under the alphanumeric-only, case-insensitive rules.
    def is_palindrome(self, s: str) -> bool:
        # Put one pointer on the first character and one on the last. They will walk toward each other and meet in the middle.
        left, right = 0, len(s) - 1
        # Keep going while the two pointers still have ground between them. Once they meet or cross, every pair has been checked. An empty string never enters the loop, so it returns True.
        while left < right:
            # Slide the left pointer forward over anything that is not a letter or digit: spaces, commas, apostrophes. The `left < right` guard stops it from running past the right pointer on a string with no alphanumerics at all.
            while left < right and not s[left].isalnum():
                left += 1
            # Do the mirror image on the right, sliding backwards over the junk, guarded the same way so the two pointers can never swap past each other.
            while left < right and not s[right].isalnum():
                right -= 1
            # Both pointers now sit on real characters. Lowercase each one so 'N' and 'n' compare equal, and if they differ the string cannot be a palindrome.
            if s[left].lower() != s[right].lower():
                # A single mismatched pair is enough to decide the whole question, so stop immediately.
                return False
            # The pair matched, so step the left pointer inward to the next candidate.
            left += 1
            # And step the right pointer inward too, shrinking the window from both ends.
            right -= 1
        # The pointers met without ever finding a mismatch, so every mirrored pair agreed and the string is a palindrome.
        return True
