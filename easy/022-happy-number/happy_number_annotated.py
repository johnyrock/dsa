class Solution:
    # Follow the digit-square sequence with a slow and a fast runner.
    def is_happy(self, n: int) -> bool:
        # The slow runner advances one transformation at a time.
        slow = n
        # The fast runner begins one transformation ahead.
        fast = self._next(n)
        # Reaching one succeeds; meeting elsewhere proves a cycle.
        while fast != 1 and slow != fast:
            # Advance the slow runner once.
            slow = self._next(slow)
            # Advance the fast runner twice.
            fast = self._next(self._next(fast))
        # Only the special value one represents a happy sequence.
        return fast == 1

    # Replace a number with the sum of its squared decimal digits.
    def _next(self, value: int) -> int:
        # Accumulate the digit-square total.
        total = 0
        # Peel digits from right to left.
        while value:
            # divmod returns the shortened value and its removed digit together.
            value, digit = divmod(value, 10)
            # Add this digit's square to the next sequence value.
            total += digit * digit
        # This transformed number is the next state.
        return total
