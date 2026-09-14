class Solution:
    # Take the fuel available at each station and the fuel needed to reach the next one; return the only start index that completes the loop, or -1.
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        # If the whole circuit burns more than it provides, no start can work. Conversely, if it does not, some start always works, so the rest of the function never needs to re-check.
        if sum(gas) < sum(cost):
            return -1
        # Candidate start index; we assume 0 until the evidence rules it out.
        start = 0
        # Fuel in the tank since we left the current candidate.
        tank = 0
        # One pass around the stations in order. We never wrap: the total check above guarantees the survivor is right.
        for i in range(len(gas)):
            # Fill up at station i and drive to station i + 1; this is the net fuel change of that leg.
            tank += gas[i] - cost[i]
            # Running dry between i and i + 1 means the candidate fails, and so does every station between the candidate and i (each of those would arrive here with even less fuel).
            if tank < 0:
                # So the next possible start is the station just past the failure point ...
                start = i + 1
                # ... with an empty tank, since nothing carries over.
                tank = 0
        # The last candidate never went negative from its start to the end of the array; the total check covers the wrap-around.
        return start
