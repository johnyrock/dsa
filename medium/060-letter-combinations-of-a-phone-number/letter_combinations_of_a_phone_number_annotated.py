class Solution:
    # Return every string that spells digits on a phone keypad, one letter per digit, in order.
    def letter_combinations(self, digits: str) -> list[str]:
        # No digits means no strings at all. Without this guard the recursion records "" once and returns [""].
        if not digits:
            return []
        # The keypad: each digit owns 3 letters, except 7 and 9 which own 4.
        keypad = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        # Completed strings.
        result = []
        # One chosen letter per digit handled so far.
        path = []

        # index: which digit we are choosing a letter for. Everything before index already has its letter in path.
        def backtrack(index: int) -> None:
            # Every digit has a letter, so path is a complete string. Join it (path is a list of characters) and record it.
            if index == len(digits):
                result.append("".join(path))
                return
            # Try each letter on the current digit's key, in keypad order so the output is lexicographic.
            for letter in keypad[digits[index]]:
                # Choose this letter for position index.
                path.append(letter)
                # Move on to the next digit.
                backtrack(index + 1)
                # Undo the choice so the next letter of this key starts from the same prefix.
                path.pop()

        # Start with the first digit and nothing chosen.
        backtrack(0)
        return result
