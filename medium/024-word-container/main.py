from word_container import Solver, WordList

words = ["apple", "app", "banana", "nana"]
solver = Solver(WordList(words))
print(solver.find_words_containing_other_words())
