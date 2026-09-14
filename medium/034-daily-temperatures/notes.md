# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `daily_temperatures.py`, keep the tests, write it again.

## Key insight

Walk the days left to right and keep a stack of indices whose warmer day has not arrived yet; by construction their temperatures are decreasing from bottom to top. When today is warmer than the index on top, today *is* that day's answer: pop it, write `i - j`, and keep popping while today still beats the new top. Then push today. Each index is pushed once and popped at most once, so the whole thing is linear even though a single day can resolve many.

## Complexity

- Time: O(n); every index is pushed once and popped at most once, so the inner `while` does at most n pops over the whole run.
- Space: O(n) for the stack (all of it in the strictly-falling case) plus the answer array.

## Mistakes to watch for

- Using `if` instead of `while` for the pop. Day 5 (72) must resolve both day 4 (69) and day 3 (71); with `if` only day 4 is popped, and the output for the running example becomes `[1, 1, 0, 0, 1, 1, 0, 0]` instead of `[1, 1, 4, 2, 1, 1, 0, 0]`.
- Pushing temperatures instead of indices. The comparison still works but `i - j` cannot be computed; you need the day number to write the distance, so the stack must hold indices and compare `temperatures[stack[-1]]`.
- Writing `<=` instead of `<`. Equal temperatures are not warmer: `[70, 70, 70]` must give `[0, 0, 0]`, but `<=` pops on equality and gives `[1, 1, 0]`.
- Pushing before popping. Today would then compare against itself (`temperatures[i] < temperatures[i]` is false) and stop immediately, so nothing is ever resolved and every answer stays 0.

## Related

- [easy/004-valid-parentheses](../../easy/004-valid-parentheses) is the stack in its simplest form: push openers, pop on match.
- [medium/035-car-fleet](../035-car-fleet) is the same monotonic-stack idea applied to arrival times.
- [easy/005-best-time-to-buy-and-sell-stock](../../easy/005-best-time-to-buy-and-sell-stock) is another single pass that keeps a running "best so far" instead of a stack.
- Review the [Stack pattern](../../patterns/stack.md) and its concept page.
