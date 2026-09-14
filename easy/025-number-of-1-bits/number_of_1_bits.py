class Solution:
    def hamming_weight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
