class Solution:
    # Return every element of the m x n matrix in clockwise spiral order, starting at the top-left corner.
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        # The output list; every cell is appended exactly once.
        result = []
        # Row bounds of the part of the matrix not yet visited (inclusive on both ends).
        top, bottom = 0, len(matrix) - 1
        # Column bounds of the unvisited part (inclusive on both ends).
        left, right = 0, len(matrix[0]) - 1
        # Keep peeling layers while the unvisited rectangle still has at least one row and one column.
        while top <= bottom and left <= right:
            # Walk the top row left to right, then shrink the rectangle from the top.
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            # Walk the right column downward from the new top, then shrink from the right.
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            # After shrinking top, the rectangle may have no rows left. Without this check a single remaining row would be read twice, once forward and once backward.
            if top <= bottom:
                # Walk the bottom row right to left, then shrink from the bottom.
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            # Same guard for a single remaining column: skip the upward walk if the right column already crossed the left one.
            if left <= right:
                # Walk the left column upward from the new bottom to the new top, then shrink from the left.
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
        # All four bounds have crossed, so every cell has been emitted.
        return result
