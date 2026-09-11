# 024. Word Container

**Difficulty:** Medium | **Pattern:** [trie](../../patterns/trie.md) ([explained](../../concepts/trie.html)) | **Source:** Custom (not a numbered LeetCode problem)

## Problem

A `WordList` manages a collection of words. A `Solver` operates on a `WordList` and finds every word in it that contains at least one *other* word from the same list as a substring.

Return the words that contain another word, in any order.

## Examples

```
Input:  words = ["apple", "app", "banana", "nana"]
Output: ["apple", "banana"]         # "apple" contains "app", "banana" contains "nana"

Input:  words = ["a", "b", "c"]
Output: []                          # no word is a substring of another

Input:  words = ["abc", "ab", "a"]
Output: ["abc", "ab"]               # containment can chain: "ab" is inside "abc", "a" is inside "ab"
```

## Constraints

- `0 <= words.length <= 10^4`
- `0 <= words[i].length <= 100`
- words consist of lowercase English letters
- a word matching itself (the same list entry, start-to-end) does not count as "containing another word"

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from pairwise substring checks to a shared trie walked from every starting index, with complexity.

## Follow-up

- The current solution is O(n · L²) in the worst case, where L is the max word length. Can you use Aho-Corasick to bring the total scan closer to O(total characters)?
- What changes if `WordList` needs to support words being added after `Solver` has already run once?
