# 048. Design Add and Search Words Data Structure

**Difficulty:** Medium | **Pattern:** [trie](../../patterns/trie.md) ([explained](../../concepts/trie.html)) | **Source:** LeetCode #211

## Problem

Design a class `WordDictionary` with `add_word(word)`, which stores a word, and `search(word)`, which returns whether any stored word matches the given string. The string may contain the character `.`, which matches exactly one arbitrary letter.

The match must cover the whole word: `search("b.")` does not match a stored `"bad"`, and `search("b...")` does not either.

## Examples

```
Input:  add_word("bad"); add_word("dad"); add_word("mad"); search("pad"); search("bad"); search(".ad"); search("b..")
Output: null, null, null, false, true, true, true
        # "pad": no stored word starts with p
        # ".ad": the dot can be b, d, or m, and b-a-d is a stored word
        # "b..": b, then any letter, then any letter, ending exactly where "bad" ends

Input:  add_word("a"); add_word("ab"); search("."); search(".."); search("...")
Output: null, null, true, true, false
        # each dot consumes exactly one letter, so "..." needs a three-letter word and there is none
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `add_word` consists of lowercase English letters
- `word` in `search` consists of `.` or lowercase English letters
- there will be at most 2 dots in `word` for `search` queries
- at most `10^4` calls will be made to `add_word` and `search`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning every stored word against the pattern to a trie whose search branches at each dot, with the trie's contents shown after every operation.

## Follow-up

- The constraint allows at most 2 dots. How does the worst-case search cost grow if a pattern were all dots, and why does the trie still beat a list scan on `"b.."`?
- Add a `*` that matches zero or more letters (like a glob). Which base case changes, and what does the recursion need to try at a `*`?
- Group stored words by length in separate tries. When does that shortcut help a search, and when does it cost more memory than it saves?
