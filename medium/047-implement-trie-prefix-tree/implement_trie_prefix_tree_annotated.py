class TrieNode:
    # __slots__ keeps each node small; a trie over 10^4 words can hold hundreds of thousands of nodes.
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        # One child per next character. A dict (not a 26-slot list) costs nothing for letters that never appear.
        self.children: dict[str, "TrieNode"] = {}
        # True only on the node where some inserted word ends. Every node is a prefix of something; only marked nodes are words.
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        # The root is the empty prefix. It is never a word and holds the first letters of every inserted word.
        self.root = TrieNode()

    # Add a word: walk down one character at a time, creating the nodes that do not exist yet, then mark the last one.
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            # Create the branch only when missing, so shared prefixes ("app" inside "apple") reuse the same nodes.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # Mark the end of the word. Without this line "app" would be a prefix of "apple" but not a stored word.
        node.is_word = True

    # A word is present when the walk reaches a node AND that node is marked as a word end.
    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    # A prefix is present when the walk simply reaches a node; whether it is marked does not matter.
    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    # Shared helper: follow the characters of s from the root; return the node reached, or None if a character has no branch.
    def _walk(self, s: str) -> TrieNode | None:
        node = self.root
        for ch in s:
            # dict.get returns None for a missing letter, which is the "no such path" signal.
            node = node.children.get(ch)
            if node is None:
                return None
        return node
