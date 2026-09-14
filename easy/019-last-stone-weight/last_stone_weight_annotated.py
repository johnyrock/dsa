import heapq


class Solution:
    # Repeatedly smash the two heaviest stones.
    def last_stone_weight(self, stones: list[int]) -> int:
        # Negate weights because Python's heapq is a min-heap.
        heap = [-stone for stone in stones]
        # Build the heap once from every stone.
        heapq.heapify(heap)
        # A smash needs two stones.
        while len(heap) > 1:
            # Negate again to recover the heaviest remaining stone.
            first = -heapq.heappop(heap)
            # The next pop is the second-heaviest stone.
            second = -heapq.heappop(heap)
            # Unequal stones leave a stone with the weight difference.
            if first != second:
                heapq.heappush(heap, second - first)
        # Convert the final negated weight back, or return zero if nothing remains.
        return -heap[0] if heap else 0
