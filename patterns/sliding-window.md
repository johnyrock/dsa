# Sliding Window / One-Pass Tracking

## When to use

- The answer for position i depends on some summary of everything before i (the min, the max, a running sum).
- You are tempted to write a nested loop where the inner loop rescans the prefix.
- Contiguous subarray or substring problems with a size or sum condition.

## Template

```python
best = 0
running = initial          # e.g. the min so far
for x in items:
    best = max(best, f(x, running))
    running = update(running, x)
```

For a true sliding window with two edges, advance `right` every step and advance `left` only while the window is invalid.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/005 Best Time to Buy and Sell Stock](../easy/005-best-time-to-buy-and-sell-stock/) | Easy | track min price so far, profit = price - min |

## Common mistakes

- Updating the running value before using it, which lets an element pair with itself.
- Initialising `best` to something that can go negative when the answer should floor at 0.
