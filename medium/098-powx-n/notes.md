# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `powx_n.py`, keep the tests, write it again.

## Key insight

Write `n` in binary. Each set bit `k` contributes a factor `x^(2^k)`, and those factors are produced by repeated squaring: `x, x², x⁴, x⁸, ...`. So keep a `base` that squares every iteration and a `result` that multiplies in `base` only when the current lowest bit of `n` is 1, then shift `n` right. That is one iteration per bit, about `log₂ n` iterations, instead of `n` multiplications. A negative `n` is handled up front by replacing `x` with `1 / x` and `n` with `-n`.

## Complexity

- Time: O(log n). One squaring per bit of `n`, at most 32 iterations for the constraint range.
- Space: O(1). Two floats and the shrinking integer `n`.

## Mistakes to watch for

- Squaring `base` before checking the bit. `base *= base` must come *after* `if n & 1: result *= base`; swapping them makes every contributing factor one power of two too big and returns `1048576` (2^20) for `x = 2, n = 10` instead of `1024`.
- Forgetting the negative exponent. `while n:` with `n = -2` loops forever in Python (`-2 >> 1` is `-1`, and `-1 >> 1` is still `-1`); `while n > 0:` instead terminates immediately and returns `1.0`, not `0.25`.
- Starting `result` at `x` instead of `1.0`. Then `n = 0` returns `x`, and every other answer is off by one factor of `x`.
- In fixed-width languages, `n = -2^31` overflows when negated. Python's ints are unbounded so the test at that value passes here, but a `long` or an extra `n % 2` step is needed elsewhere.

## Related

- [easy/025-number-of-1-bits](../../easy/025-number-of-1-bits/) — the same "consume `n` one bit at a time with `& 1` and `>>= 1`" loop, counting instead of multiplying.
- [easy/026-counting-bits](../../easy/026-counting-bits/) — binary structure of an integer, `i >> 1` drops the lowest bit.
- [easy/022-happy-number](../../easy/022-happy-number/) — another digit/bit-driven math loop.
- Pattern doc: [patterns/math.md](../../patterns/math.md)
