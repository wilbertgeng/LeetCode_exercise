"""Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ## Practice:
        grid = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[-1][-1]




        # R3:
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

        # R2: Done

        # R1:
        matrix = [[1 for x in range(m)] for x in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return matrix[m-1][n-1]
