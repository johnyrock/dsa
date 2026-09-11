from clone_graph import Solution, Node

a, b, c = Node(1), Node(2), Node(3)
a.neighbors = [b, c]
b.neighbors = [a, c]
c.neighbors = [a, b]

clone = Solution().clone_graph(a)
print(clone.val, [n.val for n in clone.neighbors])
print(clone is a)
