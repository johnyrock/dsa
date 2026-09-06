# Dynamic Programming

## When to use

- The answer for n is built from answers for smaller inputs, and the naive recursion recomputes the same subproblems.
- "Number of ways", "minimum cost", "longest / shortest" over a sequence or grid.

## Method

1. Write the recurrence: `f(n)` in terms of `f(n-1)`, `f(n-2)`, ...
2. Identify the base cases.
3. Fill bottom-up from the base cases, or memoise the recursion.
4. If `f(n)` only needs the last k values, keep k variables instead of a table.
5. For "minimum over choices" problems (Coin Change), the recurrence is `1 + min(f(n - choice))` with an unreachable sentinel; for "best ending here" problems (Maximum Subarray), the answer is the max over all table entries, not the last one.

## Template

```python
if n <= 2:
    return n
a, b = 1, 2           # f(1), f(2)
for _ in range(3, n + 1):
    a, b = b, a + b
return b
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/010 Climbing Stairs](../easy/010-climbing-stairs/) | Easy | f(n) = f(n-1) + f(n-2), Fibonacci with two variables |
| [medium/007 Maximum Subarray](../medium/007-maximum-subarray/) | Medium | best ending here = max(x, prev + x), Kadane |
| [medium/008 Coin Change](../medium/008-coin-change/) | Medium | dp[a] = 1 + min(dp[a - c]), table over amounts |

## Common mistakes

- Wrong base cases, which shift every later answer.
- Off-by-one in the loop range when switching from a table to rolling variables.
- Memoising without a cache and calling it DP. Without the cache it is still exponential.
- Seeding a running best with 0 when every real answer can be negative (Maximum Subarray). Seed with the first element.
- Trusting greedy where the DP is required (Coin Change with `[1, 3, 4]`, amount 6).
