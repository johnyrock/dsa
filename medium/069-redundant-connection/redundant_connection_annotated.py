class Solution:
    # Return the edge whose addition closes a cycle in a graph that is otherwise a tree.
    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        # Nodes are labelled 1..n and there are exactly n edges, so index n must exist; that is why the array has n + 1 slots (slot 0 is unused).
        # Every node starts as its own root, meaning n separate components.
        parent = list(range(len(edges) + 1))

        # Follow parent pointers up until a node points at itself; that self-loop node is the component's representative.
        def find(x: int) -> int:
            while parent[x] != x:
                # Path halving: point x at its grandparent so the next lookup skips a level. Keeps chains short without a rank array.
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # Process edges in input order, so the first edge that closes a cycle is the last one in the cycle; that is the edge the problem wants.
        for a, b in edges:
            # Find the representative of each endpoint before touching anything.
            root_a, root_b = find(a), find(b)
            # Same representative means a and b were already connected by earlier edges; this edge adds a second path, i.e. a cycle.
            if root_a == root_b:
                return [a, b]
            # Different components: merge them by hanging one root under the other. Linking roots (not a and b themselves) keeps every node of b's tree reachable.
            parent[root_b] = root_a
        # The problem guarantees exactly one extra edge, so this line is never reached.
        return []
