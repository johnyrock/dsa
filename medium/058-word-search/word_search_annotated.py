class Solution:
    # Return True if word can be spelled by a path of adjacent cells, each used at most once.
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Try to match word[k:] starting at cell (r, c). Returns True as soon as one full match is found.
        def dfs(r: int, c: int, k: int) -> bool:
            # Every letter has been matched (k ran past the end), so the path spelling word is complete.
            if k == len(word):
                return True
            # Off the board, or the cell holds the wrong letter (a "#" from the current path also fails here): dead end.
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False
            # Mark this cell as part of the current path so the four recursive calls cannot step back onto it.
            saved = board[r][c]
            board[r][c] = "#"
            # Try to match the next letter from each orthogonal neighbour. `or` stops at the first success.
            found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1)
                     or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
            # Undo the mark so this cell is available to paths that start elsewhere or arrive by another route.
            board[r][c] = saved
            return found

        # The word can start anywhere, so launch a search from every cell.
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
