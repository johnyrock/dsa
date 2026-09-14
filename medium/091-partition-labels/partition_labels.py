class Solution:
    def partition_labels(self, s: str) -> list[int]:
        last = {ch: i for i, ch in enumerate(s)}
        sizes = []
        end = size = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, last[ch])
            if i == end:
                sizes.append(size)
                size = 0
        return sizes
