from collections import defaultdict


class DetectSquares:
    # Store how many times each point has been added. Duplicates matter: two copies of a corner mean two distinct squares.
    def __init__(self):
        # Keys are (x, y) tuples; a missing key reads as 0, which is exactly what a multiplication needs.
        self.count_at = defaultdict(int)

    # Record one more copy of this point.
    def add(self, point: list[int]) -> None:
        self.count_at[(point[0], point[1])] += 1

    # Count axis-aligned squares that use the query point as one corner and stored points as the other three.
    def count(self, point: list[int]) -> int:
        px, py = point
        total = 0
        # Try every stored point as the corner diagonally opposite the query point.
        for (x, y), n in self.count_at.items():
            # A diagonal corner must be offset by the same non-zero distance in x and in y; anything else is not a square.
            if x == px or abs(x - px) != abs(y - py):
                continue
            # The other two corners are forced: one shares y with the query, one shares x. Multiply the copies of all three.
            total += n * self.count_at[(x, py)] * self.count_at[(px, y)]
        return total
