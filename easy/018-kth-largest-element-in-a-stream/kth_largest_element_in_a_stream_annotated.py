import heapq


class KthLargest:
    # Keep exactly the k largest values seen so far in a min-heap.
    def __init__(self, k: int, nums: list[int]) -> None:
        # Store k because add needs the same size limit.
        self.k = k
        # Copy the input so constructing this object does not mutate the caller's list.
        self.heap = nums[:]
        # Arrange the values so the smallest kept value is at index zero.
        heapq.heapify(self.heap)
        # Discard every value that cannot be among the k largest.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    # Add one stream value and return the current k-th largest.
    def add(self, val: int) -> int:
        # Insert the new candidate into the kept values.
        heapq.heappush(self.heap, val)
        # If too many are kept, remove the smallest one.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The smallest of the k kept values is precisely the k-th largest overall.
        return self.heap[0]
