"""210. Course Schedule II"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ## Practice:
        graph = collections.defaultdict(list)
        num_pre = [0]*numCourses
        for after, prev in prerequisites:
            graph[prev].append(after)
            num_pre[after] += 1
        coursesCanBeTaken = []
        for i in range(numCourses):
            if num_pre[i] == 0:
                coursesCanBeTaken.append(i)
        res = []
        while coursesCanBeTaken:
            course = coursesCanBeTaken.pop()
            res.append(course)
            for c in graph[course]:
                num_pre[c] -= 1
                if num_pre[c] == 0:
                    coursesCanBeTaken.append(c)
        return res if len(res) == numCourses else []


        ## bfs
        graph = [[] for _ in range(numCourses)]
        num_pre = [0]*numCourses
        for after, pre in prerequisites:
            graph[pre].append(after)
            num_pre[after] += 1
        coursesCanBeTaken = [i for i in range(numCourses) if num_pre[i] == 0]
        res = []
        while coursesCanBeTaken:
             courseTaken = coursesCanBeTaken.pop(0)
             res.append(courseTaken)
             for j in graph[courseTaken]:
                 num_pre[j] -= 1
                 if num_pre[j] == 0:
                     coursesCanBeTaken.append(j)
        return res if len(res) == numCourses else []

        ## DFS
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        result = []
        def dfs(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = -1

            for j in graph[i]:
                if not dfs(j):
                    return False
            result.append(i)
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result
