from collections import deque


class Solution:
    def walls_and_gates(self, rooms: list[list[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
