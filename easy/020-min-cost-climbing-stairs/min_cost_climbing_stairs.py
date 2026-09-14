class Solution:
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        previous, current = 0, 0
        for step_cost in cost:
            previous, current = current, min(previous, current) + step_cost
        return min(previous, current)
