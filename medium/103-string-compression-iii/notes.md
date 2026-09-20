# Notes

## Attempts

- 2026-09-20: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `string_compression_iii.py`, keep the tests, write it again.

## Key insight

The output is determined run by run, so two same-direction pointers do the whole job: `i` marks where the current run starts and `j` walks forward while `word[j] == word[i]`. The run's length is `j - i`, and adding `j - i < 9` to the loop condition makes a long run stop at 9 and start a fresh run from the same character, which is exactly what "remove at most 9 at a time" means. Each piece is `str(j - i) + word[i]`, collected in a list and joined once so the total cost stays O(n).

## Complexity

- Time: O(n). Every index is visited by `j` exactly once, and the final join is linear.
- Space: O(n) for the output pieces; O(1) beyond that.

## Mistakes to watch for

- Writing the character before the count (`word[i] + str(j - i)`), out of habit from String Compression I. `"aabbdd"` becomes `"a2b2d2"` instead of `"2a2b2d"`.
- Dropping the `j - i < 9` guard. `"aaaaaaaaaaaaaabb"` becomes `"14a2b"` instead of `"9a5a2b"`, and the answer is no longer decodable digit by digit.
- Using `<= 9` instead of `< 9`. That allows runs of 10, so 14 a's become `"10a4a"`.
- Forgetting `i = j` after appending, which leaves `i` at the start of the same run forever: an infinite loop on any non-empty input.
- Building the answer with `comp += ...` on a `str`. Correct, but every concatenation may copy the growing result, so a 200 000-character input can turn quadratic.

## Related

- Encode and Decode Strings (medium/026) is the same length-prefix idea with a delimiter, and its decoder is the mirror of this encoder.
- Longest Palindromic Substring (medium/012) also moves a pointer while a character condition holds, just outward from a centre instead of forward from a run start.
- Partition Labels (medium/091) scans a string and cuts it into pieces at positions decided during the scan.
- Pattern doc: [two-pointers](../../patterns/two-pointers.md).
