import heapq


class Solution:
    # Return the kth largest value in nums, counting duplicates separately.
    def find_kth_largest(self, nums: list[int], k: int) -> int:
        # A min-heap that will hold the k largest values seen so far. Its root is the smallest of those,
        # which after the last push is exactly the kth largest overall.
        heap = []
        # Visit every number once.
        for num in nums:
            # Push first, so the newcomer is compared against the current smallest survivor by the heap itself.
            heapq.heappush(heap, num)
            # If the heap now holds k + 1 values, the smallest of them is not among the k largest: evict it.
            if len(heap) > k:
                heapq.heappop(heap)
        # The heap holds exactly the k largest values, and a min-heap's root is the smallest of them.
        return heap[0]
