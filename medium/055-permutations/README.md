# 055. Permutations

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #46

## Problem

Given an array `nums` of distinct integers, return every possible ordering (permutation) of its elements. Each permutation uses every element exactly once.

The output may be in any order. Two permutations are different if the elements appear in a different order, so `[1, 2, 3]` and `[2, 1, 3]` are both answers.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]   # 3! = 6 orderings

Input:  nums = [0, 1]
Output: [[0,1], [1,0]]                                             # both orders count

Input:  nums = [1]
Output: [[1]]                                                      # one element, one ordering
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- all the integers of `nums` are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from generating every sequence and filtering to a recursion that fills one slot at a time from the unused elements and undoes both halves of each choice, with the recursion tree drawn alongside.

## Follow-up

- `nums` may now contain duplicates and the output must have no repeated permutations (LeetCode #47, Permutations II). What sort and what extra `continue` condition handle it, and why does the condition need the `used` array?
- Generate the permutations without a `used` array by swapping `nums[i]` into position `depth` and recursing on `depth + 1`. What does the undo look like, and what is the output order?
- Only permutations of length `k` are wanted (partial permutations). Which line changes, and how many leaves does the tree have?
