# Hash Map

## When to use

- You need to answer "have I seen X before?" in O(1) while scanning once.
- You need to count occurrences or group items by a computed key.
- If you only need membership and no value, use a [hash set](hash-set.md) instead.
- A brute-force nested loop is comparing every element against every other; a map often collapses the inner loop.

## Template

```python
seen = {}
for i, x in enumerate(items):
    key = f(x)               # what would make a match with x?
    if key in seen:
        ...                  # found a match, use seen[key]
    seen[g(x)] = i           # record x for later elements
```

Check before insert when an element must not match itself.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/001 Two Sum](../easy/001-two-sum/) | Easy | value -> index, look up the complement |
| [easy/002 Valid Anagram](../easy/002-valid-anagram/) | Easy | char -> count, compare the two tallies |
| [medium/001 Group Anagrams](../medium/001-group-anagrams/) | Medium | letter-count tuple -> bucket of words |
| [medium/026 Encode and Decode Strings](../medium/026-encode-and-decode-strings/) | Medium | A separator character cannot work on its own, because any character you pick may… |
| [medium/042 Copy List with Random Pointer](../medium/042-copy-list-with-random-pointer/) | Medium | A `random` pointer can target a node that has not been copied yet (it may point… |
| [medium/100 Detect Squares](../medium/100-detect-squares/) | Medium | An axis-aligned square is fixed by one diagonal: once the query point `(px, py)` and a… |

## Common mistakes

- Inserting before checking, which lets an element pair with itself.
- Using a list for membership tests, which is O(n) per lookup and turns O(n) back into O(n²).
