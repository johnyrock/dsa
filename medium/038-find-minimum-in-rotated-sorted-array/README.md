# 038. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #153

## Problem

An array of distinct integers was sorted in ascending order and then rotated some number of times between 1 and `n`, so `[0,1,2,4,5,6,7]` might have become `[4,5,6,7,0,1,2]`. Given the rotated array `nums`, return its minimum element.

The solution must run in O(log n) time.

## Examples

```
Input:  nums = [4,5,6,7,0,1,2]
Output: 0             # the sorted array [0,1,2,4,5,6,7] rotated 4 times; 0 is where the drop happens

Input:  nums = [3,4,5,1,2]
Output: 1             # [1,2,3,4,5] rotated 3 times

Input:  nums = [11,13,15,17]
Output: 11            # rotated 4 times, which is a full turn, so it is still sorted and the first element is the minimum
```

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- all values of `nums` are unique
- `nums` is sorted and rotated between `1` and `n` times

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from a linear scan to a binary search that compares the midpoint against the right end, with complexity.

## Follow-up

- What breaks if the values are not distinct (LeetCode #154, Find Minimum in Rotated Sorted Array II)? Which comparison becomes ambiguous, and what does the fix cost in the worst case?
- Instead of the minimum value, return the number of times the array was rotated. Which single line changes?
- Search in Rotated Sorted Array (LeetCode #33) asks for a target instead of the minimum. Can you solve it by first finding the rotation index with this function and then doing an ordinary binary search on the correct half?
