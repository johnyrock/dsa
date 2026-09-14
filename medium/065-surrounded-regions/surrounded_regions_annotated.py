class Solution:
    # Define the function. It mutates the board in place and returns nothing, matching the LeetCode signature.
    def solve(self, board: list[list[str]]) -> None:
        # Cache the dimensions once; the bounds check inside the flood fill uses them on every neighbour.
        rows, cols = len(board), len(board[0])

        # Flood fill from one border 'O', relabelling every 'O' it can reach as 'T' (temporarily safe).
        def mark_safe(r: int, c: int) -> None:
            # An explicit stack instead of recursion: a 200 x 200 board of all 'O' is one region 40,000 cells deep.
            stack = [(r, c)]
            # Mark the seed before pushing it so it can never be pushed again from a neighbour.
            board[r][c] = "T"
            while stack:
                cr, cc = stack.pop()
                # Only the four orthogonal neighbours count; diagonal 'O's are not connected.
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    # Check both bounds explicitly: a negative index would silently wrap to the last row or column.
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        # Mark on push, not on pop, so a cell reachable from two directions is pushed only once.
                        board[nr][nc] = "T"
                        stack.append((nr, nc))

        # Seed the flood fill from every 'O' on the left and right edges.
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    mark_safe(r, c)
        # And from every 'O' on the top and bottom edges. A corner is visited twice, but after the first visit it is 'T', not 'O'.
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    mark_safe(r, c)

        # Second pass: any 'O' still standing was never reached from a border, so it is surrounded and gets captured.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                # Every 'T' touched a border; restore it to 'O'.
                elif board[r][c] == "T":
                    board[r][c] = "O"
