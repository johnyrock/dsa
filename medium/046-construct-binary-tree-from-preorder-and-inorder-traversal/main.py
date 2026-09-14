from construct_binary_tree_from_preorder_and_inorder_traversal import Solution


def to_list(root):
    values, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


solution = Solution()
print(to_list(solution.build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
print(to_list(solution.build_tree([-1], [-1])))
