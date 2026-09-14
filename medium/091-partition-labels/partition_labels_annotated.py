class Solution:
    # Split s into as many parts as possible so that no letter appears in two different parts; return the part sizes.
    def partition_labels(self, s: str) -> list[int]:
        # Record the last index of every letter. Later writes overwrite earlier ones, so each letter ends up mapped to its final occurrence.
        last = {ch: i for i, ch in enumerate(s)}
        # The answer: one size per finished part.
        sizes = []
        # end is the furthest index the current part must reach to contain every letter seen in it so far; size counts the letters in the current part.
        end = size = 0
        # One left-to-right pass over the string.
        for i, ch in enumerate(s):
            # This letter belongs to the current part no matter what, so the part grows by one.
            size += 1
            # If this letter reappears later, the part must stretch at least that far. max keeps the furthest obligation seen so far.
            end = max(end, last[ch])
            # Reaching the furthest obligation means every letter in the part has had its last occurrence: the part can close here.
            if i == end:
                sizes.append(size)
                # The next part starts fresh at i + 1.
                size = 0
        return sizes
