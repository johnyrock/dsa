class Solution:
    # Define the function that takes a node count and undirected edges and returns how many connected components they form.
    def count_components(self, n: int, edges: list[list[int]]) -> int:
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

        # With no edges every node is its own component, so start the count at n and lower it as components merge.
        count = n
        for a, b in edges:
            # Find the root of each endpoint's component.
            ra, rb = find(a), find(b)
            # Same root: a and b are already in one component, so this edge changes nothing. Skip it without touching count.
            if ra == rb:
                continue
            # Union by rank: attach the shorter tree under the taller one so heights stay logarithmic.
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            # Only when both trees were equally tall does the merged tree get taller.
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            # Two components became one. Decrement only on a successful merge, never for a redundant edge.
            count -= 1
        return count
