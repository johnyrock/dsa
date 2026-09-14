import heapq
from collections import Counter


class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]
