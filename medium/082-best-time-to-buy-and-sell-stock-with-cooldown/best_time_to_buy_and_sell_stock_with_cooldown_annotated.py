class Solution:
    # Return the most profit from any number of buy/sell round trips, given that the day after a sell must be skipped.
    def max_profit(self, prices: list[int]) -> int:
        # Three states, each the best cash balance at the end of the current day. hold: own a share. sold: sold it today, so tomorrow is a forced cooldown. rest: own nothing and are free to buy. Nothing has been bought yet, so hold starts impossible (-inf) and the other two start at 0.
        hold, sold, rest = float("-inf"), 0, 0  # best cash while holding / just sold / free to buy
        # Process one day at a time; each day every state is recomputed from the previous day's values.
        for price in prices:
            # hold: keep holding, or buy today, which is only allowed from rest (not from sold, that is the cooldown rule). sold: the only way in is to sell what you were holding. rest: stay resting, or arrive from yesterday's sell after the cooldown. The tuple assignment reads all three old values before writing any new one.
            hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
        # Ending while still holding a share can never beat having sold it, so the answer is the better of the two cash-only states.
        return max(sold, rest)
