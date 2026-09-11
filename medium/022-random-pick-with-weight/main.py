import random
from random_pick_with_weight import Solution

random.seed(0)
solution = Solution([1, 3])
print([solution.pick_index() for _ in range(10)])
