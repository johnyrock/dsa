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
| [easy/013 Maximum Depth of Binary Tree](../easy/013-maximum-depth-of-binary-tree/) | Easy | Maximum depth is one plus the taller child subtree. |
| [easy/014 Diameter of Binary Tree](../easy/014-diameter-of-binary-tree/) | Easy | Compute heights bottom-up while recording the best path through a node. |
| [easy/015 Balanced Binary Tree](../easy/015-balanced-binary-tree/) | Easy | Return a height or an unbalanced sentinel in one post-order pass. |
| [easy/016 Same Tree](../easy/016-same-tree/) | Easy | Compare values and corresponding children recursively. |
| [easy/017 Subtree of Another Tree](../easy/017-subtree-of-another-tree/) | Easy | Try each root position, then compare the candidate structure. |
| [medium/044 Binary Tree Right Side View](../medium/044-binary-tree-right-side-view/) | Medium | "Visible from the right" means "last node of its level", not "reachable by going right" |
| [medium/045 Count Good Nodes in Binary Tree](../medium/045-count-good-nodes-in-binary-tree/) | Medium | A node is good exactly when `node.val >= max(values on the path above it)`, so the… |
| [medium/046 Construct Binary Tree from Preorder and Inorder Traversal](../medium/046-construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | The first preorder value is the root |
## Common mistakes

- Comparing a BST node only to its immediate parent instead of carrying bounds from every ancestor.
- Swapping two attributes with two separate statements instead of one tuple assignment, when the swap depends on both original values.
- Recomputing a queue's length inside a level's loop instead of snapshotting it before the loop starts, which merges levels together.
- Recursing without a `None` base case, causing an `AttributeError` on leaves.
