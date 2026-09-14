from collections import deque


class Solution:
    # Define the function that takes the grid of 0/1/2 cells and returns the minutes until no fresh orange is left, or -1.
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        # Count fresh oranges up front so the loop knows when to stop and the end knows whether any were unreachable.
        fresh = 0
        # One scan: every rotten orange is a BFS source at time 0, every fresh orange is one more to rot.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        # Stop when the frontier is exhausted OR nothing fresh remains. The second condition is what keeps the count exact:
        # without it, the last wave of newly rotten oranges would be processed as an extra minute that rots nothing.
        while queue and fresh:
            # Process exactly the oranges that were rotten at the start of this minute. len(queue) is read once, before any appends.
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # The four orthogonal neighbours. Diagonal contact does not spread rot.
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    # In bounds and fresh: it rots now. Empty cells and already-rotten cells are skipped by the same test.
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Mark it rotten immediately so no other orange in this wave queues it a second time.
                        grid[nr][nc] = 2
                        fresh -= 1
                        # It becomes a source for the NEXT minute; the for-loop bound was fixed before this append.
                        queue.append((nr, nc))
            # One whole wave has spread: the clock ticks once per level, not once per orange.
            minutes += 1
        # Any fresh orange still standing could never be reached, so the task is impossible.
        return -1 if fresh else minutes
