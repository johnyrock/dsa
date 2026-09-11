class Solution:
    # Define the function that takes the array and returns, for each slot, the product of all the other slots.
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # The output doubles as our only scratch space. Start every slot at 1, the identity for multiplication.
        result = [1] * n

        # First sweep, left to right. prefix is the running product of everything strictly before index i.
        prefix = 1  # product of everything to the left of i
        for i in range(n):
            # Store the left product first: it must not include nums[i] itself.
            result[i] = prefix
            # Now fold nums[i] in, so the next slot sees everything up to and including i.
            prefix *= nums[i]

        # Second sweep, right to left. suffix is the running product of everything strictly after index i.
        suffix = 1  # product of everything to the right of i
        for i in range(n - 1, -1, -1):
            # result[i] already holds the left product; multiplying by the right product completes it.
            result[i] *= suffix
            # Fold nums[i] in for the slots further left.
            suffix *= nums[i]

        # Each slot is now (product of the left) × (product of the right), which is everything except itself.
        return result
