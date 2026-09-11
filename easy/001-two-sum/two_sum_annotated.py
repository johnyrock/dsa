class Solution:
    # Define the function that takes a list of integers and the target sum we're looking for.
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary that will map each number we've already visited to the index where it appeared.
        seen = {}
        # Walk through the list once, getting both the position i and the value n at each step.
        for i, n in enumerate(nums):
            # Work out which number would need to pair with n to hit the target.
            complement = target - n
            # Check whether that needed number already showed up earlier in the list. Dictionary lookups are O(1), which is what keeps the whole thing to a single pass.
            if complement in seen:
                # We found the pair, so return the earlier number's stored index alongside the current one.
                return [seen[complement], i]
            # Otherwise record the current number and its index so a later element can pair with it. This happens after the check, so an element never pairs with itself.
            seen[n] = i
        # If the loop finishes with no pair found, return an empty list.
        return []
