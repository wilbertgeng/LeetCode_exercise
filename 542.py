"""542. 01 Matrix"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ## Practice: BFS
        def bfs(i, j):
            q = deque()
            node = (i, j)
            q.append((node, 0))
            visited = set()

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                node, depth = q.popleft()
                i, j = node
                if matrix[i][j] == 0:
                    return depth
                visited.add(node)
                for dir in directions:
                    newX, newY = i + dir[0], j + dir[1]
                    if newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0]) and (newX, newY) not in visited:
                        q.append(((newX, newY), depth + 1))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = bfs(i,j)
        return matrix



        ####### Iteration:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                    if i > 0 and matrix[i][j] > matrix[i-1][j]:
                        matrix[i][j] = matrix[i-1][j] + 1
                    if j > 0 and matrix[i][j] > matrix[i][j-1]:
                        matrix[i][j] = matrix[i][j-1] + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i+1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i+1][j] + 1
                    if j + 1 < n and matrix[i][j+1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j+1] + 1
        return matrix
