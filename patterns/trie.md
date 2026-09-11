# Trie

## When to use

- A fixed set of strings needs to be searched repeatedly for prefix or substring relationships — build the trie once, query it many times.
- Prefix-based problems: autocomplete, "does any word start with this prefix," longest common prefix.
- Substring-containment problems across a whole list: instead of comparing every pair of strings directly, insert them all into one trie and walk it.

## Templates

**Node and insertion:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def insert(root, word):
    node = root
    for ch in word:
        node = node.children.setdefault(ch, TrieNode())
    node.is_word = True
```

**Walk from every starting index (substring-anywhere-inside search):**

```python
def contains_another_word(root, word):
    n = len(word)
    for start in range(n):
        node = root
        for end in range(start, n):
            node = node.children.get(word[end])
            if node is None:
                break
            if node.is_word and not (start == 0 and end == n - 1):
                return True
    return False
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/024 Word Container](../medium/024-word-container/) | Medium | insert every word once, then walk from each starting index to test containment |

## Common mistakes

- Counting a word's own full-length match against itself as containment — exclude `start == 0 and end == n - 1` explicitly when the query word is also in the trie.
- Only trying `start = 0`. A contained word can begin anywhere inside the outer word.
- Breaking out of the whole search instead of just the current starting index when a branch dead-ends.
- Using a plain dict of `word -> True` instead of a trie when prefix/substring relationships across many words matter — that degrades back to O(n²) pairwise comparisons.
