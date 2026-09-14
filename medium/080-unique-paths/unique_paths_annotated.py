class Solution:
    # Count the paths from the top-left to the bottom-right of an m x n grid moving only right or down.
    def unique_paths(self, m: int, n: int) -> int:
        # The first row has exactly one path to every cell (keep moving right), so seed a single row of ones. This row is reused for every subsequent row of the grid.
        row = [1] * n
        # Rows 1 through m - 1 each derive from the row above. Row 0 is the seed, so start at 1.
        for _ in range(1, m):
            # Column 0 stays 1 (only reachable by moving straight down), so start at column 1.
            for c in range(1, n):
                # Before this update, row[c] still holds the value from the row above (paths arriving from above); row[c - 1] is already this row's value (paths arriving from the left). Their sum is the count for this cell.
                row[c] += row[c - 1]
        # After the last row is built, its final cell is the bottom-right corner.
        return row[n - 1]
