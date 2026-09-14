class Solution:
    def is_happy(self, n: int) -> bool:
        slow = n
        fast = self._next(n)
        while fast != 1 and slow != fast:
            slow = self._next(slow)
            fast = self._next(self._next(fast))
        return fast == 1

    def _next(self, value: int) -> int:
        total = 0
        while value:
            value, digit = divmod(value, 10)
            total += digit * digit
        return total
