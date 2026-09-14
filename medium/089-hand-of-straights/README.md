# 089. Hand of Straights

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #846

## Problem

Alice holds a hand of cards, given as an integer array `hand`, and wants to rearrange every card into groups of exactly `groupSize` cards where each group is a run of consecutive values (like `[2,3,4]`).

Return `true` if the whole hand can be split into such groups, and `false` otherwise.

## Examples

```
Input:  hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true          # [1,2,3], [2,3,4], [6,7,8]

Input:  hand = [1,2,3,4,5], groupSize = 4
Output: false         # 5 cards cannot be split into groups of 4

Input:  hand = [1,1,2,3,3,4], groupSize = 3
Output: false         # both 1s need a 2 to follow them, but there is only one 2
```

## Constraints

- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from repeatedly pulling cards out of a sorted list to a count map swept from the smallest value upward, with complexity.

## Follow-up

- Values go up to 10^9, so the sweep over `sorted(count)` matters. What goes wrong if you sweep `range(min, max + 1)` instead?
- The same problem with a queue of "open groups" avoids the inner `range` loop. Can you get O(n log n) without the nested loop?
- Suppose groups may be consecutive *or* all-equal (like a full house). Is there still a greedy, or does it need backtracking?
