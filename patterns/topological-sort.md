# Topological Sort

## When to use

- Ordering tasks/courses/steps that have "must come before" dependencies.
- Detecting whether a dependency graph has a cycle (which makes a valid order impossible).
- The graph is directed; an undirected graph has no meaningful topological order.

## Templates

**Kahn's algorithm (BFS via indegree):**

```python
from collections import deque

graph = [[] for _ in range(n)]
indegree = [0] * n
for a, b in edges:      # b must come before a
    graph[b].append(a)
    indegree[a] += 1

queue = deque(i for i in range(n) if indegree[i] == 0)
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

has_cycle = len(order) != n
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/018 Course Schedule](../medium/018-course-schedule/) | Medium | BFS with indegree counts; a cycle leaves nodes permanently stuck above indegree 0 |

## Common mistakes

- Building the edge in the wrong direction — a pair `[a, b]` meaning "b before a" is an edge `b -> a` (b unlocks a), not `a -> b`.
- Forgetting to seed the queue with *every* node that starts at indegree 0, not just ones discovered later.
- Checking whether the queue emptied instead of comparing the count of processed nodes to the total — both an early cycle and a full completion empty the queue eventually, but only the count distinguishes them.
