class Solution:
    # Define the function that takes a list of integers and reports whether any value repeats.
    def contains_duplicate(self, nums: list[int]) -> bool:
        # Create an empty set to hold every value we have already walked past. A set stores membership only, which is all this problem needs.
        seen = set()
        # Walk through the list once. We only care about the values here, so there is no need for enumerate.
        for n in nums:
            # Ask whether this exact value showed up earlier. Set membership is O(1) on average, which is what keeps the whole thing to a single pass.
            if n in seen:
                # A repeat exists, so the answer is settled and we can stop immediately without looking at the rest of the list.
                return True
            # Otherwise record the current value so a later element can match against it. This happens after the check, so an element never matches itself.
            seen.add(n)
        # The loop finished without ever finding a repeat, so every value was distinct.
        return False
