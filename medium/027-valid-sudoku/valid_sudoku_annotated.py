class Solution:
    # Decide whether the filled cells of a 9x9 board obey the three sudoku rules. Empty cells are '.', and the board does not have to be solvable.
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        # One set of seen digits per row. rows[r] answers "has this digit already appeared in row r?" in O(1).
        rows = [set() for _ in range(9)]
        # One set per column, indexed by c.
        cols = [set() for _ in range(9)]
        # One set per 3x3 box, indexed 0..8 left-to-right, top-to-bottom.
        boxes = [set() for _ in range(9)]
        # Visit every cell exactly once in reading order.
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                # Empty cells impose no constraint and must not be recorded, or the second '.' in a row would look like a duplicate.
                if value == ".":
                    continue
                # Map (r, c) to its box: r // 3 picks the band (0, 1, 2), c // 3 picks the stack, and *3 spreads the bands so the nine boxes get nine distinct numbers.
                box = (r // 3) * 3 + c // 3
                # A digit already seen in this row, this column, or this box is a rule violation; there is no need to look further.
                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False
                # Record the digit in all three groups it belongs to, so later cells in the same row, column, or box will catch a repeat.
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
        # Every filled cell was consistent with everything before it, so the board is valid.
        return True
