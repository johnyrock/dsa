from word_search import Solution

solution = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
for word in ["ABCCED", "SEE", "ABCB"]:
    print(word, solution.exist(board, word))
