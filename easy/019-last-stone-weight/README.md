# 019. Last Stone Weight

**Difficulty:** Easy | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #1046

## Problem

You are given an array `stones` where `stones[i]` is the weight of the i-th stone. Repeatedly take the two heaviest stones `x <= y` and smash them: if `x == y` both are destroyed, otherwise the lighter one is destroyed and the heavier one becomes `y - x`.

Return the weight of the last remaining stone, or `0` if none are left.

## Examples

```
Input:  stones = [2,7,4,1,8,1]
Output: 1             # 8,7 -> 1: [2,4,1,1,1]; 4,2 -> 2: [2,1,1,1]; 2,1 -> 1: [1,1,1]; 1,1 -> gone: [1]

Input:  stones = [1]
Output: 1             # nothing to smash against

Input:  stones = [3,3]
Output: 0             # equal stones annihilate; the array ends empty
```

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- With `stones.length <= 30`, a sort-then-`bisect.insort` loop is also fast. At what input size does the heap's O(log n) per smash start to matter?
- Last Stone Weight II (LeetCode #1049) lets you pick *any* two stones and asks for the smallest possible final weight. Why does the greedy heap stop working, and what replaces it?
- Python's `heapq` is a min-heap only. What are the alternatives to negating every value, and what does each cost?
