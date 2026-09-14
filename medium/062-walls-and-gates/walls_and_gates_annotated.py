from collections import deque


class Solution:
    # Define the function that fills every empty room with its distance to the nearest gate, in place.
    def walls_and_gates(self, rooms: list[list[int]]) -> None:
        # An empty grid has no rows to index; return before len(rooms[0]) would raise.
        if not rooms or not rooms[0]:
            return
        # The sentinel LeetCode uses for "empty room". It is also the "unvisited" marker for the search.
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        # Seed the queue with EVERY gate at once. All gates are distance 0, so they form the first BFS layer together.
        queue = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        # Plain BFS: cells come off the queue in non-decreasing distance order.
        while queue:
            r, c = queue.popleft()
            # The four orthogonal neighbours. Diagonal moves are not allowed.
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                # Only an in-bounds cell that is still INF is an unvisited empty room. Walls (-1), gates (0) and rooms already filled are all skipped by the same test.
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    # The first time BFS reaches a room is via a shortest path, so this value is final. Writing it now also marks the room visited.
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
        # Rooms no gate can reach were never written and still hold INF, which is the required output for them.
