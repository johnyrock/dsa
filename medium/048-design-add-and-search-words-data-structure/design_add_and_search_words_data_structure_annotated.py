class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        # One child per next character; a dict so only letters that actually occur take space.
        self.children: dict[str, "TrieNode"] = {}
        # True on the node where an added word ends. Needed so "ba" does not match after add_word("bad").
        self.is_word = False


class WordDictionary:
    def __init__(self) -> None:
        # The root is the empty prefix shared by every word.
        self.root = TrieNode()

    # Plain trie insert: walk the letters, creating missing nodes, and flag the last node.
    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            # Create the branch only when missing so words sharing a prefix share nodes.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    # Search with "." allowed to stand for any single letter. A "." can lead down several branches, so the walk is recursive instead of a single loop.
    def search(self, word: str) -> bool:
        # match(node, i): can word[i:] be matched starting from this node?
        def match(node, i):
            # Consumed the whole pattern: a match only if a word ends exactly here, not merely a prefix.
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == ".":
                # Wildcard: try every child. any() stops at the first branch that succeeds, and returns False for a node with no children.
                return any(match(child, i + 1) for child in node.children.values())
            # Literal letter: exactly one branch can continue, and if it is missing this path is dead.
            child = node.children.get(ch)
            return child is not None and match(child, i + 1)

        return match(self.root, 0)
