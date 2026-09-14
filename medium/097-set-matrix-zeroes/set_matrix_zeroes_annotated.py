class Solution:
    # Zero out every row and column that contains a 0, in place and with O(1) extra space.
    def set_zeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        # Row 0 and column 0 are about to be reused as marker storage, so record whether they themselves need zeroing before they get overwritten.
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
        # Pass 1: for every 0 in the interior (rows 1.., cols 1..), write a 0 into the head of its row and the head of its column. Those cells are the "this line must be zeroed" flags.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        # Pass 2: walk the interior again and zero any cell whose row flag or column flag is set. The interior is finished before row 0 / column 0 are touched, so the flags are still intact while they are read.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # Finally apply the two saved booleans. Row 0 first or column 0 first does not matter, but both must come after pass 2 or the flags would be destroyed early.
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
