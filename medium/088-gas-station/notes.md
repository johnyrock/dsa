# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `gas_station.py`, keep the tests, write it again.

## Key insight

Two facts make a single pass enough. First, if `sum(gas) >= sum(cost)` a valid start always exists (the station right after the lowest point of the running fuel curve), and if not, none does. Second, if you set out from station `s` and first run dry between `i` and `i + 1`, then every station in `s .. i` is also a bad start: you would arrive at each of them with fuel `>= 0`, so starting there with an empty tank cannot do better. That lets you skip straight to `start = i + 1` with `tank = 0`, and the last surviving candidate is the answer.

## Complexity

- Time: O(n), one pass for the sums and one for the sweep.
- Space: O(1), two integers.

## Mistakes to watch for

- Resetting to `start = i` instead of `i + 1`. Station `i` is the one we ran dry *leaving*, so it cannot be the start; on `[1,2,3,4,5] / [3,4,5,1,2]` this returns 2 instead of 3.
- Skipping the `sum(gas) < sum(cost)` check. The sweep then always returns some index, because it never wraps around to verify: `[2,3,4] / [3,4,3]` returns 2 instead of -1.
- Forgetting `tank = 0` on reset. The deficit carries into the next candidate, which then dies unfairly: on `[1,2,3,4,5] / [3,4,5,1,2]` the tank runs -2, -4, -6, -3, 0, so the reset fires at station 3 as well and the function returns 4 instead of 3.
- Returning the index after the loop *without* confirming the last leg. The greedy pass only checks `start .. n - 1`; the wrap from `n - 1` back to `start` is exactly what the total-sum check guarantees. Drop either half and the answer is wrong.

## Related

- [medium/086-jump-game](../086-jump-game) is the same "one running frontier decides everything" shape.
- [medium/076-maximum-product-subarray](../076-maximum-product-subarray) and Kadane-style scans reset a running value at a well-defined point exactly like `tank` here.
- [easy/005-best-time-to-buy-and-sell-stock](../../easy/005-best-time-to-buy-and-sell-stock) is the simplest single-pass running-minimum greedy.
- Review the [Greedy pattern](../../patterns/greedy.md) and its concept page.
