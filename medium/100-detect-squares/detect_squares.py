from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.count_at = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.count_at[(point[0], point[1])] += 1

    def count(self, point: list[int]) -> int:
        px, py = point
        total = 0
        for (x, y), n in self.count_at.items():
            if x == px or abs(x - px) != abs(y - py):
                continue
            total += n * self.count_at[(x, py)] * self.count_at[(px, y)]
        return total
