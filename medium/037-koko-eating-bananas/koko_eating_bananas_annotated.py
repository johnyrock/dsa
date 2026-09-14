class Solution:
    # Define the function that takes the pile sizes and the hour budget and returns the slowest speed that still finishes in time.
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        # The answer lives in [1, max(piles)]: speed 1 is the slowest possible, and any speed above the biggest pile clears every pile in one hour, so going faster cannot help.
        lo, hi = 1, max(piles)
        # Shrink the range until one candidate is left. lo < hi (not <=) because hi is always a speed that works, so we never need to test past it.
        while lo < hi:
            # Try the midpoint speed. Rounding down is fine because a failing mid moves lo to mid + 1, so the range always shrinks.
            mid = (lo + hi) // 2
            # Hours at speed mid: each pile takes ceil(pile / mid) hours, written with integer arithmetic to avoid floats. Koko cannot carry leftover capacity from one pile into the next.
            hours = sum((pile + mid - 1) // mid for pile in piles)
            # Feasible: mid works, so the answer is mid or something slower. Keep mid in the range because it might be the answer itself.
            if hours <= h:
                hi = mid
            # Too slow: mid is ruled out, and so is everything below it, since a slower speed takes at least as many hours.
            else:
                lo = mid + 1
        # lo == hi here, and it is the smallest speed the feasibility test never rejected.
        return lo
