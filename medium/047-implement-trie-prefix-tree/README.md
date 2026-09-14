# 047. Implement Trie (Prefix Tree)

**Difficulty:** Medium | **Pattern:** [trie](../../patterns/trie.md) ([explained](../../concepts/trie.html)) | **Source:** LeetCode #208

## Problem

Design a class `Trie` that stores strings and supports three operations: `insert(word)` adds a word, `search(word)` returns whether that exact word was inserted, and `starts_with(prefix)` returns whether any inserted word begins with `prefix`.

The point of the structure is that all three run in time proportional to the length of the argument, regardless of how many words are stored.

## Examples

```
Input:  Trie(); insert("apple"); search("apple"); search("app"); starts_with("app"); insert("app"); search("app")
Output: null, null, true, false, true, null, true
        # search("app") is false the first time: "app" is a prefix of "apple" but was never inserted
        # starts_with("app") is true for the same reason: the path a-p-p exists
        # after insert("app") the node at the end of that path is marked, so search("app") becomes true

Input:  Trie(); insert("car"); insert("card"); search("ca"); search("cards"); starts_with("card")
Output: null, null, false, false, true
        # "ca" reaches a node that is not a word end; "cards" walks off the end of "card"; "card" is a prefix of itself
```

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters
- at most `3 * 10^4` calls in total to `insert`, `search`, and `starts_with`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from a set plus prefix scans to a tree of characters with an end-of-word flag, with the trie's contents shown after every operation.

## Follow-up

- Add `delete(word)` that removes a word and prunes any nodes no other word needs. Which nodes are safe to remove, and in which order?
- Add `count_words_with_prefix(prefix)` in O(len(prefix)). What extra field per node makes that possible, and how do `insert` and `delete` maintain it?
- Replace the per-node dict with a fixed 26-slot list. When does that win on memory, and when does it lose?
