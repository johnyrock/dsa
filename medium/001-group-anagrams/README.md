# 001. Group Anagrams

**Difficulty:** Medium | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #49

## Problem

Given an array of strings `strs`, group the anagrams together and return the groups. Two strings are anagrams when one can be rearranged into the other, so they contain exactly the same letters with the same counts.

The groups may be returned in any order, and the strings inside a group may be in any order.

## Examples

```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Input:  strs = [""]
Output: [[""]]

Input:  strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters only

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from comparing every pair to a single pass that buckets each word under a canonical key, with complexity.

## Follow-up

- Sorting each word gives a key in O(k log k). Can you build a key in O(k) using the constraint that the letters are lowercase?
- What would you change if the strings could contain any Unicode character?
