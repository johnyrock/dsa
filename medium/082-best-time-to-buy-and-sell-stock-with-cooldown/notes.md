# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the state machine.

## Key insight

At the end of any day you are in one of three states: `hold` (own a share), `sold` (sold today, so tomorrow is a forced rest), or `rest` (own nothing and are free to buy). Track the best cash balance for each state and roll all three forward one day at a time: `hold = max(hold, rest - price)` (keep, or buy from rest only), `sold = hold + price` (the only way to be "just sold"), `rest = max(rest, sold)` (keep resting, or arrive after yesterday's sale). The cooldown lives in one place: buying reads from `rest`, never from `sold`. The answer is `max(sold, rest)`, because ending while holding is never best.

## Complexity

- Time: O(n), one pass with three constant-time updates per day.
- Space: O(1), three integers.

## Mistakes to watch for

- Updating the three variables one statement at a time instead of in one tuple assignment. `sold = hold + price` then reads the *new* `hold`, which lets you buy and sell on the same day; on `[1,2,3,0,2]` this returns 4 instead of 3 (it also breaks `rest`).
- Letting `hold` read from `sold`: `hold = max(hold, max(rest, sold) - price)` removes the cooldown and gives 4 on `[1,2,3,0,2]` (buy 1, sell 3, buy 0, sell 2).
- Starting `hold` at 0 instead of `-inf`. That pretends you begin the first day already holding a free share, so `[2,1]` returns 2 instead of 0.
- Returning `sold` alone. If the best plan ends with a rest day (or no trade at all, as in `[5,4,3,2,1]`), `sold` can be negative or stale; the answer is `max(sold, rest)`.

## Related

- [easy/010-climbing-stairs](../../easy/010-climbing-stairs) is the simplest rolling-variable DP; this problem is the same shape with three variables and a max instead of a sum.
- [medium/072-house-robber](../072-house-robber) also forbids using two adjacent days, with a two-state rolling recurrence.
- [easy/005-best-time-to-buy-and-sell-stock](../../easy/005-best-time-to-buy-and-sell-stock) is the single-transaction version, solvable with a running minimum instead of states.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
