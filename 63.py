"""63. Unique Paths II"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1- obstacleGrid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]*(1 - obstacleGrid[i][0])
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]*(1 - obstacleGrid[0][j])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])*(1 - obstacleGrid[i][j])
    #    print(dp)
        return dp[-1][-1]

s = Solution()
res = s.uniquePathsWithObstacles([[0,0,0],[0,1,1],[0,0,0]])
print(res)
