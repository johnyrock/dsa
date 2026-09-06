# Define the function that takes the grid of '0'/'1' characters and returns how many connected groups of '1' it holds.
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    # Scan every cell once, top to bottom, left to right.
    for r in range(rows):
        for c in range(cols):
            # Water, or land that was already sunk as part of an earlier island: nothing to do.
            if grid[r][c] != "1":
                continue
            # Unvisited land means a brand-new island. Count it once, right here.
            count += 1
            # Mark the cell as visited by turning it into water. Doing this BEFORE pushing prevents the same cell being pushed twice.
            grid[r][c] = "0"  # sink the cell so it is never counted again
            # Flood fill with an explicit stack (iterative DFS). Recursion would also work but can overflow on a 300 x 300 grid.
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                # The four orthogonal neighbours. Diagonals do not connect land.
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    # In bounds and still land: it belongs to this island.
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        # Sink it as it is discovered, then queue it so its own neighbours get explored.
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
    # Each island incremented count exactly once, on its first cell; every other cell of it was sunk before the scan reached it.
    return count
