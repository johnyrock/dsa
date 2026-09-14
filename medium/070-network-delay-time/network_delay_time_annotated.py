import heapq
from collections import defaultdict


class Solution:
    # Return how long until every node hears a signal sent from k, or -1 if some node never does.
    def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
        # Adjacency list: graph[u] holds (v, w) for every directed edge u -> v of weight w. defaultdict avoids a KeyError for nodes with no outgoing edges.
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist holds only settled nodes: node -> shortest time. A node enters exactly once, the first time it is popped.
        dist = {}
        # The min-heap is keyed on (time, node), so the smallest time is always on top. The source is reached at time 0.
        heap = [(0, k)]
        while heap:
            # Pop the unsettled node with the smallest tentative time. With non-negative weights nothing later can beat it.
            d, node = heapq.heappop(heap)
            # Stale entry: the node was already settled via a shorter path that was popped earlier. Skip it.
            if node in dist:
                continue
            # First time seeing this node, so d is its final shortest time.
            dist[node] = d
            # Relax every outgoing edge: a neighbour can be reached at d + w. Pushing without checking for a better existing entry is fine because stale entries are filtered on pop.
            for nxt, w in graph[node]:
                if nxt not in dist:
                    heapq.heappush(heap, (d + w, nxt))

        # Every node must be reachable. If so the answer is the slowest arrival, since all signals travel in parallel.
        return max(dist.values()) if len(dist) == n else -1
