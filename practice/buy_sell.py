# prices = [7, 1, 5, 3, 6, 4]

def largest_proft(prices):
    min_price = float("inf")
    best_price = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best_price:
            best_price = price - min_price

    return best_price