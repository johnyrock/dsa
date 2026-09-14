class Solution:
    # Treat the array as a linked list where index i points to index nums[i]; the duplicate is the entry point of the cycle.
    def find_duplicate(self, nums: list[int]) -> int:
        # Both pointers start at index 0. Index 0 is never a target (values are >= 1), so it is guaranteed to sit outside the cycle, which Floyd's argument needs.
        slow = fast = 0
        # Phase 1: advance slow one hop and fast two hops until they land on the same index. A do-while shape is needed because they start equal.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # The first meeting point is somewhere on the cycle, but not necessarily at its entrance.
            if slow == fast:
                break
        # Phase 2: a second pointer starts back at 0. The distance from 0 to the entrance equals the distance from the meeting point to the entrance (mod cycle length), so walking both at speed 1 makes them meet exactly at the entrance.
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        # The entrance is the index with two incoming edges, i.e. the value that appears twice in nums.
        return slow
