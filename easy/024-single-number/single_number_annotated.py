class Solution:
    # XOR every value so equal pairs cancel each other.
    def single_number(self, nums: list[int]) -> int:
        # Zero is XOR's identity value.
        unique = 0
        # Fold every number into the running XOR.
        for number in nums:
            # x XOR x is zero, so duplicated values disappear.
            unique ^= number
        # The only unpaired value remains.
        return unique
