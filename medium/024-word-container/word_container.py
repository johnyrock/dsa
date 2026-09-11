class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class WordList:
    def __init__(self, words: list[str]) -> None:
        self.words = list(words)
        self.root = TrieNode()
        for word in self.words:
            self._insert(word)

    def _insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def has_other_word_inside(self, word: str) -> bool:
        n = len(word)
        for start in range(n):
            node = self.root
            for end in range(start, n):
                node = node.children.get(word[end])
                if node is None:
                    break
                if node.is_word and not (start == 0 and end == n - 1):
                    return True
        return False


class Solver:
    def __init__(self, word_list: WordList) -> None:
        self.word_list = word_list

    def find_words_containing_other_words(self) -> list[str]:
        return [w for w in self.word_list.words if self.word_list.has_other_word_inside(w)]
