import heapq
from collections import Counter, deque


class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1
            if heap:
                remaining = heapq.heappop(heap) + 1
                if remaining:
                    cooldown.append((time + n, remaining))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
        return time
