# 077. Word Break

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #139

## Problem

You are given a string `s` and a list of dictionary words `word_dict`. Decide whether `s` can be split into a sequence of one or more dictionary words, laid end to end with nothing left over.

The same dictionary word may be used any number of times. Return `True` if such a segmentation exists, `False` otherwise.

## Examples

```
Input:  s = "leetcode", word_dict = ["leet", "code"]
Output: True          # "leet" + "code"

Input:  s = "applepenapple", word_dict = ["apple", "pen"]
Output: True          # "apple" + "pen" + "apple", reusing "apple"

Input:  s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]
Output: False         # "cats"+"and" or "cat"+"sand" both strand "og"
```

## Constraints

- `1 <= s.length <= 300`
- `1 <= word_dict.length <= 1000`
- `1 <= word_dict[i].length <= 20`
- `s` and `word_dict[i]` consist of only lowercase English letters
- all strings of `word_dict` are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the backtracking that re-explores the same suffixes to the boolean table over prefixes, with complexity.

## Follow-up

- Return *all* the segmentations instead of a yes/no (LeetCode #140). How does the table change from booleans to lists, and why does the count blow up?
- The dictionary words are at most 20 characters long. How can the inner loop use that to drop the O(n²) cut-point scan to O(n × 20)?
- What if `s` is huge but the dictionary is tiny — would a trie over the dictionary let you avoid building every slice `s[j:i]`?
