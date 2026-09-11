# 022. Random Pick with Weight

**Difficulty:** Medium | **Pattern:** [prefix-sum](../../patterns/prefix-sum.md) ([explained](../../concepts/prefix-sum.html)) | **Source:** LeetCode #528

## Problem

Given an array `w` of positive weights, implement `pickIndex()` so that the probability of picking index `i` is `w[i] / sum(w)`.

## Examples

```
Input:  w = [1, 3]
pickIndex() should return 0 with probability 1/4 and 1 with probability 3/4.
```

## Constraints

- `1 <= w.length <= 10^4`
- `1 <= w[i] <= 10^5`
- `pickIndex` is called up to `10^4` times

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of turning weights into ranges on a number line via prefix sums, then binary-searching a random point.

## Follow-up

- Why does building the prefix sums once in `__init__` matter, given `pickIndex` may be called thousands of times?
