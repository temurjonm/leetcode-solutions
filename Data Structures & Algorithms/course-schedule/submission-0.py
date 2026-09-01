class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        needed = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            needed[course] += 1

        queue = deque()

        for course in range(numCourses):
            if needed[course] == 0:
                queue.append(course)

        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            for next_course in graph[course]:
                needed[next_course] -= 1

                if needed[next_course] == 0:
                    queue.append(next_course)

        return finished == numCourses
