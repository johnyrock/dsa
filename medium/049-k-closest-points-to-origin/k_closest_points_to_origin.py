import heapq


class Solution:
    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]
