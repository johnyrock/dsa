class Solution:
    # Rotate the n x n matrix 90 degrees clockwise in place; nothing is returned, the caller's list is mutated.
    def rotate(self, matrix: list[list[int]]) -> None:
        # The matrix is square, so one dimension is enough for both loops.
        n = len(matrix)
        # Phase 1, transpose: swap every cell above the main diagonal with its mirror below it.
        for r in range(n):
            # Start at r + 1, not 0: visiting (r, c) and later (c, r) would swap each pair twice and undo the transpose.
            for c in range(r + 1, n):
                # Tuple assignment swaps matrix[r][c] and matrix[c][r] without a temporary.
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # Phase 2, reverse each row: the transpose turned rows into columns read top-to-bottom; reversing them makes the read bottom-to-top, which is exactly a clockwise turn.
        for row in matrix:
            # list.reverse() is in place, so the rotation uses O(1) extra space.
            row.reverse()
