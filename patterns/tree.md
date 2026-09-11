# Tree Traversal

## When to use

- Any problem operating on a binary tree's structure: inverting, validating, searching, or transforming it.
- Recursion is the default tool — trees are naturally recursive (a tree is a node plus two smaller trees).
- Prefer BFS (a queue) over DFS (recursion) when the problem is about *levels* or the shortest number of hops; prefer DFS when it's about paths, ancestry, or ordering constraints (BST bounds, in-order sequence).

## Templates

**DFS, top-down (bounds/state passed into the recursion):**

```python
def dfs(node, low, high):
    if node is None:
        return True
    if not (low < node.val < high):
        return False
    return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
```

**DFS, bottom-up (combine children's results):**

```python
def dfs(node):
    if node is None:
        return None
    left, right = dfs(node.right), dfs(node.left)  # invert example
    node.left, node.right = left, right
    return node
```

**BFS, level by level:**

```python
from collections import deque
queue = deque([root])
while queue:
    level = []
    for _ in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
```

**In-order traversal (BST values in ascending order), iterative:**

```python
stack = []
node = root
while stack or node:
    while node:
        stack.append(node)
        node = node.left
    node = stack.pop()
    # visit node.val here, in ascending order
    node = node.right
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/011 Invert Binary Tree](../easy/011-invert-binary-tree/) | Easy | post-order swap of both children's already-inverted results |
| [medium/014 Binary Tree Level Order Traversal](../medium/014-binary-tree-level-order-traversal/) | Medium | BFS, snapshot queue length to mark level boundaries |
| [medium/015 Validate Binary Search Tree](../medium/015-validate-binary-search-tree/) | Medium | carry an inherited (low, high) bound down the recursion |
| [medium/016 Lowest Common Ancestor of a BST](../medium/016-lowest-common-ancestor-of-a-bst/) | Medium | walk down; the split point where p and q diverge is the LCA |
| [medium/017 Kth Smallest Element in a BST](../medium/017-kth-smallest-element-in-a-bst/) | Medium | iterative in-order traversal, stop at the k-th visit |
| [medium/023 Serialize and Deserialize Binary Tree](../medium/023-serialize-and-deserialize-binary-tree/) | Medium | pre-order + explicit null markers make the encoding unambiguous |

## Common mistakes

- Comparing a BST node only to its immediate parent instead of carrying bounds from every ancestor.
- Swapping two attributes with two separate statements instead of one tuple assignment, when the swap depends on both original values.
- Recomputing a queue's length inside a level's loop instead of snapshotting it before the loop starts, which merges levels together.
- Recursing without a `None` base case, causing an `AttributeError` on leaves.
