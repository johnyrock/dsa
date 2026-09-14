from walls_and_gates import Solution

solution = Solution()

INF = 2147483647
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
]
solution.walls_and_gates(rooms)
for row in rooms:
    print(row)
