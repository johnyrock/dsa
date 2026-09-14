# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `multiply_strings.py`, keep the tests, write it again.

## Key insight

The product of digit `num1[i]` and digit `num2[j]` (indices counted from the left) always lands in the two result cells `i + j` and `i + j + 1` of an array sized `len(num1) + len(num2)`. So instead of building each partial product as a string and adding strings together, allocate the cells once, walk both numbers from the right, and drop every digit product straight into `result[i + j + 1]` with the carry into `result[i + j]`. The array is then read left to right, skipping leading zeros.

## Complexity

- Time: O(m · n), one multiplication per digit pair, plus O(m + n) to strip zeros and join.
- Space: O(m + n) for the result cells.

## Mistakes to watch for

- Forgetting the zero guard: `"0" × "12345"` fills six cells with 0 and the leading-zero strip must then stop at the last cell, which is why the loop condition is `start < len(result) - 1`. Without that `- 1` the join is `""` instead of `"0"`.
- Using `result[i + j]` for the ones digit and `result[i + j - 1]` for the carry. At `i = j = 0` that writes to index `-1`, which Python silently interprets as the last cell, so `"123" × "456"` comes out as `"560880"`: every digit is shifted one place left and the carry that should have become the leading 5 wraps around to the last cell.
- Only adding `total // 10` into the carry cell without first adding the existing `result[i + j + 1]` into `total`. The digit already in the ones cell is then overwritten instead of accumulated: `"99" × "99"` gives `"8111"` instead of `"9801"`.
- Looping `range(len(num1))` left to right. The cell rule `i + j + 1` still holds, but the carries then flow into cells that have already been finalised, so the digits never normalise: `"99" × "99"` leaves the cells `[8, 17, 10, 1]` and joins to `"817101"`.

## Related

- [easy/023-plus-one](../../easy/023-plus-one/) — the same right-to-left carry, with a single addition.
- [medium/098-powx-n](../../medium/098-powx-n/) — the other arithmetic-by-hand problem in this repo.
- [easy/022-happy-number](../../easy/022-happy-number/) — peeling digits off an integer with `% 10` and `// 10`.
- Pattern doc: [patterns/math.md](../../patterns/math.md)
