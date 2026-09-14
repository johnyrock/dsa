class Solution:
    # Reverse exactly the 32 bits of an unsigned integer.
    def reverse_bits(self, n: int) -> int:
        # Accumulate the reversed bits from left to right.
        result = 0
        # The problem fixes the width at 32, including leading zeros.
        for _ in range(32):
            # Shift the output left and append n's current lowest bit.
            result = (result << 1) | (n & 1)
            # Expose the next input bit for the next iteration.
            n >>= 1
        # The accumulator now has every bit in reverse position.
        return result
