from copy_list_with_random_pointer import Node, Solution

solution = Solution()


def build(pairs):
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rnd) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[rnd] if rnd is not None else None
    return nodes[0] if nodes else None


def serialize(head):
    nodes, index, node = [], {}, head
    while node is not None:
        index[node] = len(nodes)
        nodes.append(node)
        node = node.next
    return [[n.val, index[n.random] if n.random is not None else None] for n in nodes]


original = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
copy = solution.copy_random_list(original)
print(serialize(copy))
print(copy is not original, copy.next is not original.next)
