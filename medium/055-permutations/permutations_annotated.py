class Solution:
    # Return every ordering of a list of distinct integers.
    def permute(self, nums: list[int]) -> list[list[int]]:
        # The permutations found so far. There will be exactly len(nums)! of them.
        result = []
        # The one ordering under construction, shared by every recursive call and edited in place.
        path = []
        # used[i] is True while nums[i] is somewhere in path. Checking this flag is O(1); scanning path would be O(n).
        used = [False] * len(nums)

        # Fill the next slot of path with any element not yet used.
        def backtrack() -> None:
            # Every slot filled: path is a complete permutation. Copy it, because path keeps changing afterwards.
            if len(path) == len(nums):
                result.append(path[:])
                return
            # Unlike subsets, the loop always starts at 0: an element skipped earlier can still come later, which is what makes [2,1] reachable after [1,2].
            for i in range(len(nums)):
                # Already in path, so it cannot appear a second time.
                if used[i]:
                    continue
                # Choose: mark nums[i] taken and put it in the next slot.
                used[i] = True
                path.append(nums[i])
                # Recurse to fill the remaining slots from what is still unused.
                backtrack()
                # Undo both halves of the choice so the next iteration starts from the same state.
                path.pop()
                used[i] = False

        # Start with an empty path and nothing used.
        backtrack()
        return result
