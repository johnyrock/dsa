class Solution:
    def compressed_string(self, word: str) -> str:
        parts = []
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i] and j - i < 9:
                j += 1
            parts.append(str(j - i) + word[i])
            i = j
        return "".join(parts)
