# 100. Detect Squares

**Difficulty:** Medium | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #2013

## Problem

Design a data structure that stores points on the integer grid, with duplicates allowed, and answers this query: given a point `p`, how many axis-aligned squares of positive area have `p` as one corner and three previously added points as the other corners?

Implement `DetectSquares` with `add(point)`, which stores one more copy of the point, and `count(point)`, which returns the number of such squares. Each combination of stored copies counts separately: if a corner was added twice, every square through it counts twice.

## Examples

```
Input:  add([3,10]), add([11,2]), add([3,2]), count([11,10])
Output: 1             # diagonal corner (3,2) is 8 away in both x and y; (3,10) and (11,2) fill the other corners

Input:  ... then count([14,8])
Output: 0             # no stored point is the same distance away in x and in y

Input:  ... then add([11,2]), count([11,10])
Output: 2             # (11,2) now has 2 copies, so 1 × 1 × 2 squares
```

## Constraints

- `point.length == 2`
- `0 <= x, y <= 1000`
- at most `3000` calls in total to `add` and `count`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every triple of stored points to iterating only over candidate diagonal corners and multiplying three counts, with the point map and a scatter of the grid shown after every operation.

## Follow-up

- Suppose `count` is called far more often than `add`. Can you index stored points by x so that only points sharing the query's column are scanned, and what does that do to the worst case?
- What changes if squares may be rotated (any four points at equal side lengths and right angles), not just axis-aligned?
- Add a `remove(point)` operation. Which counts change, and does the diagonal-corner loop need to change at all?
