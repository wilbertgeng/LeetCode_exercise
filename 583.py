"""583. Delete Operation for Two Strings"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ########## Practice
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return m+n - 2*dp[-1][-1]








        ##############
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])


        return (m + n - 2 * dp[m][n])
