# 029. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #167

## Problem

You are given a 1-indexed array `numbers` that is already sorted in non-decreasing order, and an integer `target`. Find the two numbers in it that add up to `target`.

Return their positions as `[index1, index2]` with `1 <= index1 < index2 <= numbers.length`. There is exactly one valid pair, you may not use the same element twice, and the solution must use only constant extra space.

## Examples

```
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]          # 2 + 7 = 9, positions 1 and 2 (1-based)

Input:  numbers = [2,3,4], target = 6
Output: [1,3]          # 2 + 4 = 6; using 3 twice is not allowed

Input:  numbers = [-1,0], target = -1
Output: [1,2]          # -1 + 0 = -1
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- the tests are generated such that there is exactly one solution

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every pair to walking two pointers inward from both ends, with complexity.

## Follow-up

- The unsorted version (Two Sum, LeetCode #1) needs a hash map and O(n) extra space. What property of a sorted array lets the two-pointer walk skip the map entirely?
- If the array could contain *several* valid pairs, how would you enumerate all of them without reporting duplicates such as `[1,3]` and `[3,1]`?
- Extend the idea to 3Sum (medium/004): fix one element, then run this exact two-pointer scan on the rest. What does that cost?
