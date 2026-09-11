class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1  # product of everything to the left of i
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1  # product of everything to the right of i
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
