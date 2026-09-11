import bisect
import random


class Solution:
    def __init__(self, w: list[int]) -> None:
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pick_index(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)
