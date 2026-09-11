class TrieNode:
    # __slots__ keeps each node to two fixed attributes instead of a per-instance dict.
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        # Children map a single character to the next node on that branch.
        self.children: dict[str, "TrieNode"] = {}
        # True exactly at the node where some inserted word ends.
        self.is_word = False


class WordList:
    # Holds the original words plus a trie over all of them, so any substring
    # of any word can be checked against the whole list in one walk.
    def __init__(self, words: list[str]) -> None:
        self.words = list(words)
        self.root = TrieNode()
        for word in self.words:
            self._insert(word)

    def _insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            # setdefault creates the branch on first visit and reuses it on repeats,
            # so words sharing a prefix share the same nodes.
            node = node.children.setdefault(ch, TrieNode())
        # Mark the node reached after the last character as a completed word.
        node.is_word = True

    def has_other_word_inside(self, word: str) -> bool:
        n = len(word)
        # Anchor a walk at every starting index, since the contained word could
        # begin anywhere inside `word`.
        for start in range(n):
            node = self.root
            for end in range(start, n):
                node = node.children.get(word[end])
                # No word in the list has this substring as a prefix; this start
                # index cannot produce a match, so stop extending it.
                if node is None:
                    break
                # A word ends here. Exclude the one case where it is `word`
                # matching itself in full (start at 0, end at the last index) —
                # that is not "another" word containing it.
                if node.is_word and not (start == 0 and end == n - 1):
                    return True
        return False


class Solver:
    def __init__(self, word_list: WordList) -> None:
        self.word_list = word_list

    def find_words_containing_other_words(self) -> list[str]:
        # Check every word against the shared trie; the trie already encodes
        # every word in the list, so no per-pair comparison is needed.
        return [w for w in self.word_list.words if self.word_list.has_other_word_inside(w)]
