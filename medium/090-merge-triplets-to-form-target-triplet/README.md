# 090. Merge Triplets to Form Target Triplet

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #1899

## Problem

You are given a list of `triplets`, each `[a, b, c]`, and a `target` triplet `[x, y, z]`. You may pick any two triplets `i` and `j` any number of times and replace `triplets[j]` with the element-wise maximum `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `true` if some sequence of these operations can turn one of the triplets into exactly `target`, and `false` otherwise.

## Examples

```
Input:  triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true          # merge [2,5,3] and [1,7,5] -> [2,7,5]; [1,8,4] is never used because 8 > 7

Input:  triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false         # both triplets have a middle value above 2, so neither can be merged in

Input:  triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true          # [2,5,3] gives the 5 in position 1, [1,2,5] position 2, [5,2,3] position 0
```

## Constraints

- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= a_i, b_i, c_i, x, y, z <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying subsets of triplets to a single pass that skips any triplet exceeding the target and tracks which positions have been matched.

## Follow-up

- The same idea works for k-tuples instead of triplets. What is the time complexity as a function of `n` and `k`?
- What if the merge used element-wise `min` instead of `max`? Which triplets become unusable then?
- Could you also return *which* triplets to merge, not just whether it is possible?
