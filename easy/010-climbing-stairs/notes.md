# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `climbing_stairs.py`, keep the tests, write it again.

## Key insight

The number of ways to reach step `n` is the number of ways to reach step `n - 1` (then take a 1-step) plus the number of ways to reach step `n - 2` (then take a 2-step). Since each answer depends only on the previous two, the whole dp table collapses into two rolling variables. It is the Fibonacci sequence shifted by one: 1, 2, 3, 5, 8, 13, ...

## Building the recurrence from scratch

`f(n)` is a name for a question: "how many ways can I climb an `n`-step staircase with moves of 1 or 2?" The number in the parentheses is the staircase size; the value of `f` is the count of ways. `f(4)` is 5, not 4.

Count the small ones by hand:

| steps | ways | sequences |
|---|---|---|
| 1 | 1 | `1` |
| 2 | 2 | `1+1`, `2` |
| 3 | 3 | `1+1+1`, `1+2`, `2+1` |
| 4 | 5 | `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2` |

Listing gets miserable fast (`f(10)` has 89 sequences), so look at the **last move** of each sequence for 4 steps:

| sequence | last move | standing on, just before |
|---|---|---|
| 1, 1, 1, **1** | 1 | step 3 |
| 1, 1, **2** | 2 | step 2 |
| 1, 2, **1** | 1 | step 3 |
| 2, 1, **1** | 1 | step 3 |
| 2, **2** | 2 | step 2 |

Every sequence ends in a 1 or a 2; there is no third option. So the 5 sequences split into two piles:

- ended with a 1 → you were on step 3, and everything before that final move is a way to climb 3 steps. There are `f(3) = 3` of those.
- ended with a 2 → you were on step 2, and everything before is a way to climb 2 steps. There are `f(2) = 2` of those.

`f(4) = f(3) + f(2) = 3 + 2 = 5`. Nothing about that argument was specific to 4, so for any `n`:

```
f(n) = f(n-1) + f(n-2)
```

Read it as "ways to reach `n`" = "ways to reach one step below" + "ways to reach two steps below".

### Why `f(n-1)` is not `n-1`

`f(5) = f(4) + f(3) = 5 + 3 = 8`. Computing `(5-1) + (5-2) = 8` gives the same number only by coincidence (`4+3 = 5+3`). At `n = 6` it breaks: `(6-1) + (6-2) = 9`, but `f(6) = f(5) + f(4) = 8 + 5 = 13`. The recurrence adds two earlier *answers*, not two smaller *inputs*.

### Why you still need the base cases and a loop

The formula says how to get `f(n)` *if you already know* the two before it. It gives no starting point, so you hand it the first two answers counted by hand, `f(1) = 1` and `f(2) = 2`, and chain upward:

```
f(3) = f(2) + f(1) = 2 + 1 = 3
f(4) = f(3) + f(2) = 3 + 2 = 5
f(5) = f(4) + f(3) = 5 + 3 = 8
f(6) = f(5) + f(4) = 8 + 5 = 13
```

That chain is the loop in `climbing_stairs.py`: `two_back` and `one_back` are the previous two answers and `two_back + one_back` is the next one. Writing the recurrence literally as recursion (`return f(n-1) + f(n-2)`) is the same math, but it recomputes `f(3)` twice, `f(2)` three times, and so on, doubling the work with every step: O(2^n). The progression is recurrence → naive recursion (exponential) → memoized recursion (linear, needs a cache and n stack frames) → bottom-up loop (linear, two variables). The loop is what falls out once you notice the cache only ever needs its last two entries.

### Why not a closed-form formula

The answer is the (n+1)-th Fibonacci number, and Binet's formula `F(n) = (φⁿ − ψⁿ) / √5` computes it directly. It is not used because φ is irrational, so floating point rounding drifts and `round()` returns the wrong integer around `n ≈ 70`, while the loop's integer additions are exact. The loop is also already O(n) with two variables, and the recurrence is the part that generalizes (different step sizes, per-step costs, House Robber, Decode Ways); Binet only fits this exact recurrence with these exact base cases. If O(log n) is genuinely required, fast exponentiation of the matrix `[[1,1],[1,0]]` gets there with exact integers.

## Complexity

- Time: O(n), one pass from step 3 to step n.
- Space: O(1), only two integers are alive at any moment.

## Mistakes to watch for

- `n = 1` and `n = 2` need their own answers before the loop. Without the guard, `range(3, n + 1)` is empty and the seeded `one_back = 2` is returned for `n = 1`, which is wrong.
- Start the loop at 3, not 2. `range(2, n + 1)` does one extra iteration and returns the answer for `n + 1` (13 instead of 8 at `n = 5`).
- The tuple assignment `two_back, one_back = one_back, two_back + one_back` evaluates the right side first. Writing it as two separate statements clobbers `one_back` before it is used.
- Plain recursion without memoization is O(2^n) and times out well before `n = 45`.

## Related

- House Robber (medium) is the same recurrence shape with a max instead of a sum.
- Min Cost Climbing Stairs (easy, LeetCode #746) adds a per-step cost to the same table.
- Fibonacci Number (easy, LeetCode #509) is the identical loop with different base cases.
