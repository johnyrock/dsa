class Solution:
    # Return every distinct subset of a list that may contain repeated values.
    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        # Sort so equal values sit next to each other; the duplicate check below only compares neighbours.
        nums = sorted(nums)
        # The subsets collected so far.
        result = []
        # The one subset under construction, shared by every recursive call and edited in place.
        path = []

        # Extend path using only elements at index >= start, so each subset is built in index order.
        def backtrack(start: int) -> None:
            # Every node of the recursion tree is a subset, so record it on entry (copied, since path keeps mutating).
            result.append(path[:])
            for i in range(start, len(nums)):
                # Same value as the previous candidate, and that previous candidate was a *sibling choice* at this level (i > start): choosing it again would rebuild a subset already produced. Skip it.
                # When i == start the previous equal value was chosen by the parent call, so this is a legitimate second copy, not a duplicate.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Choose: put nums[i] into the subset.
                path.append(nums[i])
                # Recurse: everything that can follow nums[i] must come from indices after i.
                backtrack(i + 1)
                # Undo: remove nums[i] so the next iteration of the loop starts from the same prefix.
                path.pop()

        # Start with the empty prefix and the whole array available.
        backtrack(0)
        return result
