class Solution:
    # Return every subset (the power set) of a list of distinct integers, in any order.
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # The answers collected so far. There will be exactly 2^len(nums) of them.
        result = []
        # The one subset under construction, shared by every recursive call and edited in place.
        path = []

        # Extend path using only elements at index >= start, so each subset is built in index order exactly once.
        def backtrack(start: int) -> None:
            # Every node of the recursion tree IS a subset, so record it on entry. Copy with [:] because path keeps mutating after this.
            result.append(path[:])
            # Try each remaining element as the next member. Starting at `start`, never before it, prevents [2,1] from being generated after [1,2].
            for i in range(start, len(nums)):
                # Choose: put nums[i] into the subset.
                path.append(nums[i])
                # Recurse: everything that can follow nums[i] must come from indices after i.
                backtrack(i + 1)
                # Undo: remove nums[i] so the next iteration of the loop starts from the same prefix.
                path.pop()

        # Start with the empty prefix and the whole array available.
        backtrack(0)
        return result
