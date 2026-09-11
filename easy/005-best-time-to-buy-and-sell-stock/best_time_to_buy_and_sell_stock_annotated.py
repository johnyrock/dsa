class Solution:
    # Define the function that takes the list of daily prices and returns the best profit from a single buy-then-sell.
    def max_profit(self, prices: list[int]) -> int:
        # Track the cheapest price seen so far. Starting at infinity means the very first day always becomes the minimum.
        min_price = float("inf")  # cheapest day seen so far
        # Track the best profit found so far. It starts at 0 because doing nothing is always allowed, which is what keeps the answer from going negative.
        best = 0
        # Walk through the prices once, in order. Iterating forward is what guarantees the buy day always comes before the sell day.
        for price in prices:
            # If today is cheaper than anything before it, today becomes the new best day to have bought.
            if price < min_price:
                # Record the new minimum. We do not update the profit here, because selling on the same day we buy earns nothing.
                min_price = price
            # Otherwise today is a candidate sell day: check whether selling now beats the best profit we have already banked.
            elif price - min_price > best:
                # Selling today at the cheapest earlier price is the new best trade.
                best = price - min_price
        # After one pass, best holds the largest profit available, or 0 if prices never rose.
        return best
