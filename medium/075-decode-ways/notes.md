# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `decode_ways.py`, keep the tests, write it again.

## Key insight

Look at how a decoding of the prefix `s[:i+1]` ends: either its last code is the single digit `s[i]` (legal if it is not `"0"`), and the rest is a decoding of `s[:i]`, or its last code is the pair `s[i-1]s[i]` (legal if it is 10..26), and the rest is a decoding of `s[:i-1]`. So `dp[i+1] = (s[i] != "0") * dp[i] + (10 <= pair <= 26) * dp[i-1]`, which is Climbing Stairs with each step conditionally switched off. Only the last two counts are ever read, so two rolling variables replace the table. `dp[0] = 1` is the empty prefix, and a leading `"0"` is rejected before the loop because no code starts with it.

## Complexity

- Time: O(n), one pass over the digits with constant work each.
- Space: O(1), two integers.

## Mistakes to watch for

- Seeding `two_back, one_back = 0, 1` instead of `1, 1`, because "there are zero ways to decode nothing" feels right. It drops every two-digit code that reaches back to the start: `"226"` returns 2 instead of 3 and `"12"` returns 1 instead of 2. The empty prefix has exactly one decoding.
- Checking only `int(pair) <= 26` with no lower bound. `"06"` then counts as a code: `"106"` returns 2 instead of 1.
- Treating a lone `"0"` as a code by writing `ways += one_back` unconditionally. `"10"` returns 2 instead of 1, and `"100"` returns 2 instead of 0.
- Comparing the pair as a string (`"10" <= pair <= "26"`). It happens to work for two-character strings, but it is fragile and reads as a bug; convert with `int`.

## Related

- [Climbing Stairs](../../easy/010-climbing-stairs) (easy/010) is the same recurrence with both branches always allowed.
- [House Robber II](../073-house-robber-ii) (medium/073) keeps two rolling values with a max instead of a sum.
- [Word Break](../077-word-break) (medium/077) is the general form: a prefix is decodable if some suffix of it is a word and the rest is decodable.
- Pattern doc: [dynamic-programming](../../patterns/dynamic-programming.md).
