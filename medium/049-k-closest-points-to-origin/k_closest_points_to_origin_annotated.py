import heapq


class Solution:
    # Return the k points nearest to (0, 0). Order of the output does not matter.
    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # The heap will hold at most k entries: the k closest points seen so far.
        heap = []
        # Visit every point exactly once.
        for x, y in points:
            # Push the NEGATED squared distance so that heapq's min-heap behaves as a max-heap:
            # the root is then the FARTHEST of the kept points, which is the one to discard.
            # The square root is skipped because it does not change the ordering.
            # x and y ride along in the tuple so the point can be rebuilt at the end.
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            # If the push made the heap one too large, evict the root, i.e. the farthest of the k + 1.
            if len(heap) > k:
                heapq.heappop(heap)
        # Whatever survived is exactly the k closest points; drop the distance and rebuild the pairs.
        return [[x, y] for _, x, y in heap]
