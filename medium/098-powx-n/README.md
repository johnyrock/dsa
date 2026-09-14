# 098. Pow(x, n)

**Difficulty:** Medium | **Pattern:** [math](../../patterns/math.md) ([explained](../../concepts/math.html)) | **Source:** LeetCode #50

## Problem

Implement `pow(x, n)`: given a float `x` and an integer `n` (which may be negative), return `x` raised to the power `n`.

The exponent can be as large as about 2 billion, so multiplying `x` by itself `n` times is not acceptable.

## Examples

```
Input:  x = 2.0, n = 10
Output: 1024.0        # 10 = 8 + 2 in binary (1010), so 2^10 = 2^8 * 2^2 = 256 * 4

Input:  x = 2.1, n = 3
Output: 9.261         # 2.1 * 2.1 * 2.1

Input:  x = 2.0, n = -2
Output: 0.25          # 2^-2 = (1/2)^2 = 1/4
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer
- either `x != 0` or `n > 0`
- `-10^4 <= x^n <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the O(n) multiply loop to binary exponentiation that reads one bit of `n` per step, with complexity.

## Follow-up

- Write the same algorithm recursively: `pow(x, n) = pow(x * x, n // 2)` times `x` if `n` is odd. How deep does the call stack go for `n = 2^31 - 1`?
- Compute `x^n mod m` for huge integer `n` without ever forming a huge number. Where does the `% m` go?
- In a language with fixed-width 32-bit `int`, `n = -2^31` cannot be negated. How would you handle that case?
