# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild it including the overflow test.

## Key insight

Strip the sign, then peel digits off the low end of `x` with `digit = x % 10` and `x //= 10`, appending each to `result` with `result = result * 10 + digit`. Before each append, check whether it would push `result` past `2^31 - 1`: overflow happens if `result > 214748364`, or if `result == 214748364` and `digit > 7`. Working on the magnitude means the same threshold serves both signs, because the only value that would need the negative limit's `8` (a reversal equal to `2147483648`) cannot come from a valid 32-bit input. Restore the sign at the end.

## Complexity

- Time: O(log₁₀ |x|), one iteration per digit, at most 10 for a 32-bit integer.
- Space: O(1). Three integers.

## Mistakes to watch for

- Skipping `abs(x)` and running `%`/`//` on a negative number. In Python `-123 % 10` is `7` and `-123 // 10` is `-13`; the loop reaches `x = -1`, where `-1 // 10` is still `-1`, and `while x:` never terminates. The running example `-123` hangs instead of returning `-321`.
- Testing `result >= INT_MAX // 10` instead of `>`. That rejects any reversal whose first nine digits are `214748364` even when the tenth digit fits: `1463847412` reverses to `2147483641`, which is valid, but the `>=` version returns `0`.
- Checking overflow after the append (`if result > INT_MAX: return 0`). It works in Python because integers do not overflow, but the problem forbids relying on that; in a 32-bit `int` the product `result * 10` has already wrapped by the time it is compared.
- Using `str(x)[::-1]` and forgetting the range check. `int(str(1534236469)[::-1])` is `9646324351`, and returning it instead of `0` fails the overflow cases.

## Related

- [easy/023-plus-one](../../easy/023-plus-one) walks decimal digits from the low end with a carry.
- [easy/027-reverse-bits](../../easy/027-reverse-bits) is the base-2 version: peel with `& 1` and `>> 1`, rebuild with `<< 1 | bit`.
- [medium/098-powx-n](../098-powx-n) is another loop that consumes an integer one digit (bit) at a time.
- Review the [Math pattern](../../patterns/math.md) and its concept page.
