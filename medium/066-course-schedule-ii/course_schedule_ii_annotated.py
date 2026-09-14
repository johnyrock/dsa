from collections import deque


class Solution:
    # Define the function that takes the course count and prerequisite pairs and returns one valid order, or [] if none exists.
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        # Adjacency list: graph[pre] lists the courses that pre unlocks.
        graph = [[] for _ in range(num_courses)]
        # indegree[c] = how many prerequisites of c have not been taken yet.
        indegree = [0] * num_courses
        # Each pair [course, pre] means pre must come first, so the edge runs pre -> course.
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Every course with no prerequisites can be taken right now; they seed the queue.
        queue = deque(c for c in range(num_courses) if indegree[c] == 0)
        # The order courses are popped is the topological order we return.
        order = []
        while queue:
            # Take the course at the front. FIFO keeps the order deterministic, but any zero-indegree course would do.
            course = queue.popleft()
            order.append(course)
            # Taking it satisfies one prerequisite for everything it unlocks.
            for nxt in graph[course]:
                indegree[nxt] -= 1
                # Only enqueue when the LAST prerequisite is satisfied, otherwise a course would be scheduled twice.
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # If a cycle exists, the courses in it never reach indegree 0 and never get popped, so order is short. Return [] then.
        return order if len(order) == num_courses else []
