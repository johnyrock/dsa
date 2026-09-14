class Solution:
    # Add two integers without + or -, using XOR for the digit sums and AND-shift for the carries, inside a simulated 32-bit register.
    def get_sum(self, a: int, b: int) -> int:
        # All ones in the low 32 bits. ANDing with it throws away anything above bit 31, which is what a fixed-width register would do on its own.
        MASK = 0xFFFFFFFF
        # The largest positive 32-bit signed value. Anything above it in the masked register is a negative number in two's complement.
        MAX_INT = 0x7FFFFFFF
        # Keep going while there is still a carry to add in.
        while b != 0:
            # a ^ b adds every bit position without carrying; (a & b) << 1 is the carry each position sends one bit to the left. Both are masked so the loop cannot run forever on a negative operand.
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # If bit 31 is clear the masked value is the answer. If it is set, undo the mask: a ^ MASK flips all 32 bits, and ~ turns that into the matching negative Python int.
        return a if a <= MAX_INT else ~(a ^ MASK)
