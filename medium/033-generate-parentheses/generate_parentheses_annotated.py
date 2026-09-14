class Solution:
    # Return every string of n '(' and n ')' that is well-formed, in any order.
    def generate_parenthesis(self, n: int) -> list[str]:
        # Collected answers. Each is appended exactly once, when a path reaches full length.
        result = []
        # The string under construction, kept as a list so append/pop are O(1).
        path = []

        # open_count and close_count are how many of each bracket path currently holds.
        def backtrack(open_count: int, close_count: int) -> None:
            # A well-formed string of n pairs has exactly 2n characters; once we are there, record it.
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            # We may open another bracket only while fewer than n have been opened.
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                # Undo the choice so the sibling branch below starts from the same prefix.
                path.pop()
            # We may close only if there is an unmatched '(' to close: close_count < open_count.
            # This single guard is what keeps every prefix valid and prunes the invalid strings.
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        # Start from the empty string with nothing opened or closed.
        backtrack(0, 0)
        return result
