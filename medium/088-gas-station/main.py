from gas_station import Solution

solution = Solution()

for gas, cost in (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), ([2, 3, 4], [3, 4, 3]), ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])):
    print(gas, cost, solution.can_complete_circuit(gas, cost))
