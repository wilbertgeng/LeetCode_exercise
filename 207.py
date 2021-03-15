"""207. Course Schedule"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #### practice:
        graph = collections.defaultdict(list)
        numOfPre = [0]*numCourses
        for after, pre in prerequisites:
            graph[pre].append(after)
            numOfPre[after] += 1
        coursesCanBeTaken = [i for i in range(numCourses) if numOfPre[i]==0]

        for i in coursesCanBeTaken:
            for j in graph[i]:
                numOfPre[j] -= 1
                if numOfPre[j] == 0:
                    coursesCanBeTaken.append(j)
        return numCourses == len(coursesCanBeTaken)







        ###practice
        num_pre = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for after, pre in prerequisites:
            graph[pre].append(after)
            num_pre[after] += 1
        coursesCanBeTaken = [i for i in range(numCourses) if num_pre[i]==0]
        for i in coursesCanBeTaken:
            for j in graph[i]:
                num_pre[j] -= 1
                if num_pre[j] == 0:
                    coursesCanBeTaken.append(j)
        return len(coursesCanBeTaken) == numCourses
        ##
        numOfPre = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for after, pre in prerequisites:
            graph[pre].append(after)
            numOfPre[after] += 1
        coursesCanBeTaken = [i for i in range(numCourses) if numOfPre[i] == 0]
        for i in coursesCanBeTaken:
            for j in graph[i]:
                numOfPre[j] -= 1
                if numOfPre[j] == 0:
                    coursesCanBeTaken.append(j)
        return len(coursesCanBeTaken) == numCourses

        # BFS + color: 本题不需要使用拓扑排序，只需要检测有向图是否存在环即可
        degree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for b, a in prerequisites:
            graph[a].append(b)
            degree[b] += 1

        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

        # create graph
        # DFS
        # can't be: graph = [[]*numCourses]
        # can't be: visit = [0*numCourses]
        graph = [[] for _ in range(numCourses)] # create graph
        visit = [0 for _ in range(numCourses)] # seen
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = -1

            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
