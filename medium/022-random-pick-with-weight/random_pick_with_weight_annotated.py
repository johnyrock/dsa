import bisect
import random


class Solution:
    def __init__(self, w: list[int]) -> None:
        # prefix[i] = sum of w[0..i], the running total. Index i "owns" the
        # half-open range (prefix[i-1], prefix[i]] of the number line.
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pick_index(self) -> int:
        # Pick a uniform random point on [1, total]. The probability it lands
        # in index i's range is exactly w[i] / total, which is what "weighted
        # random pick" means.
        target = random.randint(1, self.total)
        # Binary search for the first prefix sum >= target — that's the index
        # whose range contains this point.
        return bisect.bisect_left(self.prefix, target)
