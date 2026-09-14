class Solution:
    # Define the function that takes a 0/1 grid and returns the size of the largest orthogonally connected group of 1s.
    def max_area_of_island(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # The largest area seen so far. Starting at 0 also covers the all-water grid, where no island is ever measured.
        best = 0
        # Scan every cell once, top to bottom, left to right.
        for r in range(rows):
            for c in range(cols):
                # Water, or land that was already sunk as part of an earlier island: nothing to measure here.
                if grid[r][c] != 1:
                    continue
                # Sink the seed cell BEFORE pushing it so it can never be pushed a second time from a neighbour.
                grid[r][c] = 0
                # Flood fill with an explicit stack (iterative DFS). Recursion would work at 50 x 50 but the stack is the habit that scales.
                stack = [(r, c)]
                # Fresh counter for THIS island. Forgetting to reset it here makes area accumulate across islands.
                area = 0
                while stack:
                    cr, cc = stack.pop()
                    # Count a cell when it is popped. Every land cell of the island is pushed exactly once, so it is popped exactly once.
                    area += 1
                    # The four orthogonal neighbours. Diagonals do not connect land.
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        # In bounds and still land: it belongs to this island.
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            # Sink it as it is discovered, then push it so its own neighbours get explored.
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                # The island is fully sunk and fully counted; keep it only if it beats the record.
                best = max(best, area)
        # Every island was measured exactly once, on its first cell; every other cell of it was sunk before the scan reached it.
        return best
