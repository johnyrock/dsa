# 037. Koko Eating Bananas

**Difficulty:** Medium | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #875

## Problem

Koko has `piles` of bananas, where `piles[i]` is the number of bananas in the i-th pile, and the guards come back in `h` hours. She picks an eating speed `k` (bananas per hour). Each hour she chooses one pile and eats `k` bananas from it; if the pile has fewer than `k` bananas left, she finishes that pile and eats nothing else that hour.

Return the minimum integer speed `k` that lets her finish every pile within `h` hours.

## Examples

```
Input:  piles = [3,6,7,11], h = 8
Output: 4             # at k = 4 the piles take 1 + 2 + 2 + 3 = 8 hours; at k = 3 they take 1 + 2 + 3 + 4 = 10

Input:  piles = [30,11,23,4,20], h = 5
Output: 30            # five piles in five hours means one pile per hour, so k must cover the biggest pile

Input:  piles = [30,11,23,4,20], h = 6
Output: 23            # one spare hour: the 30 pile can be split into 23 + 7, everything else fits in one hour
```

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from testing every speed to binary searching the answer space with a feasibility check, with complexity.

## Follow-up

- What if Koko could carry leftover capacity from one pile into the next hour? Which single line of the feasibility check changes, and does the answer for the first example change?
- `h` can be as large as 10^9 and `piles.length` as small as 1. Can you tighten the lower bound of the search range using `sum(piles) / h` so the search starts closer to the answer?
- The same "binary search on the answer, check feasibility" shape solves Capacity To Ship Packages Within D Days (LeetCode #1011). What is the feasibility check there, and why is it a linear scan instead of a sum of ceilings?
