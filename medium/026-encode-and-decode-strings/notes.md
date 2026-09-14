# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `encode_and_decode_strings.py`, and write it again.

## Key insight

A separator character cannot work on its own, because any character you pick may appear inside a string. Instead, write each string as `<length>#<chars>`: the number says exactly how many characters follow, so the decoder slices that many characters blindly and never has to look for a separator inside the payload. The `#` only terminates the digits, and since the decoder jumps `i` to the end of each payload, a `#` inside a payload is never searched for. Empty strings encode as `0#`, and an empty list as `""`.

## Complexity

- Time: O(N) for both directions, where N is the total number of characters across all strings; each character is written once and read once.
- Space: O(N) for the encoded string (plus a few bytes of header per element) and O(N) for the decoded list.

## Mistakes to watch for

- Slicing the payload from `j` instead of `j + 1`: `s[j:j + length]` includes the `#` and drops the last character, so `"4#neet4#code4#love3#you"` decodes to `["#nee", "#cod", "#lov", "#yo"]`.
- Advancing with `i = j + length` (forgetting the `+ 1` for the `#`). On the running example the second header is read starting at `t`, and `int("t4")` raises `ValueError`.
- Searching for `#` from the start of the string (`s.index("#")` with no start position) instead of from `i`. It keeps finding the first `#` at index 1, so every chunk is decoded as the first one, and the loop never terminates correctly.
- Joining with a delimiter and calling `split`. `"#".join(["neet", "co#de"]).split("#")` gives `["neet", "co", "de"]`, three strings instead of two, and `",".join([]).split(",")` gives `[""]` instead of `[]`.

## Related

- [easy/004-valid-parentheses](../../easy/004-valid-parentheses) is another problem where the shape of the input must be parsed rather than searched.
- [medium/023-serialize-and-deserialize-binary-tree](../../medium/023-serialize-and-deserialize-binary-tree) is the same encode/decode contract applied to a tree, with the same "the format must be unambiguous" requirement.
- [easy/002-valid-anagram](../../easy/002-valid-anagram) is the simplest string-processing problem in the repo, if you want a warm-up first.
- Review the [Hash Map pattern](../../patterns/hash-map.md) and its concept page.
