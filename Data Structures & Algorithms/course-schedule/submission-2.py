class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        needed = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            needed[course] += 1
       
        queue = deque()

        for i in range(numCourses):
            if needed[i] == 0:
                queue.append(i)

        totalCourses = 0
        
        while queue:
            course = queue.popleft() 
            totalCourses += 1

            for next_course in graph[course]:
                needed[next_course] -= 1

                if needed[next_course] == 0:
                    queue.append(next_course)

        return totalCourses == numCourses
