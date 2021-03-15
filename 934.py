"""934. Shortest Bridge"""

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        res = float('inf')
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or A[i][j] == "#" or A[i][j] == 0:
                return
            A[i][j] = '#'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        def bfs(node, depth, res):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = deque()
            q.append((node, depth))
            visited = set()
            while q:
                node, depth = q.popleft()
                i, j = node
                if A[i][j] == "#":
                    res = min(res, depth)
                    return
                visited.add(node)
                for dir in directions:
                    newX, newY = i + dir[0], j + dir[1]
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and A[newX][newY] != "#" and A[newX][newY] not in visited:
                        q.append(((newX, newY), depth + 1))

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    break
            break

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    bfs((i, j), 0, res)

        return res
