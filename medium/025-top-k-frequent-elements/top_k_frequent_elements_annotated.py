import heapq
from collections import Counter


class Solution:
    # Return the k values that occur most often in nums. Any order is accepted, and the answer is guaranteed unique.
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # One pass to count every value: {value: how many times it appears}. This is the only place nums is read.
        counts = Counter(nums)
        # A min-heap that will hold at most k (count, value) pairs. Its root is always the LEAST frequent of the survivors.
        heap = []
        # Walk the distinct values, not nums itself, so the loop runs once per distinct value.
        for num, count in counts.items():
            # Push count first so the heap orders by frequency; the value rides along as a tiebreaker and payload.
            heapq.heappush(heap, (count, num))
            # If the heap has grown to k + 1 entries, evict the root: the smallest count in the heap can never be in the top k.
            if len(heap) > k:
                heapq.heappop(heap)
        # Whatever survived the evictions is exactly the k most frequent values; drop the counts and return the values.
        return [num for _, num in heap]
