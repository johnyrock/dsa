from collections import deque


class Solution:
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(num_courses)]
        indegree = [0] * num_courses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(c for c in range(num_courses) if indegree[c] == 0)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return order if len(order) == num_courses else []
