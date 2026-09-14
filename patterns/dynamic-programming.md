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
| [easy/020 Min Cost Climbing Stairs](../easy/020-min-cost-climbing-stairs/) | Easy | Keep the cheapest costs for the prior two positions. |
| [medium/072 House Robber](../medium/072-house-robber/) | Medium | For each house the decision is binary: rob it and add its money to the best total from… |
| [medium/073 House Robber II](../medium/073-house-robber-ii/) | Medium | On a circle the only new constraint is that house 0 and house n-1 cannot both be robbed |
| [medium/074 Palindromic Substrings](../medium/074-palindromic-substrings/) | Medium | Every palindrome has a centre: a character for odd length, the gap between two… |
| [medium/075 Decode Ways](../medium/075-decode-ways/) | Medium | Look at how a decoding of the prefix `s[:i+1]` ends: either its last code is the… |
| [medium/076 Maximum Product Subarray](../medium/076-maximum-product-subarray/) | Medium | Kadane's idea, "best subarray ending here is either this element alone or this element… |
| [medium/077 Word Break](../medium/077-word-break/) | Medium | Ask about prefixes, not the whole string: `dp[i]` is "can `s[:i]` be segmented?" |
| [medium/078 Longest Increasing Subsequence](../medium/078-longest-increasing-subsequence/) | Medium | Anchor the subproblem on where the subsequence *ends*: `dp[i]` is the length of the… |
| [medium/079 Partition Equal Subset Sum](../medium/079-partition-equal-subset-sum/) | Medium | Two equal halves each sum to `total / 2`, so the problem is really "is there a subset… |
| [medium/080 Unique Paths](../medium/080-unique-paths/) | Medium | The robot enters any cell from exactly one of two neighbours: the cell above (its last… |
| [medium/081 Longest Common Subsequence](../medium/081-longest-common-subsequence/) | Medium | `dp[i][j]` is the LCS length of the first `i` characters of `text1` and the first `j`… |
| [medium/082 Best Time to Buy and Sell Stock with Cooldown](../medium/082-best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | At the end of any day you are in one of three states: `hold` (own a share), `sold`… |
| [medium/083 Coin Change II](../medium/083-coin-change-ii/) | Medium | `dp[a]` is the number of combinations that make amount `a` using only the coins… |
| [medium/084 Target Sum](../medium/084-target-sum/) | Medium | Split the numbers into the plus group `P` and the minus group `N` |
| [medium/085 Interleaving String](../medium/085-interleaving-string/) | Medium | `dp[i][j]` asks whether the first `i` characters of `s1` and the first `j` of `s2` can… |
## Common mistakes

- Wrong base cases, which shift every later answer.
- Off-by-one in the loop range when switching from a table to rolling variables.
- Memoising without a cache and calling it DP. Without the cache it is still exponential.
- Seeding a running best with 0 when every real answer can be negative (Maximum Subarray). Seed with the first element.
- Trusting greedy where the DP is required (Coin Change with `[1, 3, 4]`, amount 6).
