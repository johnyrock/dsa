class Solution:
    # Return whether target appears in a matrix whose rows are sorted and whose every row
    # starts after the previous row ends: reading it row by row gives one sorted list.
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # Treat the whole matrix as one flat sorted array of rows * cols entries and
        # binary search over the flat indices 0 .. rows * cols - 1, inclusive on both ends.
        lo, hi = 0, rows * cols - 1
        # <= keeps a one-element window alive; with < the last candidate is never examined.
        while lo <= hi:
            mid = (lo + hi) // 2
            # Convert the flat index back to a cell. Dividing by cols (the row length) gives the row,
            # the remainder gives the column. Dividing by rows would be wrong for non-square matrices.
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            # Everything at or before mid is too small: discard the left half including mid.
            if value < target:
                lo = mid + 1
            # Everything at or after mid is too large: discard the right half including mid.
            else:
                hi = mid - 1
        # The window closed without a hit, so target is not in the matrix.
        return False
