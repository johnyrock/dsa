from implement_trie_prefix_tree import Trie

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))       # True
print(trie.search("app"))         # False: a prefix, not a stored word
print(trie.starts_with("app"))    # True
trie.insert("app")
print(trie.search("app"))         # True
