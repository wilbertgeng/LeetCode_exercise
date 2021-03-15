"""1143. Longest Common Subsequence"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i, a in enumerate(text1):
            for j, b in enumerate(text2):
                dp[i+1][j+1] = dp[i][j] + 1 if a == b else max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]
        
