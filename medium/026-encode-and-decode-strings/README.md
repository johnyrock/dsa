# 026. Encode and Decode Strings

**Difficulty:** Medium | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #271

## Problem

Design an algorithm to `encode` a list of strings into a single string, and a matching `decode` that turns that single string back into the original list. The strings may contain any characters, including whatever you might want to use as a separator, and the list may contain empty strings.

`decode(encode(strs))` must equal `strs` exactly, element for element.

## Examples

```
Input:  strs = ["neet","code","love","you"]
Output: ["neet","code","love","you"]   # encode gives "4#neet4#code4#love3#you"; each chunk is <length>#<chars>

Input:  strs = ["we","say",":","yes"]
Output: ["we","say",":","yes"]         # encode gives "2#we3#say1#:3#yes"; the ':' is just payload

Input:  strs = ["", "#"]
Output: ["", "#"]                      # encode gives "0#1##"; a '#' inside a string is skipped over by its length, never searched for
```

## Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters
- do not rely on any global or class-level state; `encode` and `decode` may run in different processes

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from a naive delimiter join to length-prefixed chunks, with a decode trace and complexity.

## Follow-up

- What if the length header itself could be arbitrarily large? Would a fixed-width 4-byte header be simpler than a variable-width one ending in `#`?
- Could you encode the list with an escape character instead of length prefixes (for example, doubling every `#` inside a payload and using a single `#` as the separator)? What does decode look like then, and what is its cost?
- If the strings were streamed one at a time on the decode side, which of the two schemes above can emit a string before seeing the whole input?
