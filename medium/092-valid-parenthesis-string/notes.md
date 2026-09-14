# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `valid_parenthesis_string.py`, keep the tests, write it again.

## Key insight

Walk the string tracking the *range* of possible open-bracket counts instead of one value: `lo` assumes every star so far closed and `hi` assumes every star opened. `'('` raises both, `')'` lowers both, `'*'` widens the range by one on each side. Every integer between `lo` and `hi` is achievable (changing one star's choice moves the count by one), so the string is valid exactly when 0 stays reachable: `hi` never drops below 0 during the walk, `lo` is clamped at 0 because a negative count is not a real state, and `lo == 0` at the end.

## Complexity

- Time: O(n), one pass with constant work per character.
- Space: O(1), two integers.

## Mistakes to watch for

- Forgetting `lo = max(lo, 0)`. On `"(*))"` the bounds go `(1,1)`, `(0,2)`, `(-1,1)`, `(-2,0)`, and the final `lo == 0` test fails: returns `false` for a valid string. The negative readings correspond to star choices that already produced an unmatched `')'`; they must be discarded, not carried.
- Dropping the `if hi < 0: return False` early exit. On `")**"`, `hi` goes `-1, 0, 1` and `lo` is clamped to 0 throughout, so the function returns `true`, but nothing after a leading `')'` can ever match it.
- Returning `hi == 0` instead of `lo == 0`. `hi` counts the reading where every star opened, which is the *most* unbalanced reading; on `"(*)"` it ends at 1 and the code returns `false`. The question is whether 0 is *reachable*, i.e. whether the lowest bound is 0.
- Treating `'*'` as only `'('` or only `')'`. A left-to-right pass with stars as `'('` accepts `"(*"`, which is invalid; the two-pass variant needs the second, mirrored pass to catch it.

## Related

- [medium/033-generate-parentheses](../../medium/033-generate-parentheses/) builds valid strings from the same "open count never negative, ends at zero" rule.
- [medium/035-car-fleet](../../medium/035-car-fleet/) is another single greedy sweep carrying one running value.
- Pattern doc: [greedy](../../patterns/greedy.md).
