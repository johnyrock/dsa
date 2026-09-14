import heapq


class Solution:
    # Return the weight of a minimum spanning tree over the points, with Manhattan distance as the edge weight.
    def min_cost_connect_points(self, points: list[list[int]]) -> int:
        n = len(points)
        # visited[i] is True once point i has been absorbed into the growing tree.
        visited = [False] * n
        # The heap holds (cost, point) candidate edges that lead from the tree to a point. Point 0 is the seed and joins for free.
        heap = [(0, 0)]
        total = 0
        # Count of points in the tree; the loop ends once all n are in, even if stale entries remain in the heap.
        connected = 0
        while connected < n:
            # Cheapest known edge out of the tree. With a complete graph the heap is never empty before all points are connected.
            cost, i = heapq.heappop(heap)
            # A point can be pushed many times, once per tree point that saw it. Only the first (cheapest) pop counts; later ones are stale.
            if visited[i]:
                continue
            # Absorb the point: pay the edge that reached it and count it.
            visited[i] = True
            total += cost
            connected += 1
            # Offer an edge from the new point to every point still outside the tree. This is the "relax" step of Prim's.
            for j in range(n):
                if not visited[j]:
                    # Manhattan distance, as the problem defines the cost. Not Euclidean.
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (d, j))
        return total
