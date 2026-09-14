class Solution:
    # Return the cheapest cost to step beyond the final stair.
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        # Starting at step zero or one costs nothing before stepping on either.
        previous, current = 0, 0
        # Extend the cheapest path to each paid stair.
        for step_cost in cost:
            # This stair can be reached from either of the two previous positions.
            previous, current = current, min(previous, current) + step_cost
        # The top is reachable from either of the last two stairs without another cost.
        return min(previous, current)
