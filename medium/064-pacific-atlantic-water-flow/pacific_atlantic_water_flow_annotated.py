class Solution:
    # Define the function that takes the height grid and returns every cell whose water can reach both oceans.
    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        # One traversal, run once per ocean: from the ocean's edge cells, walk UPHILL (or level) through the grid.
        # Every cell reached this way can, in reverse, drain downhill to that ocean.
        def reach(starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
            # The visited set doubles as the answer. Seeding it with the starts also de-duplicates the shared corner.
            seen = set(starts)
            # Iterative DFS with an explicit stack; recursion would hit the limit on a 200 x 200 all-equal grid.
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                # The four orthogonal neighbours. Water does not move diagonally.
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    # In bounds, not yet reached, and at least as high as the current cell: water from there could flow HERE, so it reaches the ocean too.
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        # Mark on push so no cell is pushed twice.
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        # Pacific touches the left column and the top row.
        pacific = reach([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        # Atlantic touches the right column and the bottom row.
        atlantic = reach([(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)])
        # A cell drains to both oceans exactly when both uphill searches reached it. Scan order gives a deterministic row-major result.
        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]
