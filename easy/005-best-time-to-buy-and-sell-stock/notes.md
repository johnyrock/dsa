# Notes

## Attempts

- 2026-09-05: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete the solution file, keep the tests, and write it again before trusting any confidence score.

## Key insight

Do not search for a pair of days. Walk forward and ask, at each day, "if I sold today, what is the most I could make?" The answer is `price - min_price_so_far`, and the minimum so far is one variable you update as you go. One pass, no pair search.

## Complexity

- Time: O(n), a single pass with O(1) work per day.
- Space: O(1), two scalars regardless of input size.

### Understanding space

Space complexity counts the extra memory the algorithm allocates beyond the input itself. The input is given, not created, so it is not charged. This is called auxiliary space and is what interviewers usually mean.

The counting rule: look at every variable and container the function creates and ask, does its size depend on n, the length of the input?

- A single number, boolean, or fixed-size string takes the same memory whether n is 6 or 6 million. O(1).
- A list, set, or dict filled from the input can hold up to n items. O(n).
- A 2D grid of n by n. O(n²).
- Recursion also costs space. Every unfinished call sits on the call stack, so recursion n levels deep is O(n) even with no explicit list.

Applied to this solution:

| variable | size depends on n? | space |
|---|---|---|
| `min_price` | no, always one float | O(1) |
| `best` | no, always one int | O(1) |
| `price` | no, one value at a time, overwritten each iteration | O(1) |

Three small values regardless of input size, so O(1). Reusing a variable is not growth: `price` changes n times but only ever holds one value.

Contrast with a version that stores the running minimum for every day:

```python
def max_profit(prices):
    mins = []
    lowest = float("inf")
    for p in prices:
        lowest = min(lowest, p)
        mins.append(lowest)          # grows with n
    best = 0
    for i, p in enumerate(prices):
        best = max(best, p - mins[i])
    return best
```

Same answer, same O(n) time, but `mins` holds one entry per price, so it is O(n) space. The real solution keeps only the latest minimum instead of the whole history. Replacing "store all of them" with "store only what the next step needs" is the most common way to shrink space from O(n) to O(1).

### Quick checklist

1. Time: how many times does the innermost line run? One loop over n is O(n). A loop inside a loop is O(n²). Sorting is O(n log n).
2. Space: what did I create that is not the input, and can it grow with n? Only scalars means O(1). A list or map filled from the input means O(n). Recursion n deep means O(n).

Modifying the input in place is usually counted as O(1) extra space, since nothing new is allocated. Say so explicitly in an interview.

## Mistakes to watch for

- Start `best` at 0, not at negative infinity. A losing trade is never taken, so the answer is never negative.
- Update the minimum before considering a sale on the same day, and never let a buy day count as its own sell day.
- `[3, 2, 6, 5, 0, 3]` is the trap: the global minimum is 0 near the end, but the best trade (2 → 6, profit 4) finished long before it. Tracking the best profit separately from the minimum is what handles this.
- A single-element list must return 0, not crash.

## Related

- Best Time to Buy and Sell Stock II (LeetCode #122) allows unlimited transactions and collapses to summing every upward step.
- Maximum Subarray (LeetCode #53) is the same running-best trick applied to sums instead of differences.
