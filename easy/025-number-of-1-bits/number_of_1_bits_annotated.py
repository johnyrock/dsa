class Solution:
    # Count set bits by clearing one set bit per iteration.
    def hamming_weight(self, n: int) -> int:
        # Count how many one bits are removed.
        count = 0
        # Stop once no set bits remain.
        while n:
            # n & (n - 1) clears n's lowest set bit.
            n &= n - 1
            # One set bit was cleared.
            count += 1
        # The number of removals is the Hamming weight.
        return count
