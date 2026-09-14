class Solution:
    # Take the jump lengths and report whether index 0 can reach the last index.
    def can_jump(self, nums: list[int]) -> bool:
        # reach is the farthest index we know we can stand on so far. Index 0 is always reachable, so start there.
        reach = 0
        # Walk the array left to right; i is the index we are trying to stand on, n is the longest jump allowed from it.
        for i, n in enumerate(nums):
            # If i is beyond everything reachable, nothing to the left could carry us here, and nothing to the right can help either.
            if i > reach:
                return False
            # Standing on i lets us land anywhere up to i + n; keep the farthest frontier seen so far.
            reach = max(reach, i + n)
        # The loop only survives to the end if every index, including the last one, was within reach when we got there.
        return True
