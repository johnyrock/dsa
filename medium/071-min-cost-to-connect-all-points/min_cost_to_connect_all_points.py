import heapq


class Solution:
    def min_cost_connect_points(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        total = 0
        connected = 0
        while connected < n:
            cost, i = heapq.heappop(heap)
            if visited[i]:
                continue
            visited[i] = True
            total += cost
            connected += 1
            for j in range(n):
                if not visited[j]:
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (d, j))
        return total
