# 025. Top K Frequent Elements

**Difficulty:** Medium | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #347

## Problem

You are given an integer array `nums` and an integer `k`. Return the `k` values that appear most often in `nums`.

The answer is guaranteed to be unique (there is never a tie at the k-th place that matters), and you may return it in any order.

## Examples

```
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]         # counts are 1→3, 2→2, 3→1; the two largest counts belong to 1 and 2

Input:  nums = [1], k = 1
Output: [1]           # one value, one slot

Input:  nums = [4,4,4,5,5,6,6,7], k = 3
Output: [4,5,6]       # 7 appears once and is the only value squeezed out
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, number of unique elements in nums]`
- the answer is guaranteed to be unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting the counts to a min-heap that never holds more than `k` entries, with complexity.

## Follow-up

- The problem statement asks for better than O(n log n). The size-k heap is O(n log k); can you reach O(n) with bucket sort, indexing an array of lists by count?
- If the values arrived as a stream and `k` were fixed, which part of this solution could keep running incrementally and which part could not?
- What if ties were possible and you had to return the *smallest* values among equally frequent ones? What changes in the tuple pushed onto the heap?
