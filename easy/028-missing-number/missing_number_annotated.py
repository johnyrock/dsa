class Solution:
    # XOR the complete range with the given values so matching values cancel.
    def missing_number(self, nums: list[int]) -> int:
        # Seed the only range value that has no list index: len(nums).
        missing = len(nums)
        # Pair each index from zero through len(nums)-1 with its present value.
        for index, number in enumerate(nums):
            # Every present range value cancels, leaving the absent one.
            missing ^= index ^ number
        # The remaining XOR value is the missing number.
        return missing
