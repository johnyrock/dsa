# Dynamic Programming

## When to use

- The answer for n is built from answers for smaller inputs, and the naive recursion recomputes the same subproblems.
- "Number of ways", "minimum cost", "longest / shortest" over a sequence or grid.

## Method

1. Write the recurrence: `f(n)` in terms of `f(n-1)`, `f(n-2)`, ...
2. Identify the base cases.
3. Fill bottom-up from the base cases, or memoise the recursion.
4. If `f(n)` only needs the last k values, keep k variables instead of a table.

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

## Common mistakes

- Wrong base cases, which shift every later answer.
- Off-by-one in the loop range when switching from a table to rolling variables.
- Memoising without a cache and calling it DP. Without the cache it is still exponential.
