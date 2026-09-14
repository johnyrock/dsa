# 064. Pacific Atlantic Water Flow

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #417

## Problem

There is an `m × n` island represented by `heights`, where `heights[r][c]` is the height of the cell. The Pacific Ocean touches the island's top and left edges, and the Atlantic Ocean touches the bottom and right edges.

Rain water flows from a cell to a 4-directionally adjacent cell whose height is less than or equal to the current cell's height, and from any edge cell into the ocean that edge touches. Return the list of coordinates `[r, c]` of every cell from which water can flow to *both* oceans, in any order.

## Examples

```
Input:  heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4],
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
                      # (2, 2) at height 5 drains up-left through 3, 2 to the Pacific and down through 1 to the Atlantic

Input:  heights = [[1]]
Output: [[0,0]]       # a single cell touches both oceans

Input:  heights = [
  [1, 1],
  [1, 1],
]
Output: [[0,0],[0,1],[1,0],[1,1]]
                      # all equal: water moves anywhere, every cell reaches both
```

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from tracing water downhill from every cell to two uphill searches that start at the oceans and meet in the middle, with complexity.

## Follow-up

- Water can only flow to a *strictly* lower neighbour. Which single character changes, and why does the `[[1, 1], [1, 1]]` example now return an empty list?
- A third ocean touches only the cell `(m - 1, 0)`. How does the solution generalise, and what is the cost of each added ocean?
- Return the cells reachable from the Pacific but *not* the Atlantic. Which line changes?
