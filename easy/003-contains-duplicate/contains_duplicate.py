class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        seen = set()  # values already visited
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
