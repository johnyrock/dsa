from collections import deque


class Solution:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(num_courses)]
        indegree = [0] * num_courses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(c for c in range(num_courses) if indegree[c] == 0)
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return taken == num_courses
