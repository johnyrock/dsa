# Math

## When to use

- The operation is arithmetic but the naive loop is too slow (`x ** n` with `n` up to 2³¹) or the numbers are too big for a machine word (multiply two 200-digit strings).
- The problem forbids the obvious library shortcut (`int()`, `str()`, `pow`) and wants you to work digit by digit.
- Overflow limits are part of the spec: a 32-bit result must be detected before it happens, not after.

## Templates

**Binary exponentiation (halve the exponent, square the base):**

```python
def power(x, n):
    if n < 0:
        x, n = 1 / x, -n            # x^-n == (1/x)^n
    result = 1.0
    while n:
        if n & 1:                   # this bit of n is set: multiply it in
            result *= x
        x *= x                      # x, x^2, x^4, x^8, ...
        n >>= 1
    return result
```

**Schoolbook multiplication on digit arrays:**

```python
def multiply(a, b):
    if a == "0" or b == "0":
        return "0"
    digits = [0] * (len(a) + len(b))        # product has at most len(a)+len(b) digits
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            total = int(a[i]) * int(b[j]) + digits[i + j + 1]
            digits[i + j + 1] = total % 10  # ones digit stays
            digits[i + j] += total // 10    # carry goes one slot left
    k = 0
    while digits[k] == 0:                   # strip leading zeroes
        k += 1
    return "".join(map(str, digits[k:]))
```

**Digit-by-digit reversal with an overflow check before each step:**

```python
def reverse(x):
    INT_MAX = 2 ** 31 - 1
    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    while x:
        digit = x % 10
        x //= 10
        # result * 10 + digit must stay <= INT_MAX (for the negative side, |INT_MIN| = INT_MAX + 1,
        # but a reversed number ending in ...8 cannot start with 2^31 - 1's digits, so one bound suffices)
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit
    return sign * result
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/098 Pow(x, n)](../medium/098-powx-n/) | Medium | square the base and halve the exponent, O(log n) multiplications |
| [medium/099 Multiply Strings](../medium/099-multiply-strings/) | Medium | digit `i` times digit `j` lands in slot `i + j + 1`, carry into `i + j` |
| [medium/102 Reverse Integer](../medium/102-reverse-integer/) | Medium | peel digits with `% 10`, check the bound before multiplying by 10 |

## Common mistakes

- Handling a negative exponent by recursing on `-n` without also inverting the base, or forgetting that `-n` can overflow in fixed-width languages (Python is fine).
- Recomputing `power(x, n // 2)` twice in the recursive version, which is O(n) again instead of O(log n).
- Building the product string with `int(a) * int(b)`; Python allows it, but the interviewer wants the digit loop.
- Forgetting that `digits[i + j]` can already hold a carry from a previous pass, so `+=` is required, not `=`.
- Returning `"000"` instead of `"0"` when leading zeroes are not stripped, or stripping into an empty string.
- Using Python's `%` on negative numbers: `-123 % 10 == 7`. Work on `abs(x)` and reapply the sign at the end.
- Checking for overflow after the multiplication; in a real 32-bit type the damage is already done. Compare against `(INT_MAX - digit) // 10` first.
