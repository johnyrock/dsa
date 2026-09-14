class Solution:
    # Define the function that takes a node count and undirected edges and returns whether they form exactly one tree.
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        # A tree on n nodes has exactly n - 1 edges. Fewer means disconnected, more means a cycle. Reject early either way.
        if len(edges) != n - 1:
            return False
        # Union-find: parent[x] points toward the root of x's component; every node starts as its own root.
        parent = list(range(n))
        # rank[x] is an upper bound on the height of the tree rooted at x; used to keep the forest shallow.
        rank = [0] * n

        # Follow parent pointers up to the root. Path halving (point x at its grandparent as we go) flattens the chain for next time.
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            # Find the root of each endpoint's component.
            ra, rb = find(a), find(b)
            # Same root means a and b are already connected, so this edge closes a cycle. A tree has none.
            if ra == rb:
                return False
            # Union by rank: attach the shorter tree under the taller one so heights stay logarithmic.
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            # Only when both trees were equally tall does the merged tree get taller.
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        # n - 1 edges and no cycle means every edge merged two components: n components became 1, so it is connected.
        return True
