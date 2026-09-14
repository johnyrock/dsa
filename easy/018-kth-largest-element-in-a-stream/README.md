# 018. Kth Largest Element in a Stream

**Difficulty:** Easy | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #703

## Problem

Design a class `KthLargest` that is constructed with an integer `k` and an initial list `nums`, and supports one operation: `add(val)` appends `val` to the stream and returns the k-th largest element seen so far.

"K-th largest" is in sorted order with duplicates counted, not the k-th distinct value.

## Examples

```
Input:  k = 3, nums = [4,5,8,2]
        add(3)  -> 4      # stream 2,3,4,5,8; third largest is 4
        add(5)  -> 5      # stream 2,3,4,5,5,8; third largest is 5 (the duplicate counts)
        add(10) -> 5      # stream 2,3,4,5,5,8,10; 10 pushes 8 to second, 5 stays third
        add(9)  -> 8      # 10, 9, 8
        add(4)  -> 8      # a 4 never displaces anything in the top three

Input:  k = 1, nums = []
        add(-3) -> -3     # the stream is allowed to start empty
        add(-2) -> -2
```

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i], val <= 10^4`
- at most `10^4` calls to `add`
- the stream is guaranteed to hold at least `k` elements whenever `add` is called

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- What changes if `k` is large relative to the stream, say `k` is close to the total count? Is the heap still the right structure, or does keeping the *smallest* `n - k + 1` win?
- The obvious alternative is a sorted list with `bisect.insort`. Its query is O(1); why is `add` still worse than the heap?
- How would you support `remove(val)` as well, so the stream can shrink?
