class Solution:
    # Add one by propagating a carry from the least significant digit leftward.
    def plus_one(self, digits: list[int]) -> list[int]:
        # Start at the rightmost, least significant digit and move left.
        for index in range(len(digits) - 1, -1, -1):
            # Any digit below nine absorbs the increment and stops the carry.
            if digits[index] < 9:
                digits[index] += 1
                return digits
            # A nine becomes zero and carries one to the next position.
            digits[index] = 0
        # Every digit was nine, so the carry creates a new leading one.
        return [1] + digits
