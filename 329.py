"""329. Longest Increasing Path in a Matrix"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]

        def dfs(i, j):

            if not dp[i][j]:
                val = matrix[i][j]
                if i+1 < m and matrix[i+1][j] > val:
                    u = dfs(i+1, j)
                else:
                    u = 0
                if i-1 >=0 and matrix[i-1][j] > val:
                    d = dfs(i-1, j)
                else:
                    d = 0
                if j+1 < n and matrix[i][j+1] > val:
                    r = dfs(i, j+1)
                else:
                    r = 0
                if j-1 >= 0 and matrix[i][j-1] > val:
                    l = dfs(i, j-1)
                else:
                    l = 0
                dp[i][j] = max(u, d, l, r) + 1

            return dp[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res









####
