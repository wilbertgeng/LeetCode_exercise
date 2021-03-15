"""417. Pacific Atlantic Water Flow"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """ a good template for DFS """
        """this is a what I normally do for a dfs helper method for exploring a matrix"""
        #### Practice
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False]*n for _ in range(m)]
        a_visited = [[False]*n for _ in range(m)]
        self.directions = [(1, 0),(-1, 0),(0, 1),(0, -1)] ## !! write this before dfs
        for i in range(m):
            self.dfs(i, 0, p_visited, matrix)
        for j in range(n):
            self.dfs(0, j, p_visited, matrix)
        for i in range(m):
            self.dfs(i, n-1, a_visited, matrix)
        for j in range(n):
            self.dfs(m-1, j, a_visited, matrix)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, i, j, visited, matrix):
        m = len(matrix) ## !! write in function again 
        n = len(matrix[0])
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] < matrix[i][j] or visited[x][y]:
                continue
            self.dfs(x, y, visited, matrix)

#########
    def dfs(self, i, j, matrix, visited, m, n):
        if visited:
    # return or return a value
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] < matrix[i][j] (or a condition you want to skip this round):
                continue
        # do something like
        visited[i][j] = True
        # explore the next level like
        self.dfs(x, y, matrix, visited, m, n)

        ### R1:
        if not matrix:
            return []
        # build directions
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(matrix)
        m = len(matrix[0])
        ## build n x m matrix see if it's visited
        p_visited = [[False for _ in range(m)] for _ in range(n)]
        a_visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited)
            self.dfs(matrix, i, m-1, a_visited)

        for j in range(m):
            self.dfs(matrix, 0, j, p_visited)
            self.dfs(matrix, n-1, j, a_visited)

        result = []
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, matrix, i, j, visited):
        n = len(matrix)
        m = len(matrix[0])
        # when dfs called, meaning its caller already verified this point
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] < matrix[i][j] or visited[x][y]:
                continue
            self.dfs(matrix, x, y, visited)
