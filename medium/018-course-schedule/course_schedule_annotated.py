from collections import deque


class Solution:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        # Build the graph: edge pre -> course means pre must be taken first.
        graph = [[] for _ in range(num_courses)]
        # indegree[c] = number of unmet prerequisites for course c.
        indegree = [0] * num_courses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Courses with no prerequisites can be taken immediately.
        queue = deque(c for c in range(num_courses) if indegree[c] == 0)
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            # Taking `course` satisfies one prerequisite for each course that
            # depends on it; once a dependent has none left, it becomes takeable.
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # If every course was eventually taken, there was no cycle. If a cycle
        # exists, the courses in it never reach indegree 0 and are never queued.
        return taken == num_courses
