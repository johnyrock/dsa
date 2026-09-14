class Solution:
    # Build each bit count from the count of its binary prefix.
    def count_bits(self, n: int) -> list[int]:
        # Include a slot for every value from zero through n.
        counts = [0] * (n + 1)
        # Fill answers in increasing order so shifted prefixes are already known.
        for value in range(1, n + 1):
            # Right shift drops the last bit; AND one extracts that dropped bit.
            counts[value] = counts[value >> 1] + (value & 1)
        # Return every requested Hamming weight.
        return counts
