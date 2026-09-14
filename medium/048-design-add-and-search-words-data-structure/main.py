from design_add_and_search_words_data_structure import WordDictionary

wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
print(wd.search("pad"))   # False: no word starts with p
print(wd.search("bad"))   # True
print(wd.search(".ad"))   # True: the dot matches b, d, or m
print(wd.search("b.."))   # True: b, then any two letters, and "bad" ends there
