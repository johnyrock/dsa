# Graph Traversal (BFS / DFS)

## When to use

- Anything about connectivity or reachability: components, islands, "can A reach B", shortest path in unweighted graphs.
- The graph may be implicit: a grid where neighbours are the four adjacent cells, a word ladder where neighbours differ by one letter.
- Count connected components by scanning all nodes and traversing from each unvisited one.

## Templates

**Iterative DFS with an explicit stack (grid flood fill):**

```python
count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "1":
            continue
        count += 1
        grid[r][c] = "0"                  # mark visited on push
        stack = [(r, c)]
        while stack:
            cr, cc = stack.pop()
            for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    stack.append((nr, nc))
```

**BFS with a queue (use when distance or level order matters):**

```python
from collections import deque
queue = deque([start])
seen = {start}
while queue:
    node = queue.popleft()
    for nxt in neighbours(node):
        if nxt not in seen:
            seen.add(nxt)
            queue.append(nxt)
```

Swap the stack for a queue and DFS becomes BFS; for counting components either works.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/010 Number of Islands](../medium/010-number-of-islands/) | Medium | scan cells, on unvisited land count one and flood-fill it to water |

## Common mistakes

- Recursive DFS on large inputs. A 300 x 300 grid can recurse 90,000 deep, past Python's limit. Use an explicit stack or a queue.
- Marking visited on pop instead of on push, which lets the same node sit in the stack many times.
- Missing the lower bound in the range check. `grid[-1]` wraps around in Python instead of raising.
- Counting diagonal neighbours when only orthogonal moves connect.
- Comparing to the integer `1` when the grid holds the string `'1'`.
