# 071. Min Cost to Connect All Points

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #1584

## Problem

You are given `points`, a list of integer coordinates `[x, y]` on a 2D plane. Connecting two points costs their Manhattan distance, `|x1 - x2| + |y1 - y2|`.

Return the minimum total cost to connect all the points so that there is exactly one simple path between every pair, i.e. the weight of a minimum spanning tree.

## Examples

```
Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20            # edges 0-1 (4), 1-3 (3), 3-4 (4), 1-2 (9); 4 + 3 + 4 + 9 = 20

Input:  points = [[3,12],[-2,5],[-4,1]]
Output: 18            # 0-1 costs 12, 1-2 costs 6; the 0-2 edge (18) is never needed

Input:  points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4             # four points, three unit-length edges, plus one of length 2
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- all `(xi, yi)` are distinct

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting all n² edges for Kruskal to Prim's algorithm grown from a min-heap, with complexity.

## Follow-up

- Prim's with a heap is O(n² log n) here because the graph is complete. An O(n²) version keeps a `min_dist` array and scans it instead of using a heap; when is that the better choice?
- Kruskal's algorithm would sort all `n(n-1)/2` edges and use union-find. On which input sizes does that beat Prim's?
- If a specific pair of points must *not* be connected directly, which line changes?
