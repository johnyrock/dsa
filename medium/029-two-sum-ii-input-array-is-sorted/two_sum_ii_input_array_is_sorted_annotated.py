class Solution:
    # Take a sorted (non-decreasing) list and a target; return the 1-based indices of the two numbers that add to target.
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        # One pointer at the smallest value, one at the largest. The pair they point to is the only candidate we look at each round.
        left, right = 0, len(numbers) - 1
        # Strictly less: the two indices must be different, so the pointers stop before they meet.
        while left < right:
            # The sum of the current pair decides which pointer has to move.
            total = numbers[left] + numbers[right]
            if total == target:
                # The problem wants 1-based positions, so shift both indices up by one.
                return [left + 1, right + 1]
            if total < target:
                # Too small: the only way to get bigger is a larger left value, because right is already the largest available.
                left += 1
            else:
                # Too big: the only way to get smaller is a smaller right value, because left is already the smallest available.
                right -= 1
        # The problem guarantees exactly one answer, so this is never reached; it keeps the return type honest.
        return []
